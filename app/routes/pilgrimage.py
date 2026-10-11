import re
from typing import List, Optional
from datetime import datetime, date, timedelta
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Trip, ItineraryItem, Expense, PackingItem, TransportOption
from app.schemas import TripDetailResponse
from app.routes.trips import get_trip_details
from app.services.pilgrimage import (
    PILGRIMAGE_CIRCUITS,
    ALL_DESTINATIONS_CATALOG,
    get_all_pilgrimage_circuits,
    get_all_destination_catalog_items,
    calculate_dham_budget,
    calculate_universal_destination_budget,
    get_indian_destination_image
)

router = APIRouter(prefix="/api/pilgrimage", tags=["Pilgrimage & Destination Budget"])


class PilgrimageEstimateRequest(BaseModel):
    circuit_id: Optional[str] = None
    destination: Optional[str] = None
    days: Optional[int] = None
    travel_tier: Optional[str] = "Standard"  # Budget, Standard, Premium
    num_travelers: Optional[int] = 1
    date: Optional[str] = None
    departure_time: Optional[str] = "06:00 AM"
    travel_style: Optional[str] = "Leisure & Sightseeing"


class PilgrimageGenerateRequest(BaseModel):
    circuit_id: Optional[str] = None
    destination: Optional[str] = None
    days: Optional[int] = None
    start_date: Optional[str] = None
    departure_time: Optional[str] = "06:00 AM"
    travel_tier: Optional[str] = "Standard"
    num_travelers: Optional[int] = 1
    travel_style: Optional[str] = "Leisure & Sightseeing"


@router.get("/circuits")
def list_circuits():
    """List sacred Dham and temple pilgrimage circuits."""
    return get_all_pilgrimage_circuits()


@router.get("/destinations")
def list_destinations():
    """List all supported Indian destination circuits (Temples, Heritage, Beaches, Mountains, etc.)."""
    return get_all_destination_catalog_items()


@router.post("/estimate-budget")
def estimate_budget(req: PilgrimageEstimateRequest):
    """Calculate instant, realistic budget breakdown for any Indian place (Dham, Heritage, Beach, Mountain, or custom city)."""
    res = calculate_universal_destination_budget(
        destination=req.destination,
        circuit_id=req.circuit_id,
        days=req.days,
        travel_tier=req.travel_tier,
        num_travelers=req.num_travelers,
        travel_style=req.travel_style or "Leisure & Sightseeing",
        departure_date=req.date
    )
    return res


@router.post("/generate-trip", response_model=TripDetailResponse, status_code=status.HTTP_201_CREATED)
def generate_pilgrimage_trip(req: PilgrimageGenerateRequest, db: Session = Depends(get_db)):
    """Automatically synthesize a complete multi-day journey for any destination in India with realistic transport, itinerary, and expenses."""
    # Find matching circuit or create custom destination
    circuit = None
    if req.circuit_id and req.circuit_id in ALL_DESTINATIONS_CATALOG:
        circuit = ALL_DESTINATIONS_CATALOG[req.circuit_id]
    elif req.destination:
        dest_clean = req.destination.strip().lower()
        for c in ALL_DESTINATIONS_CATALOG.values():
            if c["destination"].lower() in dest_clean or dest_clean in c["destination"].lower() or c["id"] == dest_clean:
                circuit = c
                break

    tier_label = req.travel_tier if req.travel_tier in ["Budget", "Standard", "Premium"] else "Standard"

    try:
        s_date = datetime.strptime(req.start_date, "%Y-%m-%d").date()
    except Exception:
        s_date = date.today() + timedelta(days=7)

    if circuit:
        # Predefined Catalog Destination / Dham Circuit
        trip_days = req.days if (req.days and req.days > 0) else circuit["recommended_days"]
        e_date = s_date + timedelta(days=trip_days - 1)

        budget_calc = calculate_universal_destination_budget(
            circuit_id=circuit["id"],
            days=trip_days,
            travel_tier=req.travel_tier,
            num_travelers=req.num_travelers,
            departure_date=req.start_date
        )

        style = circuit.get("category", "Spiritual & Pilgrimage")
        pace = "Relaxed" if trip_days >= 6 else ("Moderate" if trip_days >= 4 else "Fast-Paced")

        clean_circuit_title = re.sub(r'^\d+-Day\s*', '', circuit['title'])
        trip_title = f"{trip_days}-Day {clean_circuit_title} ({tier_label} Tier)"

        new_trip = Trip(
            title=trip_title,
            destination=circuit["destination"],
            country="India",
            latitude=circuit["latitude"],
            longitude=circuit["longitude"],
            start_date=s_date.isoformat(),
            end_date=e_date.isoformat(),
            travel_style=style,
            travel_pace=pace,
            total_budget=budget_calc["total_budget"],
            currency="INR",
            cover_image=circuit["cover_image"],
            notes=f"{circuit['description']} Planned for {req.num_travelers} traveler(s) at {tier_label} tier. Departure scheduled for {req.departure_time}."
        )
        db.add(new_trip)
        db.commit()
        db.refresh(new_trip)

        # 1. Add Itinerary Items matching the user's selected days
        order = 1
        catalog_highlights = circuit["itinerary_highlights"]
        max_catalog_day = max((h[0] for h in catalog_highlights), default=1)
        for d_num in range(1, trip_days + 1):
            source_day = ((d_num - 1) % max_catalog_day) + 1
            day_acts = [h for h in catalog_highlights if h[0] == source_day]
            for _, slot, act_title, loc, lat, lon, cost, cat, desc in day_acts:
                prefix = f"Day {d_num}: " if d_num > max_catalog_day else ""
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=d_num,
                    time_slot=slot,
                    title=f"{prefix}{act_title}",
                    description=desc,
                    location=loc,
                    latitude=lat,
                    longitude=lon,
                    estimated_cost=cost,
                    category=cat,
                    is_completed=False,
                    order_index=order
                ))
                order += 1

        # 2. Add Transport Options
        cost_multiplier = max(1, req.num_travelers)
        for mode, trans_title, route, cost, tips in circuit["transports"]:
            adjusted_cost = cost * (1.0 if mode == "Cab/Taxi" else cost_multiplier)
            db.add(TransportOption(
                trip_id=new_trip.id,
                mode=mode,
                title=trans_title,
                route=route,
                estimated_cost=round(adjusted_cost, 2),
                currency="INR",
                booking_tips=tips,
                is_booked=False
            ))

        # 3. Add Initial Booked Deposits as Expenses
        bk = budget_calc["breakdown"]
        initial_exp = [
            (f"Advance Hotel / Resort Deposit ({tier_label})", round(bk["stay"] * 0.4, 2), "Accommodation", s_date.isoformat(), "Room reservation advance"),
            ("Confirmed Train / Transit Tickets", round(bk["transport"] * 0.5, 2), "Transport", s_date.isoformat(), "IRCTC / Flight advance"),
            ("Sightseeing / Darshan / Activity Passes", round(bk.get("activities_entry", bk.get("darshan_pooja", 0.0)), 2), "Activities", s_date.isoformat(), "Official entry / permit booking")
        ]
        for exp_title, exp_amt, exp_cat, exp_dt, exp_notes in initial_exp:
            db.add(Expense(
                trip_id=new_trip.id,
                title=exp_title,
                amount=exp_amt,
                currency="INR",
                category=exp_cat,
                date=exp_dt,
                notes=exp_notes
            ))

        # 4. Add Packing Items
        standard_packing = [
            ("Clothing", "Comfortable cotton & modest attire suited for local culture", True),
            ("Clothing", "Comfortable walking shoes & slip-on footwear", True),
            ("Health", "Personal medical pouch (ORS, pain relief, motion sickness tablets)", True),
            ("Documents", "Original Govt Photo ID / Aadhaar Card", True),
            ("Gear", "Phone charger & power bank", True)
        ]
        for cat, item_name, is_sugg in standard_packing:
            db.add(PackingItem(
                trip_id=new_trip.id,
                category=cat,
                item_name=item_name,
                is_packed=False,
                is_suggested=is_sugg
            ))

        for item_name in circuit.get("packing_extras", []):
            db.add(PackingItem(
                trip_id=new_trip.id,
                category="Gear",
                item_name=item_name,
                is_packed=False,
                is_suggested=True
            ))

    else:
        # Custom Arbitrary Indian Destination
        dest_title = (req.destination or "Custom Destination").strip()
        trip_days = max(1, req.days or 4)
        e_date = s_date + timedelta(days=trip_days - 1)

        budget_calc = calculate_universal_destination_budget(
            destination=dest_title,
            days=trip_days,
            travel_tier=req.travel_tier,
            num_travelers=req.num_travelers,
            travel_style=req.travel_style,
            departure_date=req.start_date
        )

        pace = "Relaxed" if trip_days >= 6 else ("Moderate" if trip_days >= 4 else "Fast-Paced")

        new_trip = Trip(
            title=f"{trip_days}-Day Exploration of {dest_title} ({tier_label})",
            destination=dest_title,
            country="India",
            latitude=20.5937,
            longitude=78.9629,
            start_date=s_date.isoformat(),
            end_date=e_date.isoformat(),
            travel_style=req.travel_style or "Leisure & Sightseeing",
            travel_pace=pace,
            total_budget=budget_calc["total_budget"],
            currency="INR",
            cover_image=get_indian_destination_image(dest_title),
            notes=f"Custom planned journey to {dest_title} for {req.num_travelers} traveler(s) at {tier_label} tier. Departure scheduled for {req.departure_time}."
        )
        db.add(new_trip)
        db.commit()
        db.refresh(new_trip)

        # 1. Generate Days of Itinerary
        for day in range(1, trip_days + 1):
            if day == 1:
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=1,
                    time_slot="Morning",
                    title=f"Arrival in {dest_title} & Hotel Check-in",
                    description=f"Arrive via scheduled transit, check in to your {tier_label} accommodation, and refresh.",
                    location=f"{dest_title} Center",
                    latitude=20.5937,
                    longitude=78.9629,
                    estimated_cost=400.0,
                    category="Lodging",
                    is_completed=False,
                    order_index=1
                ))
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=1,
                    time_slot="Evening",
                    title=f"Orientation Walk & Local Market Exploration",
                    description=f"Stroll through local street bazaars and sample popular regional delicacies in {dest_title}.",
                    location=f"{dest_title} Market",
                    latitude=20.5937,
                    longitude=78.9629,
                    estimated_cost=350.0,
                    category="Food",
                    is_completed=False,
                    order_index=2
                ))
            elif day == trip_days:
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=day,
                    time_slot="Morning",
                    title=f"Farewell Breakfast, Souvenir Shopping & Departure",
                    description=f"Enjoy breakfast, collect local specialties and souvenirs, and board return transit.",
                    location=f"{dest_title} Station / Airport",
                    latitude=20.5937,
                    longitude=78.9629,
                    estimated_cost=300.0,
                    category="Shopping",
                    is_completed=False,
                    order_index=day * 2
                ))
            else:
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=day,
                    time_slot="Morning",
                    title=f"Top Attractions & Iconic Sightseeing (Day {day})",
                    description=f"Full morning exploring major heritage landmarks, nature viewpoints, and temples in {dest_title}.",
                    location=f"{dest_title} Highlights",
                    latitude=20.5937,
                    longitude=78.9629,
                    estimated_cost=600.0,
                    category="Attraction",
                    is_completed=False,
                    order_index=day * 2 - 1
                ))
                db.add(ItineraryItem(
                    trip_id=new_trip.id,
                    day_number=day,
                    time_slot="Evening",
                    title=f"Scenic Sunset Point & Regional Dinner Experience",
                    description=f"Sunset photography viewpoint followed by an authentic dinner at a top-rated dining spot.",
                    location=f"{dest_title} Viewpoint",
                    latitude=20.5937,
                    longitude=78.9629,
                    estimated_cost=500.0,
                    category="Leisure",
                    is_completed=False,
                    order_index=day * 2
                ))

        # 2. Add Transport Options
        bk = budget_calc["breakdown"]
        db.add(TransportOption(
            trip_id=new_trip.id,
            mode="Train / Flight",
            title=f"Intercity Express Train / Flight to {dest_title}",
            route=f"Origin City ⇄ {dest_title}",
            estimated_cost=round(bk["transport"] * 0.6, 2),
            currency="INR",
            booking_tips="Book in advance via IRCTC or airline portal for best fare rates.",
            is_booked=False
        ))
        db.add(TransportOption(
            trip_id=new_trip.id,
            mode="Cab/Taxi",
            title=f"Dedicated AC Sightseeing Cab & Station Transfers",
            route=f"Local {dest_title} Circuit",
            estimated_cost=round(bk["transport"] * 0.4, 2),
            currency="INR",
            booking_tips="Hire pre-paid or app-based cab for hassle-free daily sightseeing.",
            is_booked=False
        ))

        # 3. Add Initial Expenses
        db.add(Expense(
            trip_id=new_trip.id,
            title=f"Hotel / Stay Advance ({tier_label})",
            amount=round(bk["stay"] * 0.5, 2),
            currency="INR",
            category="Accommodation",
            date=s_date.isoformat(),
            notes="Booking deposit for accommodation"
        ))
        db.add(Expense(
            trip_id=new_trip.id,
            title=f"Transit Reservation Tickets",
            amount=round(bk["transport"] * 0.5, 2),
            currency="INR",
            category="Transport",
            date=s_date.isoformat(),
            notes="Advance tickets"
        ))

        # 4. Standard Packing
        packing_items = [
            ("Clothing", "Comfortable cotton clothes & light jacket", True),
            ("Clothing", "Walking shoes / sneakers", True),
            ("Health", "Personal medical kit & sanitizer", True),
            ("Documents", "Aadhaar Card / Govt ID", True),
            ("Gear", "Power bank, umbrella, and camera", True)
        ]
        for cat, item_name, is_sugg in packing_items:
            db.add(PackingItem(
                trip_id=new_trip.id,
                category=cat,
                item_name=item_name,
                is_packed=False,
                is_suggested=is_sugg
            ))

    db.commit()
    db.refresh(new_trip)
    return get_trip_details(new_trip.id, db)

