"""API Router for World Destination Guides & Global Tour Exploration."""
from typing import List, Optional
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.routes.trips import get_trip_details
from app.schemas import TripDetailResponse
from app.services.world_guides import (
    WORLD_GUIDES,
    get_all_world_guides,
    get_world_guide_by_id,
    clone_world_guide_to_trip
)

router = APIRouter(prefix="/api/world-guides", tags=["World Destination Guides"])


class CloneGuideRequest(BaseModel):
    start_date: Optional[str] = None


@router.get("")
def list_world_guides(
    q: Optional[str] = Query(None, description="Search query by city, country, title, or tag"),
    tag: Optional[str] = Query(None, description="Filter by destination tag or country")
):
    """List curated global travel guides with optional search and tag filters."""
    return get_all_world_guides(query=q, tag=tag)


@router.get("/popular-tags")
def get_popular_tags():
    """Return top popular world destination tags for quick navigation chips."""
    from collections import Counter
    tag_counts = Counter()
    for g in WORLD_GUIDES.values():
        for t in g.get("tags", []):
            tag_counts[t] += 1
        # Also ensure country is represented
        if g.get("country"):
            tag_counts[g["country"]] += 1
        if g.get("region"):
            tag_counts[g["region"]] += 1

    # Return top 15 tags sorted by popularity
    top = [{"name": name, "count": count} for name, count in tag_counts.most_common(15)]
    return top


@router.get("/{guide_id}")
def get_guide(guide_id: str):
    """Retrieve detailed travel guide metadata, itinerary highlights, and transport options."""
    guide = get_world_guide_by_id(guide_id)
    if not guide:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="World guide not found")
    return guide


@router.post("/{guide_id}/like")
def like_guide(guide_id: str):
    """Increment like count on a world travel guide."""
    guide = get_world_guide_by_id(guide_id)
    if not guide:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="World guide not found")
    guide["likes"] = guide.get("likes", 0) + 1
    return {"id": guide_id, "likes": guide["likes"]}


@router.post("/{guide_id}/clone", response_model=TripDetailResponse, status_code=status.HTTP_201_CREATED)
def clone_guide(guide_id: str, req: Optional[CloneGuideRequest] = None, db: Session = Depends(get_db)):
    """Clone a world destination guide into an active, editable trip in the workspace."""
    start_date = req.start_date if req else None
    try:
        new_trip = clone_world_guide_to_trip(db=db, guide_id=guide_id, start_date=start_date)
        return get_trip_details(new_trip.id, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to clone guide: {str(e)}")
