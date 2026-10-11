/**
 * Map Module: Leaflet.js interactive maps with custom dark-matter styling.
 */
let mapInstance = null;
let markerLayerGroup = null;

function initMap(defaultLat = 35.6895, defaultLon = 139.6917) {
  const mapElement = document.getElementById("leaflet-map");
  if (!mapElement) return;

  if (mapInstance) {
    mapInstance.remove();
    mapInstance = null;
  }

  // Create Leaflet instance
  mapInstance = L.map("leaflet-map", {
    zoomControl: true,
    attributionControl: false
  }).setView([defaultLat, defaultLon], 12);

  // High-aesthetic CartoDB Dark Matter tiles
  L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", {
    maxZoom: 19,
    subdomains: "abcd"
  }).addTo(mapInstance);

  markerLayerGroup = L.layerGroup().addTo(mapInstance);
}

function updateMapPins(activities, centerLat, centerLon) {
  if (!mapInstance) {
    initMap(centerLat, centerLon);
  }

  if (!markerLayerGroup) {
    markerLayerGroup = L.layerGroup().addTo(mapInstance);
  } else {
    markerLayerGroup.clearLayers();
  }

  const validMarkers = [];

  activities.forEach(act => {
    const lat = act.latitude || centerLat;
    const lon = act.longitude || centerLon;

    if (!lat || !lon) return;

    // Pick color by time slot
    let pinColor = "#f59e0b"; // Morning amber
    if (act.time_slot === "Afternoon") pinColor = "#06b6d4"; // Cyan
    if (act.time_slot === "Evening") pinColor = "#8b5cf6"; // Violet

    const customIcon = L.divIcon({
      className: "custom-leaflet-marker",
      html: `
        <div style="
          width: 28px;
          height: 28px;
          background: ${pinColor};
          border: 2px solid #ffffff;
          border-radius: 50%;
          box-shadow: 0 4px 12px rgba(0,0,0,0.5);
          display: flex;
          align-items: center;
          justify-content: center;
          color: #ffffff;
          font-weight: 700;
          font-size: 11px;
          cursor: pointer;
        ">
          ${act.order_index || "•"}
        </div>
      `,
      iconSize: [28, 28],
      iconAnchor: [14, 14]
    });

    const marker = L.marker([lat, lon], { icon: customIcon });

    const popupHtml = `
      <div class="custom-map-popup">
        <h4>${act.title}</h4>
        <p>${act.location || ""}</p>
        <span class="popup-cost">${act.time_slot} • ${act.estimated_cost > 0 ? '$' + act.estimated_cost : 'Free'}</span>
      </div>
    `;

    marker.bindPopup(popupHtml);
    markerLayerGroup.addLayer(marker);
    validMarkers.push([lat, lon]);
  });

  const badge = document.getElementById("map-stops-badge");
  if (badge) {
    badge.textContent = `${validMarkers.length} Stops`;
  }

  if (validMarkers.length > 1) {
    mapInstance.fitBounds(validMarkers, { padding: [40, 40], maxZoom: 15 });
  } else if (validMarkers.length === 1) {
    mapInstance.setView(validMarkers[0], 13);
  } else if (centerLat && centerLon) {
    mapInstance.setView([centerLat, centerLon], 12);
  }

  setTimeout(() => {
    if (mapInstance) mapInstance.invalidateSize();
  }, 250);
}

function flyToLocation(lat, lon, title) {
  if (!mapInstance || !lat || !lon) return;
  mapInstance.flyTo([lat, lon], 15, { duration: 1.2 });
}

window.MapModule = {
  initMap,
  updateMapPins,
  flyToLocation
};
