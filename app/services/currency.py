"""Currency exchange rate service with caching."""
import time
import logging
from typing import Dict, Any, Optional
import httpx

logger = logging.getLogger(__name__)

CACHE: Dict[str, Any] = {}
CACHE_TTL = 3600  # 1 hour cache


# Popular fallback exchange rates relative to USD
FALLBACK_USD_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 155.5,
    "CAD": 1.36,
    "AUD": 1.52,
    "CHF": 0.90,
    "INR": 83.4,
    "SGD": 1.35,
    "CNY": 7.23,
    "AED": 3.67,
    "THB": 36.8,
    "KRW": 1370.0,
    "BRL": 5.15,
    "MXN": 16.9
}


async def get_exchange_rates(base_currency: str = "INR") -> Dict[str, Any]:
    """Fetch real-time currency exchange rates with local memory cache."""
    base = base_currency.upper()
    now = time.time()

    if base in CACHE:
        cached_data, timestamp = CACHE[base]
        if now - timestamp < CACHE_TTL:
            return cached_data

    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                data = resp.json()
                rates = data.get("rates", {})
                result = {
                    "base": base,
                    "rates": rates,
                    "updated_at": data.get("time_last_update_utc", "")
                }
                CACHE[base] = (result, now)
                return result
    except Exception as e:
        logger.error(f"Currency rates API error: {e}")

    # Compute fallback rates if base is different
    usd_rate = FALLBACK_USD_RATES.get(base, 1.0)
    converted_rates = {k: round(v / usd_rate, 4) for k, v in FALLBACK_USD_RATES.items()}
    fallback_result = {
        "base": base,
        "rates": converted_rates,
        "updated_at": "Offline fallback rate table"
    }
    CACHE[base] = (fallback_result, now)
    return fallback_result


def convert_currency_sync(amount: float, from_curr: str, to_curr: str, rates: Dict[str, float]) -> float:
    """Helper to convert between currencies given a rates dictionary with from_curr as base."""
    if from_curr == to_curr or amount == 0:
        return amount
    rate = rates.get(to_curr, 1.0)
    return round(amount * rate, 2)
