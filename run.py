"""Startup runner for Smart Travel Planner."""
import uvicorn
from seed_data import seed_database

if __name__ == "__main__":
    print("=" * 60)
    print(" 🌍 SMART TRAVEL PLANNER - Launching Server")
    print("=" * 60)
    # Ensure database is seeded
    seed_database()
    import socket
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        local_ip = "10.15.99.99"

    print(" ✨ Local Machine: http://127.0.0.1:8000 or http://localhost:8000")
    print(f" 📱 Network (Phone/Other devices): http://{local_ip}:8000")
    print(" 📖 Interactive API Docs: http://127.0.0.1:8000/docs")
    print("=" * 60)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
