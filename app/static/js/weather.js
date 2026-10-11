/**
 * Weather Module: Live forecast rendering & climate packing alerts.
 */

async function fetchAndRenderWeather(lat, lon, destinationName) {
  const container = document.getElementById("weather-forecast-grid");
  const heroCity = document.getElementById("weather-city-name");
  const heroCond = document.getElementById("weather-condition-desc");
  const heroIcon = document.getElementById("weather-hero-icon");
  const heroAlert = document.getElementById("weather-alert-message");

  if (!container) return;

  if (!lat || !lon) {
    if (heroCity) heroCity.textContent = `${destinationName} Weather`;
    if (heroCond) heroCond.textContent = "Coordinates unavailable for live weather.";
    return;
  }

  container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding: 2rem; color: var(--text-dim);">Loading live 7-day meteorological forecast...</div>`;

  try {
    const res = await fetch(`/api/weather?lat=${lat}&lon=${lon}`);
    if (!res.ok) throw new Error("Weather API error");
    const data = await res.json();

    const daily = data.daily || [];
    const today = daily[0] || {};

    if (heroCity) heroCity.textContent = `${destinationName} 7-Day Forecast`;
    if (heroCond) {
      const curTemp = data.current_temp !== null ? `${data.current_temp}°C` : `${today.temp_max}°C`;
      heroCond.textContent = `${today.weather_label || 'Pleasant'} • Current ~${curTemp} (H: ${today.temp_max}°C / L: ${today.temp_min}°C)`;
    }
    if (heroIcon) heroIcon.textContent = today.weather_icon || "🌤️";
    if (heroAlert) heroAlert.textContent = data.packing_alert || "Pleasant weather forecast. Standard travel essentials recommended.";

    // Render 7-day cards
    container.innerHTML = "";
    daily.forEach((day, idx) => {
      const card = document.createElement("div");
      card.className = "forecast-day-card";

      const dateObj = new Date(day.date + "T00:00:00");
      const dayName = idx === 0 ? "Today" : dateObj.toLocaleDateString("en-US", { weekday: "short" });
      const formattedDate = dateObj.toLocaleDateString("en-US", { month: "short", day: "numeric" });

      card.innerHTML = `
        <span class="forecast-day-name">${dayName}</span>
        <span class="forecast-date">${formattedDate}</span>
        <div class="forecast-icon">${day.weather_icon || '🌤️'}</div>
        <div class="forecast-temps">
          <span class="temp-high">${day.temp_max}°</span>
          <span class="temp-low">${day.temp_min}°</span>
        </div>
        <div class="forecast-rain">💧 ${day.precip_prob}% rain</div>
      `;
      container.appendChild(card);
    });

  } catch (err) {
    console.error("Weather error:", err);
    container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding: 2rem; color: var(--accent-rose);">Unable to load weather forecast right now.</div>`;
  }
}

window.WeatherModule = {
  fetchAndRenderWeather
};
