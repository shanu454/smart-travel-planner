# 🌍 WanderPulse – Smart Travel Planner

An intelligent, full-stack travel planner and journey companion built with **Python (FastAPI)**, **SQLite (SQLAlchemy 2.0 ORM)**, **Real-Time Travel APIs**, and a **Glassmorphic Modern Web Interface**.

---

## 🚀 Key Features

1. **Smart Algorithmic Journey Generator**:
   - Creates balanced multi-day itineraries broken into **Morning**, **Afternoon**, and **Evening** time slots.
   - Tailored to travel styles: *Cultural & Explorer*, *Foodie & Culinary*, *Adventure & Nature*, *Relaxation & Wellness*, *Budget Backpacking*, or *Luxury Escape*.
   - Pre-loaded with curated destination blueprints for global hubs (Tokyo, Paris, Rome, etc.) and adaptive synthesis for any city worldwide.

2. **Live External APIs (Zero API Keys Required Out-of-the-Box)**:
   - 📍 **Open-Meteo Geocoding**: Real-time city search, coordinate resolution, and country detection.
   - ⛅ **Open-Meteo Forecast**: 7-day meteorological weather forecast, precipitation chance, temperature ranges, and automated climate packing advisories.
   - 💱 **ExchangeRate API**: Real-time currency conversions across major world currencies (USD, EUR, GBP, JPY, INR, CAD, AUD, CHF, etc.).
   - 📚 **Wikipedia REST API**: Destination summary extracts and authentic high-resolution cover photography.

3. **Interactive Day-by-Day Timeline & Route Map**:
   - **Interactive Leaflet.js Map**: Color-coded markers for Morning (Amber), Afternoon (Cyan), and Evening (Violet) stops.
   - Click activity locations to fly to exact map pins and view rich popups.
   - Check off completed activities with progress bar tracking.

4. **Budget & Expense Tracking**:
   - Visual spending meter and safe daily allowance calculator.
   - HTML5 Canvas dynamic category donut chart (Food, Transport, Lodging, Activities, Shopping).
   - Transaction ledger with instant expense logging and deletion.
   - Interactive live currency converter.

5. **Climate-Adapted Smart Packing Checklist**:
   - Dynamically adapts packing lists based on forecast rain probability and temperature extremes (e.g. suggests thermal wear when cold, sunscreen when UV is high, rain gear when showers are predicted).
   - Progress meter showing percentage and item count packed.
   - Add custom packing items.

6. **AI Travel Advisor**:
   - Curated local cultural etiquette, tipping norms, and transit hacks.
   - Interactive Q&A advisor for neighborhood advice, food recommendations, and travel tips.

---

## 🛠️ Architecture & Tech Stack

- **Backend**: Python 3.14, FastAPI, Uvicorn, SQLAlchemy 2.0, Pydantic v2, HTTPX
- **Database**: SQLite with relational schema (`trips`, `itinerary_items`, `expenses`, `packing_items`)
- **Frontend**: Vanilla HTML5 & CSS (Glassmorphism, Google Fonts Plus Jakarta Sans / Outfit, micro-animations, native `<dialog>` with modern entry/exit transitions), Vanilla JS, Leaflet.js

---

## 🏃 Getting Started

### 1. Activate Environment & Install Dependencies
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
python3 run.py
```

Open your browser at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Interactive Swagger API documentation:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
