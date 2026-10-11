"""Seed rich Indian travel itineraries and Sacred Dham Yatras into the database."""
from datetime import date, timedelta
from app.database import SessionLocal, Base, engine
from app.models import Trip, ItineraryItem, Expense, PackingItem, TransportOption
from app.services.planner import generate_smart_itinerary, generate_smart_packing_list
from app.services.pilgrimage import PILGRIMAGE_CIRCUITS, calculate_dham_budget


def seed_database():
    """Seed initial Indian trips & Dham yatras if database is empty or needs refresh."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        print("Refreshing database with authentic Indian itineraries and sacred Dham Yatras...")
        db.query(TransportOption).delete()
        db.query(Expense).delete()
        db.query(ItineraryItem).delete()
        db.query(PackingItem).delete()
        db.query(Trip).delete()
        db.commit()

        today = date.today()

        # -----------------------------------------------------------------
        # 1. Seed Core Sacred Dham Yatras
        # -----------------------------------------------------------------
        dham_keys = [
            ("do-dham-kedarnath-badrinath", 5),
            ("vaishno-devi-shiv-khori", 12),
            ("tirupati-balaji", 18),
            ("ayodhya-kashi", 25),
            ("jagannath-puri", 32),
            ("dwarka-somnath", 40),
            ("ujjain-omkareshwar", 48)
        ]

        for circuit_key, offset in dham_keys:
            circuit = PILGRIMAGE_CIRCUITS[circuit_key]
            s_date = today + timedelta(days=offset)
            e_date = s_date + timedelta(days=circuit["recommended_days"] - 1)
            b_calc = calculate_dham_budget(circuit_key, travel_tier="Standard", num_travelers=1, departure_date=s_date.isoformat())

            trip = Trip(
                title=circuit["title"],
                destination=circuit["destination"],
                country="India",
                latitude=circuit["latitude"],
                longitude=circuit["longitude"],
                start_date=s_date.isoformat(),
                end_date=e_date.isoformat(),
                travel_style="Spiritual & Pilgrimage",
                travel_pace="Moderate",
                total_budget=b_calc["total_budget"],
                currency="INR",
                cover_image=circuit["cover_image"],
                notes=circuit["description"]
            )
            db.add(trip)
            db.commit()
            db.refresh(trip)

            # Itinerary
            order = 1
            for day_num, slot, act_title, loc, lat, lon, cost, cat, desc in circuit["itinerary_highlights"]:
                db.add(ItineraryItem(
                    trip_id=trip.id,
                    day_number=day_num,
                    time_slot=slot,
                    title=act_title,
                    description=desc,
                    location=loc,
                    latitude=lat,
                    longitude=lon,
                    estimated_cost=cost,
                    category=cat,
                    is_completed=False,
                    order_index=order
                ))
                order += 1

            # Transport
            for mode, trans_title, route, cost, tips in circuit["transports"]:
                db.add(TransportOption(
                    trip_id=trip.id,
                    mode=mode,
                    title=trans_title,
                    route=route,
                    estimated_cost=cost,
                    currency="INR",
                    booking_tips=tips,
                    is_booked=False
                ))

            # Initial Expense
            db.add(Expense(
                trip_id=trip.id,
                title="Confirmed Vande Bharat / Express Train Tickets",
                amount=round(b_calc["breakdown"]["transport"] * 0.45, 2),
                currency="INR",
                category="Transport",
                date=today.isoformat(),
                notes="IRCTC advance booking deposit"
            ))
            db.add(Expense(
                trip_id=trip.id,
                title="Dharamshala / Hotel Booking Deposit",
                amount=round(b_calc["breakdown"]["stay"] * 0.4, 2),
                currency="INR",
                category="Accommodation",
                date=today.isoformat(),
                notes="Pilgrim rest house advance"
            ))

            # Packing list
            p_items = generate_smart_packing_list(circuit["destination"], circuit["recommended_days"], None, "Spiritual & Pilgrimage")
            for p in p_items:
                db.add(PackingItem(
                    trip_id=trip.id,
                    category=p["category"],
                    item_name=p["item_name"],
                    is_packed=False,
                    is_suggested=True
                ))
            for item_name in circuit.get("packing_extras", []):
                db.add(PackingItem(
                    trip_id=trip.id,
                    category="Gear",
                    item_name=item_name,
                    is_packed=False,
                    is_suggested=True
                ))

        # -----------------------------------------------------------------
        # 2. Seed Flagship Leisure & Heritage Destinations
        # -----------------------------------------------------------------
        leisure_configs = [
            # Jaipur
            {
                "title": "5-Day Royal Rajasthan Heritage: Jaipur & Amber Odyssey",
                "destination": "Jaipur",
                "country": "India",
                "latitude": 26.9124,
                "longitude": 75.7873,
                "days": 5,
                "start_offset": 8,
                "travel_style": "Cultural & Heritage",
                "travel_pace": "Moderate",
                "total_budget": 35000.0,
                "cover_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
                "notes": "Experience royal grandeur: Rajput fortresses, Sheesh Mahal mirror palace, colorful bazaars, and royal Rajasthani hospitality.",
                "transports": [
                    ("Train", "Vande Bharat Express (Delhi to Jaipur Jn)", "New Delhi (NDLS) → Jaipur Jn (JP)", 2400.0, "Executive Chair Car. Includes hot meals; leaves early morning."),
                    ("Cab/Taxi", "Prepaid AC Airport/Station Transfer", "Jaipur Jn → Heritage Haveli (Old City)", 650.0, "Book at official prepaid counter inside station exit gate."),
                    ("Cab/Taxi", "Full-Day Amer & Nahargarh Fort Sightseeing", "City Palace → Amer Fort → Nahargarh Sunset", 2200.0, "AC Sedan hire for 8 hours. Covers hill climbs to forts."),
                    ("Auto-Rickshaw", "Pink City Bazaars & Hawa Mahal E-Rickshaw", "Johari Bazaar ⇄ Bapu Bazaar ⇄ Hawa Mahal", 450.0, "Best way to navigate narrow walled-city alleyways.")
                ],
                "expenses": [
                    ("Heritage Haveli Palace Hotel (2 Nights Deposit)", 12000.0, "Accommodation", -4, "Old city heritage haveli stay"),
                    ("Vande Bharat Train Tickets", 2400.0, "Transport", -2, "Advance IRCTC confirmed ticket"),
                    ("Amer Fort & Composite Monument Pass", 1000.0, "Activities", -1, "Combo ticket for 8 monuments")
                ]
            },
            # Goa
            {
                "title": "4-Day Tropical Goa: Sun, Portuguese Heritage & Spice Trails",
                "destination": "Goa",
                "country": "India",
                "latitude": 15.2993,
                "longitude": 74.1240,
                "days": 4,
                "start_offset": 22,
                "travel_style": "Relaxation & Beach",
                "travel_pace": "Relaxed",
                "total_budget": 28000.0,
                "cover_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
                "notes": "Relaxed coastal getaway exploring colorful Fontainhas villas, UNESCO cathedrals, tranquil South Goa beaches, and sunset seafood shacks.",
                "transports": [
                    ("Flight", "Domestic Flight to Goa Mopa (GOX)", "Delhi/Mumbai → Manohar Intl Airport (GOX)", 5800.0, "Mopa airport offers quick highway access to North Goa."),
                    ("Cab/Taxi", "GoaMiles Prepaid Airport Cab", "GOX Airport → Candolim Beach Resort", 1600.0, "Book via GoaMiles app or airport government taxi booth."),
                    ("Scooter", "Honda Activa Scooter Rental (4 Days)", "Self-drive local beach & market exploration", 1800.0, "₹450/day. Always wear helmet; keep physical driving license.")
                ],
                "expenses": [
                    ("Candolim Beachfront Boutique Resort", 14000.0, "Accommodation", -5, "3 nights ocean-view room deposit"),
                    ("Scooter Fuel & Security Deposit", 1000.0, "Transport", -1, "Full tank fuel")
                ]
            },
            # Munnar (Kerala)
            {
                "title": "5-Day Serene Kerala: Tea Valleys, Waterfalls & Backwater Cruises",
                "destination": "Munnar",
                "country": "India",
                "latitude": 10.0889,
                "longitude": 77.0595,
                "days": 5,
                "start_offset": 30,
                "travel_style": "Nature & Eco-Tour",
                "travel_pace": "Relaxed",
                "total_budget": 32000.0,
                "cover_image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
                "notes": "Lush green emerald hills, sprawling Tata tea plantations, Eravikulam Nilgiri Tahr sanctuary, and a tranquil overnight houseboat cruise.",
                "transports": [
                    ("Cab/Taxi", "Private AC Innova Hill Transfer", "Kochi Airport (COK) → Munnar Hill Station", 3200.0, "Scenic 4-hour mountain drive via Cheeyappara waterfalls."),
                    ("Ferry", "Traditional Deluxe Houseboat Cruise", "Alleppey Punnamada Jetty ⇄ Vembanad Lake", 8500.0, "Overnight stay with all 3 traditional Kerala meals included.")
                ],
                "expenses": [
                    ("Munnar Tea Valley Treehouse Resort", 11000.0, "Accommodation", -4, "2 nights amidst tea gardens"),
                    ("Houseboat Advance Deposit", 4000.0, "Accommodation", -2, "Alleppey backwater cruise advance")
                ]
            },
            # Manali
            {
                "title": "6-Day Himalayan Adventure: Manali Snow Peaks & Rohtang Pass",
                "destination": "Manali",
                "country": "India",
                "latitude": 32.2432,
                "longitude": 77.1892,
                "days": 6,
                "start_offset": 38,
                "travel_style": "Adventure & Mountain",
                "travel_pace": "Fast-Paced",
                "total_budget": 30000.0,
                "cover_image": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
                "notes": "High altitude thrills: Atal Tunnel transit, Solang Valley paragliding, Rohtang snowline, Jogini waterfall hike, and Old Manali riverside cafes.",
                "transports": [
                    ("Bus", "HPTDC Volvo Semi-Sleeper AC Bus", "Delhi Kashmiri Gate ⇄ Manali Mall Road (Overnight)", 3200.0, "Govt luxury bus with blankets, water & heating."),
                    ("Cab/Taxi", "4x4 SUV Rohtang Pass & Atal Tunnel Permit Cab", "Manali ⇄ Atal Tunnel ⇄ Rohtang Snow View", 4500.0, "Requires green NGT permit; SUV required for snowy passes.")
                ],
                "expenses": [
                    ("Old Manali Pine Chalet Stay", 9500.0, "Accommodation", -6, "Cedar forest river cottage"),
                    ("Solang Valley Paragliding Flight", 3200.0, "Activities", 0, "High fly tandem glider with GoPro video")
                ]
            },
            # Leh Ladakh
            {
                "title": "7-Day High Mountain Odyssey: Pangong Tso, Nubra & Khardung La",
                "destination": "Leh Ladakh",
                "country": "India",
                "latitude": 34.1526,
                "longitude": 77.5771,
                "days": 7,
                "start_offset": 55,
                "travel_style": "Adventure & Mountain",
                "travel_pace": "Fast-Paced",
                "total_budget": 48000.0,
                "cover_image": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
                "notes": "Once-in-a-lifetime Himalayan journey across Khardung La (18,380 ft), Nubra Valley double-humped camel safari, and turquoise Pangong Lake.",
                "transports": [
                    ("Flight", "Scenic Flight into Leh Kushok Bakula Airport", "Delhi (DEL) → Leh (IXL)", 7500.0, "Spectacular snow-capped Himalayan flight vistas."),
                    ("Cab/Taxi", "Ladakh Taxi Union 4x4 Scorpio / Innova (4 Days)", "Leh ⇄ Khardung La ⇄ Nubra Valley ⇄ Pangong Lake", 18500.0, "Official registered local union SUV for rugged mountain passes.")
                ],
                "expenses": [
                    ("Leh Heritage Guest House & Luxury Camp", 16000.0, "Accommodation", -6, "Includes Pangong luxury tent stay"),
                    ("Inner Line Permit (ILP) & Wildlife Fee", 650.0, "Activities", -1, "DC Office mandatory permit")
                ]
            }
        ]

        for conf in leisure_configs:
            s_date = today + timedelta(days=conf["start_offset"])
            e_date = s_date + timedelta(days=conf["days"] - 1)

            trip = Trip(
                title=conf["title"],
                destination=conf["destination"],
                country=conf["country"],
                latitude=conf["latitude"],
                longitude=conf["longitude"],
                start_date=s_date.isoformat(),
                end_date=e_date.isoformat(),
                travel_style=conf["travel_style"],
                travel_pace=conf["travel_pace"],
                total_budget=conf["total_budget"],
                currency="INR",
                cover_image=conf["cover_image"],
                notes=conf["notes"]
            )
            db.add(trip)
            db.commit()
            db.refresh(trip)

            acts = generate_smart_itinerary(
                destination=conf["destination"],
                country=conf["country"],
                lat=conf["latitude"],
                lon=conf["longitude"],
                start_date_str=s_date.isoformat(),
                end_date_str=e_date.isoformat(),
                travel_style=conf["travel_style"],
                travel_pace=conf["travel_pace"],
                total_budget=conf["total_budget"]
            )
            for act in acts:
                db.add(ItineraryItem(
                    trip_id=trip.id,
                    day_number=act["day_number"],
                    time_slot=act["time_slot"],
                    title=act["title"],
                    description=act["description"],
                    location=act["location"],
                    latitude=act["latitude"],
                    longitude=act["longitude"],
                    estimated_cost=act["estimated_cost"],
                    category=act["category"],
                    is_completed=False,
                    order_index=act["order_index"]
                ))

            for mode, title, route, cost, tips in conf["transports"]:
                db.add(TransportOption(
                    trip_id=trip.id,
                    mode=mode,
                    title=title,
                    route=route,
                    estimated_cost=cost,
                    currency="INR",
                    booking_tips=tips,
                    is_booked=False
                ))

            for exp_title, exp_amt, exp_cat, exp_day_offset, exp_notes in conf["expenses"]:
                db.add(Expense(
                    trip_id=trip.id,
                    title=exp_title,
                    amount=exp_amt,
                    currency="INR",
                    category=exp_cat,
                    date=(today + timedelta(days=exp_day_offset)).isoformat(),
                    notes=exp_notes
                ))

            p_items = generate_smart_packing_list(conf["destination"], conf["days"], None, conf["travel_style"])
            for p in p_items:
                db.add(PackingItem(
                    trip_id=trip.id,
                    category=p["category"],
                    item_name=p["item_name"],
                    is_packed=False,
                    is_suggested=True
                ))

        db.commit()
        print("Successfully seeded 12 iconic Indian journeys including 7 major Dham & Temple Yatras!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
