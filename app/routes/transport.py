"""Transport and commute options router."""
from typing import List
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Trip, TransportOption, Expense
from app.schemas import TransportOptionCreate, TransportOptionResponse, ExpenseResponse

router = APIRouter(tags=["Transport"])


@router.get("/api/trips/{trip_id}/transport", response_model=List[TransportOptionResponse])
def get_trip_transport_options(trip_id: int, db: Session = Depends(get_db)):
    """Retrieve all transport options for a trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    return [TransportOptionResponse.from_orm(t) for t in trip.transport_options]


@router.post("/api/trips/{trip_id}/transport", response_model=TransportOptionResponse, status_code=status.HTTP_201_CREATED)
def add_transport_option(trip_id: int, trans_in: TransportOptionCreate, db: Session = Depends(get_db)):
    """Add a transport or commute option to a trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    new_opt = TransportOption(
        trip_id=trip_id,
        mode=trans_in.mode,
        title=trans_in.title,
        route=trans_in.route or "",
        estimated_cost=trans_in.estimated_cost,
        currency=trans_in.currency or trip.currency,
        booking_tips=trans_in.booking_tips or "",
        is_booked=trans_in.is_booked
    )
    db.add(new_opt)
    db.commit()
    db.refresh(new_opt)
    return new_opt


@router.patch("/api/transport/{transport_id}/toggle", response_model=TransportOptionResponse)
def toggle_transport_booked(transport_id: int, db: Session = Depends(get_db)):
    """Toggle booked / confirmed status of a transport option."""
    opt = db.query(TransportOption).filter(TransportOption.id == transport_id).first()
    if not opt:
        raise HTTPException(status_code=404, detail="Transport option not found")

    opt.is_booked = not opt.is_booked
    db.commit()
    db.refresh(opt)
    return opt


@router.post("/api/transport/{transport_id}/to-expense", response_model=ExpenseResponse)
def convert_transport_to_expense(transport_id: int, db: Session = Depends(get_db)):
    """Convenience endpoint to convert an estimated transport item into an actual logged expense."""
    opt = db.query(TransportOption).filter(TransportOption.id == transport_id).first()
    if not opt:
        raise HTTPException(status_code=404, detail="Transport option not found")

    new_exp = Expense(
        trip_id=opt.trip_id,
        title=f"{opt.mode}: {opt.title}",
        amount=opt.estimated_cost,
        currency=opt.currency,
        category="Transport",
        date=date.today().isoformat(),
        notes=f"Auto-logged from transport section. Route: {opt.route}"
    )
    opt.is_booked = True
    db.add(new_exp)
    db.commit()
    db.refresh(new_exp)
    return new_exp


@router.delete("/api/transport/{transport_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transport_option(transport_id: int, db: Session = Depends(get_db)):
    """Delete a transport option."""
    opt = db.query(TransportOption).filter(TransportOption.id == transport_id).first()
    if not opt:
        raise HTTPException(status_code=404, detail="Transport option not found")

    db.delete(opt)
    db.commit()
    return None
