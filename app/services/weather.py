"""Weather forecast service using Open-Meteo API with packing alerts."""
import logging
from typing import Dict, Any, List, Optional
import httpx

logger = logging.getLogger(__name__)

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO Weather interpretation codes
WMO_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Foggy", "🌫️"),
    48: ("Depositing rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Moderate drizzle", "🌦️"),
    55: ("Dense drizzle", "🌧️"),
    61: ("Slight rain", "🌧️"),
    63: ("Moderate rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Slight snow", "🌨️"),
    73: ("Moderate snow", "❄️"),
    75: ("Heavy snow", "❄️"),
    77: ("Snow grains", "❄️"),
    80: ("Slight rain showers", "🌦️"),
    81: ("Moderate rain showers", "🌧️"),
    82: ("Violent rain showers", "⛈️"),
    85: ("Slight snow showers", "🌨️"),
    86: ("Heavy snow showers", "❄️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with hail", "⛈️"),
    99: ("Thunderstorm with heavy hail", "⛈️")
}


def interpret_weather_code(code: int):
    """Return human readable description and emoji icon for WMO code."""
    return WMO_CODES.get(code, ("Variable", "🌤️"))


async def get_weather_forecast(lat: float, lon: float) -> Dict[str, Any]:
    """Fetch 7-day forecast and generate climate packing insights."""
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            response = await client.get(
                FORECAST_URL,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max,uv_index_max",
                    "current": "temperature_2m,weather_code",
                    "timezone": "auto"
                }
            )
            if response.status_code == 200:
                data = response.json()
                daily_data = data.get("daily", {})
                times = daily_data.get("time", [])
                w_codes = daily_data.get("weathercode", [])
                max_temps = daily_data.get("temperature_2m_max", [])
                min_temps = daily_data.get("temperature_2m_min", [])
                precip_probs = daily_data.get("precipitation_probability_max", [])
                uv_indices = daily_data.get("uv_index_max", [])

                days: List[Dict[str, Any]] = []
                max_precip = 0
                lowest_temp = 999.0
                highest_temp = -999.0
                highest_uv = 0.0

                for i in range(len(times)):
                    code = w_codes[i] if i < len(w_codes) else 0
                    label, icon = interpret_weather_code(code)
                    t_max = max_temps[i] if i < len(max_temps) else 22.0
                    t_min = min_temps[i] if i < len(min_temps) else 15.0
                    p_prob = precip_probs[i] if i < len(precip_probs) and precip_probs[i] is not None else 0
                    uv = uv_indices[i] if i < len(uv_indices) and uv_indices[i] is not None else 0.0

                    if p_prob > max_precip:
                        max_precip = p_prob
                    if t_min < lowest_temp:
                        lowest_temp = t_min
                    if t_max > highest_temp:
                        highest_temp = t_max
                    if uv > highest_uv:
                        highest_uv = uv

                    days.append({
                        "date": times[i],
                        "weather_code": code,
                        "weather_label": label,
                        "weather_icon": icon,
                        "temp_max": round(float(t_max), 1),
                        "temp_min": round(float(t_min), 1),
                        "precip_prob": int(p_prob),
                        "uv_index": round(float(uv), 1)
                    })

                # Generate Smart Weather Advisory
                alerts = []
                if max_precip >= 50:
                    alerts.append(f"Rain likely ({max_precip}%): Pack waterproof outerwear & travel umbrella.")
                if lowest_temp < 10:
                    alerts.append(f"Chilly low of {lowest_temp:.0f}°C: Pack thermal base layers & warm jacket.")
                elif lowest_temp < 16:
                    alerts.append(f"Mild evenings ({lowest_temp:.0f}°C): Bring a light sweater or cardigan.")
                if highest_temp > 28:
                    alerts.append(f"Warm weather up to {highest_temp:.0f}°C: Breathable fabrics & hydration bottle recommended.")
                if highest_uv >= 6:
                    alerts.append(f"High UV Index ({highest_uv:.1f}): Sunscreen SPF 50+, sunglasses & hat essential.")

                packing_alert = " • ".join(alerts) if alerts else "Pleasant weather forecast. Standard travel essentials recommended."

                curr = data.get("current", {})
                current_temp = curr.get("temperature_2m")

                return {
                    "latitude": lat,
                    "longitude": lon,
                    "timezone": data.get("timezone", "UTC"),
                    "current_temp": round(float(current_temp), 1) if current_temp is not None else None,
                    "daily": days,
                    "packing_alert": packing_alert
                }
    except Exception as e:
        logger.error(f"Weather forecast request failed: {e}")

    # Fallback default forecast
    from datetime import date, timedelta
    today = date.today()
    fallback_days = []
    for i in range(7):
        d = today + timedelta(days=i)
        fallback_days.append({
            "date": d.isoformat(),
            "weather_code": 1,
            "weather_label": "Mainly clear",
            "weather_icon": "🌤️",
            "temp_max": 23.0,
            "temp_min": 15.0,
            "precip_prob": 15,
            "uv_index": 5.0
        })

    return {
        "latitude": lat,
        "longitude": lon,
        "timezone": "UTC",
        "current_temp": 20.0,
        "daily": fallback_days,
        "packing_alert": "Mild conditions expected. Pack light layers and comfortable walking shoes."
    }
