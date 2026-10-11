"""Expenses and budget tracking router."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Trip, Expense
from app.schemas import ExpenseCreate, ExpenseResponse, BudgetSummaryResponse

router = APIRouter(tags=["Expenses"])


@router.post("/api/trips/{trip_id}/expenses", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def add_expense(trip_id: int, expense_in: ExpenseCreate, db: Session = Depends(get_db)):
    """Log an actual travel expense."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    new_expense = Expense(
        trip_id=trip_id,
        title=expense_in.title,
        amount=expense_in.amount,
        currency=expense_in.currency or trip.currency,
        category=expense_in.category,
        date=expense_in.date,
        notes=expense_in.notes or ""
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.get("/api/trips/{trip_id}/budget", response_model=BudgetSummaryResponse)
def get_trip_budget(trip_id: int, db: Session = Depends(get_db)):
    """Get calculated budget breakdown, category totals, and recent expenses."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    expenses = db.query(Expense).filter(Expense.trip_id == trip_id).order_by(Expense.date.desc()).all()
    total_spent = sum(e.amount for e in expenses)
    remaining = max(0.0, trip.total_budget - total_spent)
    pct = round((total_spent / trip.total_budget * 100.0), 1) if trip.total_budget > 0 else 0.0

    by_cat: dict = {}
    for e in expenses:
        by_cat[e.category] = round(by_cat.get(e.category, 0.0) + e.amount, 2)

    return BudgetSummaryResponse(
        total_budget=trip.total_budget,
        total_spent=round(total_spent, 2),
        remaining_budget=round(remaining, 2),
        percent_used=pct,
        currency=trip.currency,
        by_category=by_cat,
        recent_expenses=[ExpenseResponse.from_orm(e) for e in expenses]
    )


@router.delete("/api/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    """Delete an expense record."""
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return None
