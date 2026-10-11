"""External APIs proxy and AI Travel Assistant router."""
import os
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel

from app.services.geocoding import search_places
from app.services.weather import get_weather_forecast
from app.services.currency import get_exchange_rates
from app.services.wiki import get_destination_details
from app.schemas import PlaceSearchResult, WeatherForecastResponse, CurrencyRatesResponse

router = APIRouter(prefix="/api", tags=["External APIs & AI"])


class AskAiRequest(BaseModel):
    destination: str
    country: Optional[str] = ""
    query: str
    travel_style: Optional[str] = "Cultural & Explorer"


class AskAiResponse(BaseModel):
    destination: str
    answer: str
    tips: List[str]
    source: str


@router.get("/places/search", response_model=List[PlaceSearchResult])
async def search_destination_places(q: str = Query(..., min_length=2, description="Place or city name")):
    """Search for places and cities using Open-Meteo Geocoding."""
    return await search_places(q, count=8)


@router.get("/weather", response_model=WeatherForecastResponse)
async def get_live_weather(lat: float = Query(...), lon: float = Query(...)):
    """Fetch 7-day live weather forecast and packing recommendations."""
    return await get_weather_forecast(lat, lon)


@router.get("/currency/rates", response_model=CurrencyRatesResponse)
async def get_currency_rates(base: str = Query(default="INR")):
    """Fetch live multi-currency exchange rates."""
    return await get_exchange_rates(base)


@router.get("/wiki/destination")
async def get_wiki_info(name: str = Query(..., min_length=1)):
    """Fetch Wikipedia summary, extract and photos for a destination."""
    return await get_destination_details(name)


@router.post("/ai/travel-tips", response_model=AskAiResponse)
async def ask_travel_ai(req: AskAiRequest):
    """Smart AI Travel Advisor providing instant local tips, etiquette, and custom recommendations for Indian travel."""
    dest = req.destination.strip()
    query_lower = req.query.lower()

    # Curated knowledge base for top Indian destinations
    knowledge = {
        "jaipur": {
            "tips": [
                "UPI (Google Pay, PhonePe, Paytm) is accepted everywhere, from street tea vendors to royal emporiums.",
                "Bargain with a friendly smile at Johari & Bapu Bazaars; counter-offering around 50–60% of the initial quote is normal practice.",
                "Visit Amer Fort and Nahargarh early morning (8:30–10:30 AM) to beat the afternoon desert sun and tourist buses.",
                "Savor authentic crisp Pyaaz Kachoris at Rawat Mishtan Bhandar and clay-cup lassi at Lassiwala on MI Road.",
                "Hire official government-licensed guides bearing green ID cards at monuments to ensure authentic historical storytelling."
            ],
            "general": "Jaipur, the Pink City of Rajasthan, is a royal wonderland of Rajput forts, vibrant bazaars, and opulent heritage palace courtyards."
        },
        "goa": {
            "tips": [
                "Renting a scooter or hatchback car is the best way to explore Goa; always wear a helmet and carry a valid driving license to avoid traffic fines.",
                "North Goa (Anjuna, Baga, Vagator) is famous for watersports, beach parties, and vibrant night markets.",
                "South Goa (Palolem, Agonda, Cavelossim) offers pristine quiet silver beaches, scenic cliffs, and luxury resorts.",
                "Try authentic Goan fish curry thali with red rice, fried pomfret, and traditional Bebinca coconut layer dessert.",
                "Observe modest dress etiquette when entering historic churches like Basilica of Bom Jesus; cover shoulders and knees."
            ],
            "general": "Goa blends sun-drenched Arabian Sea coastlines with 450 years of historic Portuguese architecture, spice farms, and vibrant coastal shacks."
        },
        "varanasi": {
            "tips": [
                "Experience the 'Subah-e-Banaras' dawn wooden boat ride along the 84 ghats as the morning sun illuminates the ancient temples.",
                "Arrive at Dashashwamedh Ghat by 5:45 PM to reserve front-row boat or staircase seating for the mesmerizing Ganga Maha Aarti.",
                "Varanasi's historic winding alleys ('galis') are exclusively pedestrian; comfortable slip-on walking sandals are essential.",
                "Always remove footwear outside temples; friendly flower vendors will look after your shoes for a nominal coin.",
                "Do not miss the iconic Tamatar Chaat at Kashi Chaat Bhandar, hand-churned fruit lassi, and Banarasi Meetha Paan."
            ],
            "general": "Varanasi (Kashi) is one of the world's oldest continually inhabited sacred cities, where timeless spiritual energy and divine Ganga rituals unfold daily."
        },
        "kerala": {
            "tips": [
                "For backwaters exploration in Alleppey, book government SWTD public ferries for an incredible budget alternative to private houseboats.",
                "Feast on traditional Kerala Sadhya served on fresh banana leaf; eat with clean right hand for the authentic local custom.",
                "Munnar hill stations get pleasantly chilly in the evenings (12–16°C); pack a warm shawl or light jacket.",
                "Purchase genuine Malabar black pepper, cardamom, and pure coconut oil directly from cooperative spice plantations.",
                "Experience a live Kathakali dance or Kalaripayattu martial arts performance in Fort Kochi."
            ],
            "general": "Kerala, known as God's Own Country, boasts emerald backwaters, misty Western Ghats tea plantations, and ancient Ayurvedic healing traditions."
        }
    }

    dest_key = dest.lower()
    local_info = None
    for k, v in knowledge.items():
        if k in dest_key:
            local_info = v
            break

    if local_info:
        tips = local_info["tips"]
        intro = local_info["general"]
    else:
        tips = [
            f"Use UPI digital payments (Google Pay / PhonePe); virtually all Indian merchants and auto-drivers accept QR codes.",
            f"Drink only sealed bottled water or RO-purified water; avoid unboiled tap water.",
            f"Book IRCTC Vande Bharat or Rajdhani/Shatabdi express trains 2-3 weeks in advance for comfortable intercity transit.",
            f"Dress respectfully with shoulders and knees covered when visiting sacred temples, gurdwaras, and religious sites.",
            f"Carry a scarf or dupatta for temples, and wear slip-on footwear that is easy to take off outside holy sanctums."
        ]
        intro = f"{dest} is a captivating Indian destination offering vibrant regional culture, historic architecture, and delicious local cuisines."

    # Answer query contextually
    if "food" in query_lower or "eat" in query_lower or "restaurant" in query_lower:
        answer = f"For culinary adventures in {dest}, avoid eateries with multilingual photo menus placed directly outside tourist hotspots. Instead, seek out busy neighborhood side streets where locals queue during lunch hours."
    elif "transit" in query_lower or "metro" in query_lower or "train" in query_lower:
        answer = f"Navigating {dest} is typically easiest via high-frequency public trains or modern rideshare apps. We recommend grabbing a rechargeable transit pass upon arrival at the airport."
    elif "budget" in query_lower or "money" in query_lower:
        answer = f"To maximize your budget in {dest}, take advantage of free museum admission days, eat your main cooked meal at lunchtime for special 'plat du jour' sets, and walk between adjacent sights."
    else:
        answer = f"{intro} Regarding '{req.query}': Focus on prioritizing 2-3 major activities per day with designated buffer time for wandering and spontaneous discoveries."

    return AskAiResponse(
        destination=dest,
        answer=answer,
        tips=tips,
        source="Smart Travel AI Advisor Engine"
    )
