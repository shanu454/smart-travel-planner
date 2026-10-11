"""Itinerary activities router."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Trip, ItineraryItem
from app.schemas import ItineraryItemCreate, ItineraryItemUpdate, ItineraryItemResponse

router = APIRouter(tags=["Itinerary"])


@router.post("/api/trips/{trip_id}/itinerary", response_model=ItineraryItemResponse, status_code=status.HTTP_201_CREATED)
def add_itinerary_item(trip_id: int, item_in: ItineraryItemCreate, db: Session = Depends(get_db)):
    """Add a new scheduled activity to a trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    new_item = ItineraryItem(
        trip_id=trip_id,
        day_number=item_in.day_number,
        time_slot=item_in.time_slot,
        title=item_in.title,
        description=item_in.description or "",
        location=item_in.location or "",
        latitude=item_in.latitude or trip.latitude,
        longitude=item_in.longitude or trip.longitude,
        estimated_cost=item_in.estimated_cost,
        category=item_in.category,
        is_completed=item_in.is_completed,
        order_index=item_in.order_index
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.put("/api/itinerary/{item_id}", response_model=ItineraryItemResponse)
def update_itinerary_item(item_id: int, item_in: ItineraryItemUpdate, db: Session = Depends(get_db)):
    """Update details of an itinerary activity."""
    item = db.query(ItineraryItem).filter(ItineraryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Itinerary item not found")

    update_dict = item_in.dict(exclude_unset=True)
    for k, v in update_dict.items():
        setattr(item, k, v)

    db.commit()
    db.refresh(item)
    return item


@router.patch("/api/itinerary/{item_id}/toggle", response_model=ItineraryItemResponse)
def toggle_itinerary_item(item_id: int, db: Session = Depends(get_db)):
    """Toggle completion status of an activity."""
    item = db.query(ItineraryItem).filter(ItineraryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Itinerary item not found")

    item.is_completed = not item.is_completed
    db.commit()
    db.refresh(item)
    return item


@router.delete("/api/itinerary/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_itinerary_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an activity from the itinerary."""
    item = db.query(ItineraryItem).filter(ItineraryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Itinerary item not found")

    db.delete(item)
    db.commit()
    return None
