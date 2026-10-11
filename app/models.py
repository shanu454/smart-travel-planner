"""SQLAlchemy ORM models for Smart Travel Planner."""
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from app.database import Base


class Trip(Base):
    """Trip model representing an overall travel journey."""
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False, index=True)
    country = Column(String(100), nullable=False, default="")
    latitude = Column(Float, nullable=False, default=0.0)
    longitude = Column(Float, nullable=False, default=0.0)
    start_date = Column(String(20), nullable=False)  # Format: YYYY-MM-DD
    end_date = Column(String(20), nullable=False)    # Format: YYYY-MM-DD
    travel_style = Column(String(50), nullable=False, default="Cultural & Heritage")
    travel_pace = Column(String(50), nullable=False, default="Moderate")  # Relaxed, Moderate, Fast-Paced
    total_budget = Column(Float, nullable=False, default=25000.0)
    currency = Column(String(10), nullable=False, default="INR")
    cover_image = Column(String(500), nullable=True, default="")
    notes = Column(Text, nullable=True, default="")
    is_completed = Column(Boolean, nullable=False, default=False)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    itinerary_items = relationship(
        "ItineraryItem",
        back_populates="trip",
        cascade="all, delete-orphan",
        order_by="ItineraryItem.day_number, ItineraryItem.order_index"
    )
    expenses = relationship(
        "Expense",
        back_populates="trip",
        cascade="all, delete-orphan",
        order_by="Expense.date.desc()"
    )
    packing_items = relationship(
        "PackingItem",
        back_populates="trip",
        cascade="all, delete-orphan"
    )
    transport_options = relationship(
        "TransportOption",
        back_populates="trip",
        cascade="all, delete-orphan",
        order_by="TransportOption.id"
    )
    feedback = relationship(
        "TripFeedback",
        back_populates="trip",
        uselist=False,
        cascade="all, delete-orphan"
    )


class ItineraryItem(Base):
    """Activity / Schedule item belonging to a specific day of a trip."""
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    day_number = Column(Integer, nullable=False, default=1)
    time_slot = Column(String(20), nullable=False, default="Morning")  # Morning, Afternoon, Evening
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True, default="")
    location = Column(String(200), nullable=True, default="")
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    estimated_cost = Column(Float, nullable=False, default=0.0)
    category = Column(String(50), nullable=False, default="Attraction")  # Attraction, Food, Transport, Leisure, Lodging
    is_completed = Column(Boolean, nullable=False, default=False)
    order_index = Column(Integer, nullable=False, default=0)

    trip = relationship("Trip", back_populates="itinerary_items")


class Expense(Base):
    """Actual logged expense for a trip."""
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(10), nullable=False, default="USD")
    category = Column(String(50), nullable=False, default="Food & Dining")  # Food & Dining, Accommodation, Transport, Activities, Shopping, Other
    date = Column(String(20), nullable=False)  # Format: YYYY-MM-DD
    notes = Column(Text, nullable=True, default="")

    trip = relationship("Trip", back_populates="expenses")


class PackingItem(Base):
    """Packing checklist item for a trip."""
    __tablename__ = "packing_items"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(50), nullable=False, default="Essentials")  # Clothing, Documents, Toiletries, Electronics, Health, Gear
    item_name = Column(String(200), nullable=False)
    is_packed = Column(Boolean, nullable=False, default=False)
    is_suggested = Column(Boolean, nullable=False, default=True)

    trip = relationship("Trip", back_populates="packing_items")


class TransportOption(Base):
    """Transport and commute option with estimated cost for a trip."""
    __tablename__ = "transport_options"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False)
    mode = Column(String(50), nullable=False, default="Train")  # Train, Flight, Cab/Taxi, Auto-Rickshaw, Scooter, Bus, Ferry, Metro
    title = Column(String(200), nullable=False)
    route = Column(String(200), nullable=False, default="")
    estimated_cost = Column(Float, nullable=False, default=0.0)
    currency = Column(String(10), nullable=False, default="INR")
    booking_tips = Column(Text, nullable=True, default="")
    is_booked = Column(Boolean, nullable=False, default=False)

    trip = relationship("Trip", back_populates="transport_options")


class User(Base):
    """Registered Traveler / User model."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(150), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    salt = Column(String(64), nullable=False)
    avatar_url = Column(String(500), nullable=True, default="")
    phone = Column(String(50), nullable=True, default="")
    preferred_currency = Column(String(10), nullable=False, default="INR")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    sessions = relationship("UserSession", back_populates="user", cascade="all, delete-orphan")


class UserSession(Base):
    """User authentication session tokens."""
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    token = Column(String(128), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="sessions")


class TripFeedback(Base):
    """Traveler feedback and rating after completing a trip."""
    __tablename__ = "trip_feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id", ondelete="CASCADE"), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    rating_overall = Column(Integer, nullable=False, default=5)  # 1 to 5 stars
    rating_transit = Column(Integer, nullable=False, default=5)
    rating_stays = Column(Integer, nullable=False, default=5)
    rating_activities = Column(Integer, nullable=False, default=5)
    rating_budget = Column(Integer, nullable=False, default=5)
    recommend = Column(String(50), nullable=False, default="Highly Recommend")
    best_highlights = Column(String(300), nullable=True, default="")
    comments = Column(Text, nullable=True, default="")
    tips_for_others = Column(Text, nullable=True, default="")
    traveler_name = Column(String(150), nullable=False, default="Traveler")
    created_at = Column(DateTime, default=datetime.utcnow)

    trip = relationship("Trip", back_populates="feedback")

