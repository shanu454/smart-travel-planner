"""Wikipedia summary & destination imagery service."""
import urllib.parse
import logging
from typing import Dict, Any, Optional
import httpx

logger = logging.getLogger(__name__)

WIKI_SUMMARY_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"

# High quality fallback photography for Indian destinations
CURATED_COVERS = {
    "jaipur": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
    "goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
    "varanasi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "udaipur": "https://images.unsplash.com/photo-1605649487212-47bdab064df8?auto=format&fit=crop&w=1200&q=80",
    "kerala": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "munnar": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "alleppey": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=1200&q=80",
    "agra": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
    "taj mahal": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
    "delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "manali": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
    "rishikesh": "https://images.unsplash.com/photo-1596895111956-bf1cf0599ce5?auto=format&fit=crop&w=1200&q=80",
    "mumbai": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
    "ladakh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "leh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "amritsar": "https://images.unsplash.com/photo-1588714477688-cf28a50e94f7?auto=format&fit=crop&w=1200&q=80",
    "kolkata": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1200&q=80"
}
DEFAULT_COVER = "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=1200&q=80"


async def get_destination_details(destination_name: str) -> Dict[str, Any]:
    """Retrieve destination summary, extract, and photo from Wikipedia or curated collection."""
    clean_name = destination_name.strip()
    encoded = urllib.parse.quote(clean_name.replace(" ", "_"))

    thumbnail_url = None
    extract = ""
    page_url = ""

    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get(
                f"{WIKI_SUMMARY_API}{encoded}",
                headers={"User-Agent": "SmartTravelPlanner/1.0 (contact: support@smarttravel.local)"}
            )
            if resp.status_code == 200:
                data = resp.json()
                extract = data.get("extract", "")
                if data.get("originalimage"):
                    thumbnail_url = data["originalimage"].get("source")
                elif data.get("thumbnail"):
                    thumbnail_url = data["thumbnail"].get("source")
                page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")
    except Exception as e:
        logger.error(f"Wikipedia lookup error for {destination_name}: {e}")

    # Fallback to curated photography if no wiki image or wiki failed
    if not thumbnail_url:
        dest_lower = clean_name.lower()
        for key, url in CURATED_COVERS.items():
            if key in dest_lower:
                thumbnail_url = url
                break
        if not thumbnail_url:
            thumbnail_url = DEFAULT_COVER

    if not extract:
        extract = f"Explore the breathtaking culture, landmarks, and vibrant scenery of {clean_name}."

    return {
        "title": clean_name,
        "extract": extract,
        "image_url": thumbnail_url,
        "page_url": page_url
    }
