"""Packing checklist router."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Trip, PackingItem
from app.schemas import PackingItemCreate, PackingItemResponse, PackingSummaryResponse
from app.services.weather import get_weather_forecast
from app.services.planner import generate_smart_packing_list
from app.routes.trips import calculate_days

router = APIRouter(tags=["Packing"])


@router.get("/api/trips/{trip_id}/packing", response_model=PackingSummaryResponse)
def get_packing_list(trip_id: int, db: Session = Depends(get_db)):
    """Retrieve full categorized packing list with progress metrics."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    items = db.query(PackingItem).filter(PackingItem.trip_id == trip_id).all()
    packed_count = sum(1 for p in items if p.is_packed)
    total = len(items)
    pct = round((packed_count / total * 100.0), 1) if total > 0 else 0.0

    by_cat: dict = {}
    for p in items:
        by_cat.setdefault(p.category, []).append(PackingItemResponse.from_orm(p))

    return PackingSummaryResponse(
        total_items=total,
        packed_items=packed_count,
        percent_packed=pct,
        by_category=by_cat
    )


@router.post("/api/trips/{trip_id}/packing", response_model=PackingItemResponse, status_code=status.HTTP_201_CREATED)
def add_packing_item(trip_id: int, item_in: PackingItemCreate, db: Session = Depends(get_db)):
    """Add a custom item to the trip packing checklist."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    new_item = PackingItem(
        trip_id=trip_id,
        category=item_in.category,
        item_name=item_in.item_name,
        is_packed=item_in.is_packed,
        is_suggested=False
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.patch("/api/packing/{item_id}/toggle", response_model=PackingItemResponse)
def toggle_packing_item(item_id: int, db: Session = Depends(get_db)):
    """Check or uncheck an item on the packing checklist."""
    item = db.query(PackingItem).filter(PackingItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Packing item not found")

    item.is_packed = not item.is_packed
    db.commit()
    db.refresh(item)
    return item


@router.delete("/api/packing/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_packing_item(item_id: int, db: Session = Depends(get_db)):
    """Remove an item from the packing checklist."""
    item = db.query(PackingItem).filter(PackingItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Packing item not found")

    db.delete(item)
    db.commit()
    return None


@router.post("/api/trips/{trip_id}/packing/regenerate", response_model=PackingSummaryResponse)
async def regenerate_packing_checklist(trip_id: int, db: Session = Depends(get_db)):
    """Regenerate climate-adapted packing suggestions for this trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Fetch fresh weather forecast
    weather = None
    if trip.latitude != 0.0 or trip.longitude != 0.0:
        weather = await get_weather_forecast(trip.latitude, trip.longitude)

    days_count = calculate_days(trip.start_date, trip.end_date)
    new_suggestions = generate_smart_packing_list(
        destination=trip.destination,
        days_count=days_count,
        weather_forecast=weather,
        travel_style=trip.travel_style
    )

    # Remove existing AI/suggested items (keep custom user items)
    db.query(PackingItem).filter(PackingItem.trip_id == trip_id, PackingItem.is_suggested == True).delete()

    for item in new_suggestions:
        db.add(PackingItem(
            trip_id=trip_id,
            category=item["category"],
            item_name=item["item_name"],
            is_packed=False,
            is_suggested=True
        ))
    db.commit()
    return get_packing_list(trip_id, db)
