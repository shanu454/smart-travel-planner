"""Trips API router with CRUD and smart generation."""
from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Trip, ItineraryItem, Expense, PackingItem, TransportOption, TripFeedback
from app.schemas import (
    TripCreate,
    TripUpdate,
    TripResponse,
    TripDetailResponse,
    TripGenerateRequest,
    PaceUpdateRequest,
    BudgetSummaryResponse,
    PackingSummaryResponse,
    PackingItemResponse,
    ExpenseResponse,
    ItineraryItemResponse,
    TransportOptionResponse,
    TripFeedbackCreate,
    TripFeedbackResponse
)
from app.services.geocoding import search_places
from app.services.weather import get_weather_forecast
from app.services.wiki import get_destination_details
from app.services.planner import generate_smart_itinerary, generate_smart_packing_list

router = APIRouter(prefix="/api/trips", tags=["Trips"])


def calculate_days(start_str: str, end_str: str) -> int:
    try:
        s = datetime.strptime(start_str, "%Y-%m-%d")
        e = datetime.strptime(end_str, "%Y-%m-%d")
        return max(1, (e - s).days + 1)
    except Exception:
        return 1


@router.get("", response_model=List[TripResponse])
def list_trips(country: Optional[str] = None, db: Session = Depends(get_db)):
    """List all trips with total expenses and duration, optionally filtered by country."""
    query = db.query(Trip)
    if country:
        query = query.filter(Trip.country.ilike(f"%{country}%"))
    trips = query.order_by(Trip.created_at.desc()).all()
    results = []
    for t in trips:
        spent = db.query(func.sum(Expense.amount)).filter(Expense.trip_id == t.id).scalar() or 0.0
        days = calculate_days(t.start_date, t.end_date)
        res = TripResponse.from_orm(t)
        res.total_spent = round(float(spent), 2)
        res.days_count = days
        res.is_completed = bool(t.is_completed)
        res.completed_at = t.completed_at
        results.append(res)
    return results


@router.post("", response_model=TripDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    """Create a new trip manually."""
    # Lookup cover image if not provided
    cover = trip_in.cover_image
    if not cover:
        details = await get_destination_details(trip_in.destination)
        cover = details.get("image_url", "")

    new_trip = Trip(
        title=trip_in.title,
        destination=trip_in.destination,
        country=trip_in.country,
        latitude=trip_in.latitude,
        longitude=trip_in.longitude,
        start_date=trip_in.start_date,
        end_date=trip_in.end_date,
        travel_style=trip_in.travel_style,
        travel_pace=trip_in.travel_pace,
        total_budget=trip_in.total_budget,
        currency=trip_in.currency,
        cover_image=cover,
        notes=trip_in.notes
    )
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return get_trip_details(new_trip.id, db)


@router.post("/generate", response_model=TripDetailResponse, status_code=status.HTTP_201_CREATED)
async def generate_smart_trip(req: TripGenerateRequest, db: Session = Depends(get_db)):
    """Generate an end-to-end intelligent trip with geocoding, live weather, wiki image, itinerary & packing list."""
    # 1. Geocode destination if coordinates not set
    dest_name = req.destination.strip()
    lat = 0.0
    lon = 0.0
    country = req.country or "India"

    places = await search_places(dest_name, count=1)
    if places:
        first = places[0]
        lat = first["latitude"]
        lon = first["longitude"]
        if not country or country == "India":
            country = first.get("country", "India")

    # 2. Fetch destination Wikipedia extract and photo
    wiki_info = await get_destination_details(dest_name)
    cover_image = wiki_info.get("image_url", "")
    notes = wiki_info.get("extract", "")

    # 3. Fetch weather forecast for destination
    weather_data = None
    if lat != 0.0 or lon != 0.0:
        weather_data = await get_weather_forecast(lat, lon)

    # 4. Calculate trip duration
    days_count = calculate_days(req.start_date, req.end_date)

    # 5. Create Trip record
    travel_pace = req.travel_pace or "Moderate"
    trip_title = f"{days_count}-Day {dest_name} {req.travel_style.split('&')[0].strip()} Journey"
    trip = Trip(
        title=trip_title,
        destination=dest_name,
        country=country,
        latitude=lat,
        longitude=lon,
        start_date=req.start_date,
        end_date=req.end_date,
        travel_style=req.travel_style,
        travel_pace=travel_pace,
        total_budget=req.total_budget,
        currency=req.currency,
        cover_image=cover_image,
        notes=notes
    )
    db.add(trip)
    db.commit()
    db.refresh(trip)

    # 6. Generate smart itinerary activities
    activities = generate_smart_itinerary(
        destination=dest_name,
        country=country,
        lat=lat,
        lon=lon,
        start_date_str=req.start_date,
        end_date_str=req.end_date,
        travel_style=req.travel_style,
        travel_pace=travel_pace,
        total_budget=req.total_budget
    )
    for act in activities:
        db.add(ItineraryItem(
            trip_id=trip.id,
            day_number=act["day_number"],
            time_slot=act["time_slot"],
            title=act["title"],
            description=act["description"],
            location=act["location"],
            latitude=act["latitude"],
            longitude=act["longitude"],
            estimated_cost=act["estimated_cost"],
            category=act["category"],
            is_completed=False,
            order_index=act["order_index"]
        ))

    # 7. Generate smart packing checklist
    packing_list = generate_smart_packing_list(
        destination=dest_name,
        days_count=days_count,
        weather_forecast=weather_data,
        travel_style=req.travel_style
    )
    for item in packing_list:
        db.add(PackingItem(
            trip_id=trip.id,
            category=item["category"],
            item_name=item["item_name"],
            is_packed=False,
            is_suggested=True
        ))

    # 8. Generate smart transport options with realistic Indian costs
    dest_lower = dest_name.lower()
    transport_defaults = [
        ("Train", f"Vande Bharat / Express Train to {dest_name}", f"Intercity ➡️ {dest_name} Junction", 1600.0, "Book via IRCTC 15-30 days prior. Executive & AC Chair Car seats."),
        ("Cab/Taxi", f"Prepaid Airport / Railway Station Cab to Hotel", f"Station / Airport ➡️ City Center", 850.0, "Opt for official prepaid taxi counters or Uber/Ola pickup point."),
        ("Auto-Rickshaw", f"Local Sightseeing Auto-Rickshaw / E-Rickshaw Day Pass", f"Historic Monuments & Bazaars", 600.0, "Negotiate full-day or half-day rate in advance or ask for meter.")
    ]
    if "goa" in dest_lower:
        transport_defaults.append(("Scooter", "Goa Activa / Fascino Scooter Rental (Daily)", "North & South Goa Coastline", 450.0, "Carry physical driving license and helmet. Petrol bunks available along highway."))
    elif "varanasi" in dest_lower:
        transport_defaults.append(("Ferry", "Sunrise Handcrafted Wooden Boat (Assi to Manikarnika)", "Ganges River Ghats", 500.0, "Book early at Assi Ghat at dawn for peaceful photography."))
    elif "kerala" in dest_lower or "alleppey" in dest_lower:
        transport_defaults.append(("Ferry", "Alleppey Backwaters Public Ferry / Shikara Ride", "Vembanad Lake Canals", 600.0, "SWTD government ferry is affordable and scenic."))
    elif "jaipur" in dest_lower or "udaipur" in dest_lower:
        transport_defaults.append(("Cab/Taxi", f"Private AC Sedan for Forts & Palaces Sightseeing", f"Full Day {dest_name} Heritage Tour", 1800.0, "Includes fuel and chauffeur for 8 hours / 80 km."))

    for mode, title, route, cost, tips in transport_defaults:
        db.add(TransportOption(
            trip_id=trip.id,
            mode=mode,
            title=title,
            route=route,
            estimated_cost=cost,
            currency=trip.currency,
            booking_tips=tips,
            is_booked=False
        ))

    db.commit()
    return get_trip_details(trip.id, db)


@router.get("/{trip_id}", response_model=TripDetailResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    """Retrieve full details of a specific trip."""
    return get_trip_details(trip_id, db)


def get_trip_details(trip_id: int, db: Session) -> TripDetailResponse:
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Build Itinerary Items
    itinerary_items = [ItineraryItemResponse.from_orm(item) for item in trip.itinerary_items]

    # Build Expenses & Budget Summary
    expenses = [ExpenseResponse.from_orm(e) for e in trip.expenses]
    total_spent = sum(e.amount for e in expenses)
    remaining = max(0.0, trip.total_budget - total_spent)
    percent_used = round((total_spent / trip.total_budget * 100.0), 1) if trip.total_budget > 0 else 0.0

    by_category: dict = {}
    for e in expenses:
        by_category[e.category] = round(by_category.get(e.category, 0.0) + e.amount, 2)

    budget_summary = BudgetSummaryResponse(
        total_budget=trip.total_budget,
        total_spent=round(total_spent, 2),
        remaining_budget=round(remaining, 2),
        percent_used=percent_used,
        currency=trip.currency,
        by_category=by_category,
        recent_expenses=expenses[:5]
    )

    # Build Packing Summary
    packing_items = [PackingItemResponse.from_orm(p) for p in trip.packing_items]
    packed_count = sum(1 for p in packing_items if p.is_packed)
    total_packing = len(packing_items)
    pct_packed = round((packed_count / total_packing * 100.0), 1) if total_packing > 0 else 0.0

    packing_by_cat: dict = {}
    for p in packing_items:
        packing_by_cat.setdefault(p.category, []).append(p)

    packing_summary = PackingSummaryResponse(
        total_items=total_packing,
        packed_items=packed_count,
        percent_packed=pct_packed,
        by_category=packing_by_cat
    )

    transport_options = [TransportOptionResponse.from_orm(t) for t in trip.transport_options]

    days_count = calculate_days(trip.start_date, trip.end_date)
    fb_response = TripFeedbackResponse.from_orm(trip.feedback) if trip.feedback else None

    res = TripDetailResponse(
        id=trip.id,
        title=trip.title,
        destination=trip.destination,
        country=trip.country,
        latitude=trip.latitude,
        longitude=trip.longitude,
        start_date=trip.start_date,
        end_date=trip.end_date,
        travel_style=trip.travel_style,
        travel_pace=trip.travel_pace,
        total_budget=trip.total_budget,
        currency=trip.currency,
        cover_image=trip.cover_image,
        notes=trip.notes,
        is_completed=bool(trip.is_completed),
        completed_at=trip.completed_at,
        created_at=trip.created_at,
        total_spent=round(total_spent, 2),
        days_count=days_count,
        itinerary_items=itinerary_items,
        expenses=expenses,
        packing_items=packing_items,
        transport_options=transport_options,
        budget_summary=budget_summary,
        packing_summary=packing_summary,
        feedback=fb_response
    )
    return res


@router.patch("/{trip_id}/pace", response_model=TripDetailResponse)
def update_trip_pace(trip_id: int, req: PaceUpdateRequest, db: Session = Depends(get_db)):
    """Update travel pace and automatically re-synthesize day schedule activities to match."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    trip.travel_pace = req.travel_pace

    # Re-generate activities to match new pace
    db.query(ItineraryItem).filter(ItineraryItem.trip_id == trip.id).delete()

    new_acts = generate_smart_itinerary(
        destination=trip.destination,
        country=trip.country,
        lat=trip.latitude,
        lon=trip.longitude,
        start_date_str=trip.start_date,
        end_date_str=trip.end_date,
        travel_style=trip.travel_style,
        travel_pace=req.travel_pace,
        total_budget=trip.total_budget
    )
    for act in new_acts:
        db.add(ItineraryItem(
            trip_id=trip.id,
            day_number=act["day_number"],
            time_slot=act["time_slot"],
            title=act["title"],
            description=act["description"],
            location=act["location"],
            latitude=act["latitude"],
            longitude=act["longitude"],
            estimated_cost=act["estimated_cost"],
            category=act["category"],
            is_completed=False,
            order_index=act["order_index"]
        ))
    db.commit()
    db.refresh(trip)
    return get_trip_details(trip.id, db)


@router.put("/{trip_id}", response_model=TripDetailResponse)
@router.patch("/{trip_id}", response_model=TripDetailResponse)
def update_trip(trip_id: int, trip_in: TripUpdate, db: Session = Depends(get_db)):
    """Update trip details (budget, title, dates, etc.) and return refreshed details."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    update_data = trip_in.dict(exclude_unset=True)
    for field, val in update_data.items():
        setattr(trip, field, val)

    db.commit()
    db.refresh(trip)

    return get_trip_details(trip.id, db)


@router.delete("/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    """Delete a trip and all its associated data."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip)
    db.commit()
    return None


@router.post("/{trip_id}/complete", response_model=TripDetailResponse)
def complete_trip(trip_id: int, db: Session = Depends(get_db)):
    """Mark a trip as completed or toggle completion state."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    trip.is_completed = not bool(trip.is_completed)
    if trip.is_completed:
        trip.completed_at = datetime.utcnow()
    else:
        trip.completed_at = None

    db.commit()
    db.refresh(trip)
    return get_trip_details(trip.id, db)


@router.post("/{trip_id}/feedback", response_model=TripFeedbackResponse)
def submit_trip_feedback(trip_id: int, req: TripFeedbackCreate, db: Session = Depends(get_db)):
    """Submit or update traveler review and feedback for a trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Mark trip as completed if not already
    trip.is_completed = True
    if not trip.completed_at:
        trip.completed_at = datetime.utcnow()

    # Check if feedback already exists for this trip
    existing = db.query(TripFeedback).filter(TripFeedback.trip_id == trip_id).first()
    if existing:
        existing.rating_overall = req.rating_overall
        existing.rating_transit = req.rating_transit
        existing.rating_stays = req.rating_stays
        existing.rating_activities = req.rating_activities
        existing.rating_budget = req.rating_budget
        existing.recommend = req.recommend
        existing.best_highlights = req.best_highlights or ""
        existing.comments = req.comments or ""
        existing.tips_for_others = req.tips_for_others or ""
        existing.traveler_name = req.traveler_name or "Traveler"
        db.commit()
        db.refresh(existing)
        return existing

    new_fb = TripFeedback(
        trip_id=trip_id,
        rating_overall=req.rating_overall,
        rating_transit=req.rating_transit,
        rating_stays=req.rating_stays,
        rating_activities=req.rating_activities,
        rating_budget=req.rating_budget,
        recommend=req.recommend,
        best_highlights=req.best_highlights or "",
        comments=req.comments or "",
        tips_for_others=req.tips_for_others or "",
        traveler_name=req.traveler_name or "Traveler",
        created_at=datetime.utcnow()
    )
    db.add(new_fb)
    db.commit()
    db.refresh(new_fb)
    return new_fb


@router.get("/{trip_id}/feedback", response_model=TripFeedbackResponse)
def get_trip_feedback(trip_id: int, db: Session = Depends(get_db)):
    """Get traveler feedback for a specific trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    fb = db.query(TripFeedback).filter(TripFeedback.trip_id == trip_id).first()
    if not fb:
        raise HTTPException(status_code=404, detail="Feedback not found for this trip")
    return fb
