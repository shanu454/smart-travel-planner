"""API Router for Hotels, Airbnbs, and Hostels Stays & Bookings."""
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.stays import (
    STAYS_CATALOG,
    get_all_stays,
    get_stay_by_id,
    book_stay_instant,
    add_stay_to_trip_booking
)

router = APIRouter(prefix="/api/stays", tags=["Hotels, Airbnb & Hostels"])


class BookStayRequest(BaseModel):
    guest_name: Optional[str] = "Valued Traveler"
    guest_email: Optional[str] = "traveler@example.com"
    check_in: str = Field(..., description="Check-in date (YYYY-MM-DD)")
    check_out: str = Field(..., description="Check-out date (YYYY-MM-DD)")
    guests_count: Optional[int] = 1
    rooms_count: Optional[int] = 1


class AddStayToTripRequest(BaseModel):
    trip_id: int
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    guests_count: Optional[int] = 1


@router.get("")
def list_stays(
    q: Optional[str] = Query(None, description="Search query by city, destination, name, or amenities"),
    type: Optional[str] = Query(None, description="Filter by lodging type: hotel, airbnb, hostel, or all"),
    min_price: Optional[float] = Query(None, description="Minimum price per night in INR"),
    max_price: Optional[float] = Query(None, description="Maximum price per night in INR"),
    amenity: Optional[str] = Query(None, description="Filter by amenity tag"),
    sort_by: Optional[str] = Query(None, description="Sort order: rating, price_asc, price_desc, reviews")
):
    """Retrieve catalog of hotels, airbnbs, and hostels with real-time filters."""
    return get_all_stays(
        query=q,
        lodging_type=type,
        min_price=min_price,
        max_price=max_price,
        amenity=amenity,
        sort_by=sort_by
    )


@router.get("/popular-destinations")
def get_popular_stay_destinations():
    """Return top popular stay locations for quick chips."""
    return [
        {"name": "Goa", "label": "🏖️ Goa", "count": 3},
        {"name": "Jaipur", "label": "🏰 Jaipur", "count": 3},
        {"name": "Rishikesh", "label": "🧘 Rishikesh", "count": 2},
        {"name": "Manali", "label": "🏔️ Manali", "count": 3},
        {"name": "Udaipur", "label": "✨ Udaipur", "count": 1},
        {"name": "Kedarnath", "label": "🕉️ Kedarnath", "count": 1},
        {"name": "Ayodhya", "label": "🛕 Ayodhya", "count": 1},
        {"name": "Tokyo", "label": "🗾 Tokyo", "count": 2},
        {"name": "Paris", "label": "🗼 Paris", "count": 2},
        {"name": "Bali", "label": "🌴 Bali", "count": 1}
    ]


@router.get("/{stay_id}")
def get_stay_details(stay_id: str):
    """Retrieve complete metadata, amenities, and house rules for a single stay."""
    stay = get_stay_by_id(stay_id)
    if not stay:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lodging stay not found")
    return stay


@router.post("/{stay_id}/book")
def instant_reserve_stay(stay_id: str, req: BookStayRequest):
    """Generate instant simulated booking voucher with reservation code and invoice breakdown."""
    try:
        voucher = book_stay_instant(
            stay_id=stay_id,
            guest_name=req.guest_name,
            guest_email=req.guest_email,
            check_in=req.check_in,
            check_out=req.check_out,
            guests_count=req.guests_count or 1,
            rooms_count=req.rooms_count or 1
        )
        return voucher
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{stay_id}/add-to-trip")
def attach_stay_to_trip(stay_id: str, req: AddStayToTripRequest, db: Session = Depends(get_db)):
    """Add accommodation booking as an Expense and lodging record to the user's active trip."""
    try:
        res = add_stay_to_trip_booking(
            db=db,
            trip_id=req.trip_id,
            stay_id=stay_id,
            check_in=req.check_in,
            check_out=req.check_out,
            guests_count=req.guests_count or 1
        )
        return res
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
