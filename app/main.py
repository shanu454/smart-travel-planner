"""Main FastAPI application entrypoint."""
import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import engine, Base
from app.routes import trips, itinerary, expenses, packing, apis, transport, pilgrimage, world_guides, stays, auth, guides

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Travel Planner API",
    description="Intelligent multi-day travel planner with live weather, geocoding, currency exchange, and interactive itinerary management.",
    version="1.0.0"
)

# Enable CORS for flexible development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(auth.router)
app.include_router(trips.router)
app.include_router(itinerary.router)
app.include_router(expenses.router)
app.include_router(packing.router)
app.include_router(transport.router)
app.include_router(pilgrimage.router)
app.include_router(world_guides.router)
app.include_router(stays.router)
app.include_router(guides.router)
app.include_router(apis.router)

# Mount static files
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.api_route("/", methods=["GET", "HEAD"])
@app.api_route("/index.html", methods=["GET", "HEAD"])
def serve_index():
    """Serve the primary single-page web app without caching."""
    index_file = static_dir / "index.html"
    if index_file.exists():
        return FileResponse(
            str(index_file),
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return {
        "status": "online",
        "message": "Smart Travel Planner API is running. Access /docs for interactive Swagger API documentation."
    }


@app.get("/world-guide/{guide_id}")
@app.get("/world-guide")
def serve_world_guide_page(guide_id: str = None):
    """Serve the dedicated standalone world destination guide page."""
    guide_file = static_dir / "world-guide.html"
    if guide_file.exists():
        return FileResponse(
            str(guide_file),
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return FileResponse(str(static_dir / "index.html"))



@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "smart-travel-planner"}
