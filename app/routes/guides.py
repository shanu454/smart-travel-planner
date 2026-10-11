"""API Router for Local Travel Guides & Direct Guide Connection."""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, Query, status

from app.services.guides import (
    get_all_guides,
    get_guide_by_id,
    get_guides_for_destination,
    create_guide_inquiry,
    generate_guide_chat_reply
)

router = APIRouter(prefix="/api/guides", tags=["Local Travel Guides"])


class GuideInquiryRequest(BaseModel):
    client_name: Optional[str] = "Valued Traveler"
    client_email: Optional[str] = "traveler@example.com"
    client_phone: Optional[str] = ""
    tour_date: str = Field(..., description="Planned tour date (YYYY-MM-DD)")
    group_size: Optional[int] = Field(1, ge=1, le=50)
    duration_type: Optional[str] = Field("full_day", description="full_day, half_day, or custom")
    special_notes: Optional[str] = ""


class GuideChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Customer's message to the guide")
    traveler_name: Optional[str] = "Traveler"


@router.api_route("", methods=["GET", "HEAD"])
def list_guides(
    q: Optional[str] = Query(None, description="Search query by name, destination, language, or specialty"),
    destination: Optional[str] = Query(None, description="Filter by destination city/region"),
    region: Optional[str] = Query(None, description="Filter by category (Spiritual, Cultural, Adventure, etc.)"),
    language: Optional[str] = Query(None, description="Filter by spoken language"),
    specialty: Optional[str] = Query(None, description="Filter by guide specialty"),
    sort_by: Optional[str] = Query("rating", description="Sort order: rating, price_asc, price_desc, experience, reviews")
):
    """Retrieve verified local guides catalog with real-time search and filters."""
    return get_all_guides(
        query=q,
        destination=destination,
        region=region,
        language=language,
        specialty=specialty,
        sort_by=sort_by
    )


@router.api_route("/destination/{destination}", methods=["GET", "HEAD"])
def get_destination_guides(destination: str, limit: Optional[int] = 4):
    """Retrieve top certified guides recommended for a specific destination (e.g. for active trips)."""
    return get_guides_for_destination(destination, limit=limit)


@router.api_route("/{guide_id}", methods=["GET", "HEAD"])
def get_guide_profile(guide_id: str):
    """Retrieve full profile, accreditation, and sample tours for a single guide."""
    guide = get_guide_by_id(guide_id)
    if not guide:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Local guide not found")
    return guide


@router.post("/{guide_id}/inquire")
def submit_guide_inquiry(guide_id: str, req: GuideInquiryRequest):
    """Submit a direct booking inquiry to a local guide and generate a verified confirmation voucher."""
    try:
        voucher = create_guide_inquiry(
            guide_id=guide_id,
            inquiry_data={
                "client_name": req.client_name,
                "client_email": req.client_email,
                "client_phone": req.client_phone,
                "tour_date": req.tour_date,
                "group_size": req.group_size or 1,
                "duration_type": req.duration_type or "full_day",
                "special_notes": req.special_notes or ""
            }
        )
        return voucher
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{guide_id}/chat")
def chat_with_guide(guide_id: str, req: GuideChatRequest):
    """Send an interactive chat message to the guide and receive an instant contextual reply."""
    try:
        reply = generate_guide_chat_reply(
            guide_id=guide_id,
            message=req.message,
            traveler_name=req.traveler_name or "Traveler"
        )
        return reply
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
