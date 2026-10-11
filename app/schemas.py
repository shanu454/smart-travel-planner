"""Pydantic schemas for request and response validation."""
from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


# -------------------------------------------------------------------------
# Itinerary Schemas
# -------------------------------------------------------------------------
class ItineraryItemBase(BaseModel):
    day_number: int = Field(..., ge=1, description="Day number of the trip")
    time_slot: str = Field(default="Morning", description="Morning, Afternoon, or Evening")
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = ""
    location: Optional[str] = ""
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    estimated_cost: float = Field(default=0.0, ge=0.0)
    category: str = Field(default="Attraction")
    is_completed: bool = False
    order_index: int = 0


class ItineraryItemCreate(ItineraryItemBase):
    pass


class ItineraryItemUpdate(BaseModel):
    day_number: Optional[int] = None
    time_slot: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    estimated_cost: Optional[float] = None
    category: Optional[str] = None
    is_completed: Optional[bool] = None
    order_index: Optional[int] = None


class ItineraryItemResponse(ItineraryItemBase):
    id: int
    trip_id: int

    class Config:
        from_attributes = True


# -------------------------------------------------------------------------
# Expense Schemas
# -------------------------------------------------------------------------
class ExpenseBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    amount: float = Field(..., gt=0)
    currency: str = Field(default="USD")
    category: str = Field(default="Food & Dining")
    date: str = Field(..., description="Format: YYYY-MM-DD")
    notes: Optional[str] = ""


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    id: int
    trip_id: int

    class Config:
        from_attributes = True


class BudgetSummaryResponse(BaseModel):
    total_budget: float
    total_spent: float
    remaining_budget: float
    percent_used: float
    currency: str
    by_category: Dict[str, float]
    recent_expenses: List[ExpenseResponse]


# -------------------------------------------------------------------------
# Packing Item Schemas
# -------------------------------------------------------------------------
class PackingItemBase(BaseModel):
    category: str = Field(default="Essentials")
    item_name: str = Field(..., min_length=1, max_length=200)
    is_packed: bool = False
    is_suggested: bool = True


class PackingItemCreate(PackingItemBase):
    pass


class PackingItemUpdate(BaseModel):
    category: Optional[str] = None
    item_name: Optional[str] = None
    is_packed: Optional[bool] = None


class PackingItemResponse(PackingItemBase):
    id: int
    trip_id: int

    class Config:
        from_attributes = True


class PackingSummaryResponse(BaseModel):
    total_items: int
    packed_items: int
    percent_packed: float
    by_category: Dict[str, List[PackingItemResponse]]


# -------------------------------------------------------------------------
# Trip Schemas
# -------------------------------------------------------------------------
class TripBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    destination: str = Field(..., min_length=1, max_length=200)
    country: str = Field(default="India")
    latitude: float = Field(default=0.0)
    longitude: float = Field(default=0.0)
    start_date: str = Field(..., description="Format: YYYY-MM-DD")
    end_date: str = Field(..., description="Format: YYYY-MM-DD")
    travel_style: str = Field(default="Cultural & Heritage")
    travel_pace: str = Field(default="Moderate", description="Relaxed, Moderate, Fast-Paced")
    total_budget: float = Field(default=25000.0, ge=0.0)
    currency: str = Field(default="INR")
    cover_image: Optional[str] = ""
    notes: Optional[str] = ""


class TripCreate(TripBase):
    pass


class TripUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    travel_style: Optional[str] = None
    travel_pace: Optional[str] = None
    total_budget: Optional[float] = None
    currency: Optional[str] = None
    cover_image: Optional[str] = None
    notes: Optional[str] = None


class PaceUpdateRequest(BaseModel):
    travel_pace: str = Field(..., description="Relaxed, Moderate, Fast-Paced")


class TripResponse(TripBase):
    id: int
    created_at: Optional[datetime] = None
    total_spent: Optional[float] = 0.0
    days_count: Optional[int] = 1
    is_completed: bool = False
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# -------------------------------------------------------------------------
# Transport Schemas
# -------------------------------------------------------------------------
class TransportOptionBase(BaseModel):
    mode: str = Field(default="Train", description="Train, Flight, Cab/Taxi, Auto-Rickshaw, Scooter, Bus, Ferry, Metro")
    title: str = Field(..., min_length=1, max_length=200)
    route: Optional[str] = ""
    estimated_cost: float = Field(default=0.0, ge=0.0)
    currency: str = Field(default="INR")
    booking_tips: Optional[str] = ""
    is_booked: bool = False


class TransportOptionCreate(TransportOptionBase):
    pass


class TransportOptionResponse(TransportOptionBase):
    id: int
    trip_id: int

    class Config:
        from_attributes = True


# -------------------------------------------------------------------------
# Trip Completion & Feedback Schemas
# -------------------------------------------------------------------------
class TripFeedbackBase(BaseModel):
    rating_overall: int = Field(default=5, ge=1, le=5, description="1 to 5 stars")
    rating_transit: int = Field(default=5, ge=1, le=5)
    rating_stays: int = Field(default=5, ge=1, le=5)
    rating_activities: int = Field(default=5, ge=1, le=5)
    rating_budget: int = Field(default=5, ge=1, le=5)
    recommend: str = Field(default="Highly Recommend", description="Highly Recommend, Good, Needs Improvement")
    best_highlights: Optional[str] = ""
    comments: Optional[str] = ""
    tips_for_others: Optional[str] = ""
    traveler_name: Optional[str] = "Traveler"


class TripFeedbackCreate(TripFeedbackBase):
    pass


class TripFeedbackResponse(TripFeedbackBase):
    id: int
    trip_id: int
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TripDetailResponse(TripResponse):
    itinerary_items: List[ItineraryItemResponse] = []
    expenses: List[ExpenseResponse] = []
    packing_items: List[PackingItemResponse] = []
    transport_options: List[TransportOptionResponse] = []
    budget_summary: Optional[BudgetSummaryResponse] = None
    packing_summary: Optional[PackingSummaryResponse] = None
    feedback: Optional[TripFeedbackResponse] = None


# -------------------------------------------------------------------------
# Smart Generator & API Schemas
# -------------------------------------------------------------------------
class TripGenerateRequest(BaseModel):
    destination: str = Field(..., min_length=1)
    country: Optional[str] = "India"
    start_date: str = Field(..., description="YYYY-MM-DD")
    end_date: str = Field(..., description="YYYY-MM-DD")
    travel_style: str = Field(default="Cultural & Heritage")
    travel_pace: str = Field(default="Moderate", description="Relaxed, Moderate, Fast-Paced")
    total_budget: float = Field(default=25000.0, ge=0.0)
    currency: str = Field(default="INR")
    interests: List[str] = Field(default_factory=list)


class PlaceSearchResult(BaseModel):
    name: str
    country: str
    admin1: Optional[str] = ""
    latitude: float
    longitude: float
    timezone: Optional[str] = ""
    country_code: Optional[str] = ""


class WeatherDay(BaseModel):
    date: str
    weather_code: int
    weather_label: str
    weather_icon: str
    temp_max: float
    temp_min: float
    precip_prob: Optional[int] = 0
    uv_index: Optional[float] = 0.0


class WeatherForecastResponse(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    current_temp: Optional[float] = None
    daily: List[WeatherDay]
    packing_alert: Optional[str] = None


class CurrencyRatesResponse(BaseModel):
    base: str
    rates: Dict[str, float]
    updated_at: Optional[str] = None
