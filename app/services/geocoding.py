"""Geocoding service using Open-Meteo Geocoding API."""
import logging
from typing import List, Dict, Any, Optional
import httpx

logger = logging.getLogger(__name__)

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


async def search_places(query: str, count: int = 8) -> List[Dict[str, Any]]:
    """Search for cities, towns, and tourist destinations worldwide."""
    if not query or len(query.strip()) < 2:
        return []

    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            response = await client.get(
                GEOCODING_URL,
                params={
                    "name": query.strip(),
                    "count": count,
                    "language": "en",
                    "format": "json"
                }
            )
            if response.status_code == 200:
                data = response.json()
                results = []
                raw_results = data.get("results", [])
                results = []
                for item in raw_results:
                    results.append({
                        "name": item.get("name", ""),
                        "country": item.get("country", "India"),
                        "admin1": item.get("admin1", ""),
                        "latitude": float(item.get("latitude", 0.0)),
                        "longitude": float(item.get("longitude", 0.0)),
                        "timezone": item.get("timezone", "Asia/Kolkata"),
                        "country_code": item.get("country_code", "IN")
                    })
                # Prioritize Indian results to the top
                results.sort(key=lambda x: (0 if x.get("country_code") == "IN" else 1))
                return results
            else:
                logger.warning(f"Geocoding API returned status {response.status_code}")
    except Exception as e:
        logger.error(f"Geocoding request failed: {e}")

    # Fallback to popular Indian travel destinations
    query_lower = query.lower()
    fallback_destinations = [
        {"name": "Jaipur", "country": "India", "admin1": "Rajasthan", "latitude": 26.9124, "longitude": 75.7873, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Goa", "country": "India", "admin1": "Goa", "latitude": 15.2993, "longitude": 74.1240, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Varanasi", "country": "India", "admin1": "Uttar Pradesh", "latitude": 25.3176, "longitude": 82.9739, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Udaipur", "country": "India", "admin1": "Rajasthan", "latitude": 24.5854, "longitude": 73.7125, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Munnar", "country": "India", "admin1": "Kerala", "latitude": 10.0889, "longitude": 77.0595, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Manali", "country": "India", "admin1": "Himachal Pradesh", "latitude": 32.2432, "longitude": 77.1892, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Rishikesh", "country": "India", "admin1": "Uttarakhand", "latitude": 30.0869, "longitude": 78.2676, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Agra", "country": "India", "admin1": "Uttar Pradesh", "latitude": 27.1767, "longitude": 78.0081, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Delhi", "country": "India", "admin1": "National Capital Territory", "latitude": 28.6139, "longitude": 77.2090, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Leh Ladakh", "country": "India", "admin1": "Ladakh", "latitude": 34.1526, "longitude": 77.5771, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Mumbai", "country": "India", "admin1": "Maharashtra", "latitude": 19.0760, "longitude": 72.8777, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Bengaluru", "country": "India", "admin1": "Karnataka", "latitude": 12.9716, "longitude": 77.5946, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Alleppey", "country": "India", "admin1": "Kerala", "latitude": 9.4981, "longitude": 76.3388, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Amritsar", "country": "India", "admin1": "Punjab", "latitude": 31.6340, "longitude": 74.8723, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Kolkata", "country": "India", "admin1": "West Bengal", "latitude": 22.5726, "longitude": 88.3639, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Pondicherry", "country": "India", "admin1": "Puducherry", "latitude": 11.9416, "longitude": 79.8083, "timezone": "Asia/Kolkata", "country_code": "IN"},
        {"name": "Darjeeling", "country": "India", "admin1": "West Bengal", "latitude": 27.0410, "longitude": 88.2663, "timezone": "Asia/Kolkata", "country_code": "IN"}
    ]
    return [d for d in fallback_destinations if query_lower in d["name"].lower() or query_lower in d["admin1"].lower()]
