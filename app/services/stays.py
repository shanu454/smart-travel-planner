"""Curated Lodging & Stays Service for Hotels, Airbnbs, and Hostels worldwide."""
from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime, date, timedelta
from sqlalchemy.orm import Session
from app.models import Trip, Expense

STAYS_CATALOG: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # 1. LUXURY & BOUTIQUE HOTELS
    # -------------------------------------------------------------------------
    {
        "id": "hotel-taj-lake-palace",
        "title": "Taj Lake Palace",
        "type": "hotel",
        "category_label": "5★ Luxury Heritage Palace",
        "destination": "Udaipur, Rajasthan",
        "city": "Udaipur",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.95,
        "reviews_count": 1840,
        "is_superhost": True,
        "badge_text": "Iconic Heritage Palace",
        "price_per_night_inr": 36500,
        "address": "Pichola, Udaipur, Rajasthan 313001",
        "proximity": "Floating on Lake Pichola, private boat arrival",
        "overview": "Built between 1743 and 1746 by Maharana Jagat Singh II as a royal summer palace, this white marble wonderland appears to float serenely on Lake Pichola. Features butler service, Jiva Spa on a royal boat, and bespoke Mewari dining.",
        "amenities": ["🏊 Private Lake Pool", "📶 High-speed WiFi", "🍳 Royal Breakfast", "❄️ Central AC", "💆 Jiva Spa", "🍸 Fine Dining Lounge", "🚤 Royal Boat Transfers"],
        "room_type": "Palace Garden Room (King Bed, Lake View)",
        "max_guests": 2,
        "cancellation_policy": "Free cancellation up to 72 hours before arrival."
    },
    {
        "id": "hotel-imperial-delhi",
        "title": "The Imperial New Delhi",
        "type": "hotel",
        "category_label": "5★ Colonial Heritage Hotel",
        "destination": "New Delhi",
        "city": "New Delhi",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.88,
        "reviews_count": 2150,
        "is_superhost": True,
        "badge_text": "Historic Landmark",
        "price_per_night_inr": 18500,
        "address": "Janpath, Connaught Place, New Delhi 110001",
        "proximity": "0.4 km to Connaught Place, 1.2 km to India Gate",
        "overview": "Legendary 1930s hotel blending Victorian style with subtle Art Deco. Home to an invaluable museum collection of British Raj artwork, award-winning restaurants like 1911, and tranquil palm-fringed gardens in the heart of the capital.",
        "amenities": ["🏊 Outdoor Pool", "📶 Free WiFi", "🍳 Buffet Breakfast", "❄️ Central AC", "🏋️ Fitness Center", "🍸 1911 Bar", "🚗 Airport Limousine"],
        "room_type": "Heritage Grand Room (King Bed)",
        "max_guests": 3,
        "cancellation_policy": "Free cancellation up to 48 hours before check-in."
    },
    {
        "id": "hotel-alila-diwa-goa",
        "title": "Alila Diwa Goa Beach Resort",
        "type": "hotel",
        "category_label": "5★ Coastal Beach Resort",
        "destination": "Majorda, South Goa",
        "city": "Goa",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.91,
        "reviews_count": 1420,
        "is_superhost": True,
        "badge_text": "Paddy View Infinity Pool",
        "price_per_night_inr": 14200,
        "address": "48/10 Adao Waddo, Majorda, Goa 403713",
        "proximity": "0.6 km to Majorda Beach (Private Shuttle included)",
        "overview": "Nestled amidst lush paddy fields in South Goa, Alila Diwa combines traditional Goan architecture with high-vaulted roofs and deep verandas. Features an iconic infinity pool merging into the emerald green rice terraces.",
        "amenities": ["🏊 Infinity Pool", "📶 High-speed WiFi", "🍳 Continental Breakfast", "❄️ AC", "🏖️ Beach Shuttle", "🍹 Poolside Bistro", "🧒 Kids Club"],
        "room_type": "Terrace Room with Balcony (Paddy View)",
        "max_guests": 3,
        "cancellation_policy": "Full refund up to 7 days prior to check-in."
    },
    {
        "id": "hotel-ananda-himalayas",
        "title": "Ananda in the Himalayas",
        "type": "hotel",
        "category_label": "5★ Luxury Himalayan Wellness Palace",
        "destination": "Rishikesh, Uttarakhand",
        "city": "Rishikesh",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.97,
        "reviews_count": 980,
        "is_superhost": True,
        "badge_text": "World's Best Spa Resort",
        "price_per_night_inr": 42000,
        "address": "The Palace Estate, Narendra Nagar, Uttarakhand 249175",
        "proximity": "High mountain ridge overlooking Rishikesh and the holy Ganges",
        "overview": "Spanning 100 acres of virgin forest on the Maharaja's Palace estate, Ananda offers world-acclaimed Ayurvedic programs, yoga amphitheaters, organic cuisine, and sweeping vistas of the sacred Ganges valley.",
        "amenities": ["🧘 Daily Yoga & Vedanta", "🏊 Heated Mountain Pool", "📶 WiFi", "🍳 Organic Ayurvedic Meals", "❄️ AC", "💆 24,000 sq ft Spa", "🏌️ 6-hole Golf"],
        "room_type": "Palace View Suite with Private Balcony",
        "max_guests": 2,
        "cancellation_policy": "Moderate cancellation policy (14 days advance)."
    },
    {
        "id": "hotel-snow-valley-manali",
        "title": "Snow Valley Alpine Resort",
        "type": "hotel",
        "category_label": "4★ Alpine Mountain Lodge",
        "destination": "Manali, Himachal Pradesh",
        "city": "Manali",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1518684079-3c830dcef090?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.75,
        "reviews_count": 1640,
        "is_superhost": False,
        "badge_text": "Snow Peak Balcony Views",
        "price_per_night_inr": 4800,
        "address": "Log Huts Area, Old Manali, Manali 175131",
        "proximity": "1.0 km to Hadimba Temple, 1.5 km to Mall Road",
        "overview": "Surrounded by pine trees and majestic deodar forests, this peaceful mountain resort offers heated timber rooms, private balconies facing snow-clad summits, and warm Himachali hospitality.",
        "amenities": ["🏔️ Mountain View Balcony", "📶 Free WiFi", "🍳 Buffet Breakfast", "🔥 Heating", "🍽️ Multi-cuisine Dining", "🎯 Recreation Room"],
        "room_type": "Presidential Pine Suite (Cedar Wood)",
        "max_guests": 3,
        "cancellation_policy": "Free cancellation up to 48 hours prior to check-in."
    },
    {
        "id": "hotel-park-hyatt-tokyo",
        "title": "Park Hyatt Tokyo",
        "type": "hotel",
        "category_label": "5★ Luxury Skyscraper Hotel",
        "destination": "Shinjuku, Tokyo",
        "city": "Tokyo",
        "country": "Japan",
        "image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.96,
        "reviews_count": 2840,
        "is_superhost": True,
        "badge_text": "Iconic Skyline Horizon",
        "price_per_night_inr": 48500,
        "address": "3-7-1-2 Nishi-Shinjuku, Shinjuku City, Tokyo 163-1055",
        "proximity": "Occupies top floors 39-52 of Shinjuku Park Tower with Mt. Fuji views",
        "overview": "An oasis of calm soaring high above Shinjuku. Renowned for its glass-atrium indoor pool, world-class New York Grill & Jazz Bar, and panoramic skyline vistas stretching to Mount Fuji on clear mornings.",
        "amenities": ["🏊 47th-Floor Glass Sky Pool", "📶 High-speed WiFi", "🍳 Gourmet Breakfast", "❄️ AC", "🍸 New York Jazz Bar", "🧖 Club on the Park Spa"],
        "room_type": "Park King View Room (Deep Soak Tub)",
        "max_guests": 2,
        "cancellation_policy": "Free cancellation up to 72 hours prior to arrival."
    },
    {
        "id": "hotel-plaza-athenee-paris",
        "title": "Hôtel Plaza Athénée",
        "type": "hotel",
        "category_label": "5★ Haute Couture Parisian Palace",
        "destination": "Avenue Montaigne, Paris",
        "city": "Paris",
        "country": "France",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.94,
        "reviews_count": 2310,
        "is_superhost": True,
        "badge_text": "Eiffel Tower Courtyard",
        "price_per_night_inr": 62000,
        "address": "25 Avenue Montaigne, 75008 Paris",
        "proximity": "Fashion epicenter, 0.8 km to Eiffel Tower, 0.5 km to Champs-Élysées",
        "overview": "The definition of Parisian glamour since 1913. Famous for its signature red geraniums, courtyard ice rink in winter, Dior Spa, and suites framing unobstructed views of the Eiffel Tower.",
        "amenities": ["🗼 Direct Eiffel Tower Views", "📶 High-speed WiFi", "🍳 Parisian Breakfast", "❄️ AC", "💄 Dior Spa", "🍷 Cellar Tasting Room"],
        "room_type": "Deluxe Room (Louis XVI Decor)",
        "max_guests": 2,
        "cancellation_policy": "Free cancellation up to 5 days prior to check-in."
    },

    # -------------------------------------------------------------------------
    # 2. AIRBNBS, VILLAS & PRIVATE HOMESTAYS
    # -------------------------------------------------------------------------
    {
        "id": "airbnb-saffron-villa-goa",
        "title": "SaffronStays Portuguese Heritage Villa",
        "type": "airbnb",
        "category_label": "Entire Airbnb Villa with Private Pool",
        "destination": "Assagao, North Goa",
        "city": "Goa",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1613490493576-7fde63acd811?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.98,
        "reviews_count": 340,
        "is_superhost": True,
        "badge_text": "Airbnb Superhost • Entire Villa",
        "price_per_night_inr": 19500,
        "address": "Badem Road, Assagao, Goa 403507",
        "proximity": "Nestled in trendy Assagao, 3 km to Vagator & Anjuna Beaches",
        "overview": "A meticulously restored 150-year-old Portuguese mansion. Boasts high wooden-rafter ceilings, antique oyster-shell windows, a private azure pool, lush tropical gardens, and a dedicated in-house chef.",
        "amenities": ["🏊 Private Swimming Pool", "👨‍🍳 In-house Private Chef", "📶 150Mbps WiFi", "🍳 Breakfast Included", "❄️ AC in all rooms", "☕ Fully Equipped Kitchen", "🚗 Free Private Parking"],
        "room_type": "Entire Villa • 4 Bedrooms • 4 Baths • 8 Beds",
        "max_guests": 8,
        "cancellation_policy": "Full refund up to 14 days before check-in."
    },
    {
        "id": "airbnb-kasauli-pinecone-chalet",
        "title": "The Pinecone Wood & Glass Chalet",
        "type": "airbnb",
        "category_label": "Airbnb Mountain Chalet with Panoramic Deck",
        "destination": "Kasauli Hills, Himachal Pradesh",
        "city": "Manali",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.93,
        "reviews_count": 420,
        "is_superhost": True,
        "badge_text": "Airbnb Guest Favorite",
        "price_per_night_inr": 8200,
        "address": "Upper Mall Forest Road, Kasauli, Himachal 173204",
        "proximity": "Perched on pine ridge, 1.8 km to Gilbert Nature Trail",
        "overview": "Floor-to-ceiling glass windows overlooking misty valleys and cedar forests. Features a wood-burning fireplace, star-gazing telescope, sun-drenched timber deck, and direct access to mountain walking trails.",
        "amenities": ["🏔️ 360° Valley Views", "🔥 Indoor Wood Fireplace", "📶 Starlink WiFi", "☕ Chef Kitchen", "🍳 Breakfast on Deck", "🔭 Telescope", "🐾 Pet Friendly"],
        "room_type": "Entire 2-Bedroom Alpine Chalet (Sleeps 5)",
        "max_guests": 5,
        "cancellation_policy": "Free cancellation up to 5 days before check-in."
    },
    {
        "id": "airbnb-jaipur-haveli-loft",
        "title": "Traditional Haveli Courtyard Loft",
        "type": "airbnb",
        "category_label": "Artisan Heritage Homestay",
        "destination": "Pink City, Jaipur",
        "city": "Jaipur",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.96,
        "reviews_count": 680,
        "is_superhost": True,
        "badge_text": "Airbnb Plus • Top 1%",
        "price_per_night_inr": 4900,
        "address": "Subhash Chowk, Pink City, Jaipur, Rajasthan 302002",
        "proximity": "Walking distance to Hawa Mahal (600m) and City Palace",
        "overview": "Live inside the walled city of Jaipur in this sun-drenched loft restored by local textile artisans. Includes private marble jharokha balcony, brass lanterns, hand-block printed linens, and rooftop chai evenings.",
        "amenities": ["🏰 Rooftop View of Nahargarh Fort", "📶 100Mbps WiFi", "❄️ AC", "☕ Espresso Machine", "🍳 Homemade Poha & Parathas", "🌿 Courtyard Garden"],
        "room_type": "Entire Loft Apartment • 1 Bed • 1 Bath",
        "max_guests": 3,
        "cancellation_policy": "Full refund up to 48 hours before check-in."
    },
    {
        "id": "airbnb-munnar-tea-bungalow",
        "title": "Munnar Mist Valley Colonial Tea Bungalow",
        "type": "airbnb",
        "category_label": "Historic Tea Plantation Estate",
        "destination": "Munnar Hills, Kerala",
        "city": "Munnar",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1596178065887-1198b6148b2b?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1596178065887-1198b6148b2b?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.92,
        "reviews_count": 310,
        "is_superhost": True,
        "badge_text": "Plantation Experience",
        "price_per_night_inr": 11500,
        "address": "Chithirapuram Estate, Munnar, Kerala 685565",
        "proximity": "Surrounded by 50 acres of rolling tea gardens and mist",
        "overview": "Original 1920s Scottish tea planter's bungalow with teak wood flooring and antique fireplaces. Enjoy estate walking tours, private tea tasting sessions, and traditional Kerala Sadhya cooked by your personal caretaker.",
        "amenities": ["🍃 50-Acre Tea Plantation Walk", "🔥 Fireplace", "📶 WiFi", "🍳 Traditional Kerala Breakfast", "☕ Fresh Estate Tea", "🚗 Free Parking"],
        "room_type": "Entire Bungalow • 3 Bedrooms • 6 Guests",
        "max_guests": 6,
        "cancellation_policy": "Free cancellation up to 7 days before check-in."
    },
    {
        "id": "airbnb-kyoto-machiya-house",
        "title": "Kyoto Traditional Machiya Townhouse",
        "type": "airbnb",
        "category_label": "Historic Wooden Townhouse with Zen Garden",
        "destination": "Gion, Kyoto",
        "city": "Tokyo",
        "country": "Japan",
        "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.97,
        "reviews_count": 520,
        "is_superhost": True,
        "badge_text": "Airbnb Superhost • Registered Machiya",
        "price_per_night_inr": 22000,
        "address": "Miyagawacho, Higashiyama Ward, Kyoto 605-0801",
        "proximity": "3 minutes walk to Gion Shirakawa stone bridge",
        "overview": "A registered century-old wooden Machiya preserved with Japanese cedar, tatami mats, shoji screens, and a serene private inner courtyard (Tsuboniwa) with a handcrafted Hinoki cypress soaking tub.",
        "amenities": ["🌿 Private Tsuboniwa Zen Garden", "🛁 Hinoki Cypress Bath Tub", "📶 Pocket WiFi included", "❄️ Climate AC/Heat", "🍵 Matcha Tea Set", "👘 Yukata Robes"],
        "room_type": "Entire House • 2 Bedrooms • Futons (Sleeps 4)",
        "max_guests": 4,
        "cancellation_policy": "Full refund up to 14 days before check-in."
    },
    {
        "id": "airbnb-paris-montmartre-loft",
        "title": "Montmartre Bohemian Artists Loft",
        "type": "airbnb",
        "category_label": "Sunlit Studio with Panoramic Paris Views",
        "destination": "Montmartre, Paris",
        "city": "Paris",
        "country": "France",
        "image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.91,
        "reviews_count": 790,
        "is_superhost": True,
        "badge_text": "Eiffel Skyline View",
        "price_per_night_inr": 13800,
        "address": "Rue des Saules, 75018 Paris",
        "proximity": "200m from Sacré-Cœur Basilica, near Rue Lepic bakeries",
        "overview": "Romantic top-floor artist studio perched on the hill of Montmartre. Features exposed oak beams, parquet floors, French balcony overlooking the rooftops of Paris, and a vinyl record collection.",
        "amenities": ["🗼 Distant Eiffel Views from Balcony", "📶 Fiber WiFi", "☕ Nespresso Machine", "🍳 Full Kitchenette", "🍷 Welcome French Wine", "🎵 Vintage Vinyl Player"],
        "room_type": "Entire Loft • 1 Queen Bed • 1 Bath",
        "max_guests": 2,
        "cancellation_policy": "Full refund up to 7 days before check-in."
    },
    {
        "id": "airbnb-ubud-bamboo-villa",
        "title": "Ubud River Sanctuary Eco Bamboo Villa",
        "type": "airbnb",
        "category_label": "Open-air Bamboo Architecture with Pool",
        "destination": "Ubud, Bali",
        "city": "Bali",
        "country": "Indonesia",
        "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.99,
        "reviews_count": 1120,
        "is_superhost": True,
        "badge_text": "Architectural Digest Featured",
        "price_per_night_inr": 16500,
        "address": "Banjar Sayan, Ubud, Gianyar, Bali 80571",
        "proximity": "Suspended over the sacred Ayung River valley in Ubud",
        "overview": "Masterpiece of sustainable bamboo engineering immersed in the jungle canopy. Features a private tear-drop infinity pool, open-air bedroom with river song lullabies, and floating morning breakfast trays.",
        "amenities": ["🏊 Private Jungle Infinity Pool", "🍳 Floating Tropical Breakfast", "📶 High-speed WiFi", "🛁 Natural Stone Tub", "🧘 Private Yoga Deck", "🛵 Scooter Rental"],
        "room_type": "Entire 2-Story Bamboo Villa • 1 King Bed",
        "max_guests": 2,
        "cancellation_policy": "Strict 14-day cancellation policy."
    },

    # -------------------------------------------------------------------------
    # 3. HOSTELS, BACKPACKER PODS & DHARAMSHALAS
    # -------------------------------------------------------------------------
    {
        "id": "hostel-zostel-rishikesh",
        "title": "Zostel Plus Rishikesh (Riverfront)",
        "type": "hostel",
        "category_label": "Riverfront Backpacker Hostel & Pods",
        "destination": "Tapovan, Rishikesh",
        "city": "Rishikesh",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.86,
        "reviews_count": 3120,
        "is_superhost": True,
        "badge_text": "Top Rated Backpacker Hostel",
        "price_per_night_inr": 1150,
        "address": "Badrinath Road, Tapovan, Rishikesh 249192",
        "proximity": "0.5 km to Lakshman Jhula, panoramic view of the Ganges",
        "overview": "India's favorite community hostel. Features private river-view pods, shared backpacker bunk dorms, an amphitheater for live acoustic nights, rooftop co-working space, and organized white-water rafting expeditions.",
        "amenities": ["📶 100Mbps Co-working WiFi", "☕ Rooftop Cafe & Bakery", "❄️ AC in Dorms", "🔒 Personal Lockers", "🎮 Common Room & Billiards", "🧗 Rafting & Trek Guides"],
        "room_type": "6-Bed Mixed AC Dorm Bed (Privacy Curtain + Reading Light)",
        "max_guests": 1,
        "cancellation_policy": "Free cancellation up to 24 hours prior to arrival."
    },
    {
        "id": "hostel-the-hosteller-goa",
        "title": "The Hosteller Goa (Anjuna Beach)",
        "type": "hostel",
        "category_label": "Poolside Social Backpacker Hostel",
        "destination": "Anjuna, North Goa",
        "city": "Goa",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.82,
        "reviews_count": 2840,
        "is_superhost": False,
        "badge_text": "Backpacker Social Hub",
        "price_per_night_inr": 850,
        "address": "Near Anjuna Flea Market, Anjuna, Goa 403509",
        "proximity": "600m to Anjuna Beach, 1.2 km to Curlies & Shiva Valley",
        "overview": "Bright yellow Portuguese-style villa converted into a buzzing traveler haven. Offers an outdoor swimming pool, open garden cafe, communal guitar sessions, foosball tournaments, and sunset beach walks.",
        "amenities": ["🏊 Backyard Swimming Pool", "📶 High-speed WiFi", "❄️ AC Dorms", "🔒 Lockers with RFID", "🛵 Scooter Rentals Onsite", "🍺 Social Bar & Cafe"],
        "room_type": "Standard 8-Bed Mixed Dorm (Bunk Bed)",
        "max_guests": 1,
        "cancellation_policy": "Free cancellation up to 24 hours before check-in."
    },
    {
        "id": "hostel-moustache-jaipur",
        "title": "Moustache Hostel Jaipur",
        "type": "hostel",
        "category_label": "Heritage Social Hostel with Fort Views",
        "destination": "M.I. Road, Jaipur",
        "city": "Jaipur",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.79,
        "reviews_count": 2490,
        "is_superhost": False,
        "badge_text": "Rooftop Pool & Fort Views",
        "price_per_night_inr": 750,
        "address": "Park Street, Near Ganpati Plaza, M.I. Road, Jaipur 302001",
        "proximity": "0.8 km from Jaipur Railway Station, 2.5 km to City Palace",
        "overview": "A vibrant blend of Rajasthani tradition and modern nomad perks. Features a rooftop splash pool overlooking the pink city horizon, communal Rajasthani thali dinners, walking tours, and quiet work pods.",
        "amenities": ["🏊 Rooftop Splash Pool", "📶 Fast WiFi", "❄️ AC Dorms & Privates", "🍛 Daily Thali Dinners", "🚶 Free Heritage Walking Tours"],
        "room_type": "6-Bed Deluxe Female / Mixed Dorm",
        "max_guests": 1,
        "cancellation_policy": "Free cancellation up to 24 hours before check-in."
    },
    {
        "id": "hostel-zostel-manali",
        "title": "Zostel Old Manali",
        "type": "hostel",
        "category_label": "Apple Orchard Backpacker Pods & Cafe",
        "destination": "Old Manali, Himachal Pradesh",
        "city": "Manali",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.88,
        "reviews_count": 2180,
        "is_superhost": True,
        "badge_text": "Bohemian Mountain Haven",
        "price_per_night_inr": 950,
        "address": "Manu Temple Road, Old Manali 175131",
        "proximity": "200m from historic Manu Temple, amid apple orchards",
        "overview": "A cozy timber-and-stone retreat nestled in peaceful Old Manali. Surrounded by apple trees, babbling mountain streams, and laid-back cafes. Excellent high-speed WiFi for digital nomads and trekkers.",
        "amenities": ["🍎 Apple Orchard Garden", "📶 100Mbps Nomad WiFi", "🔥 Evening Bonfires", "☕ The Garden Cafe", "🎸 Live Music Jam Room"],
        "room_type": "Cosy 6-Bed Mixed Dorm Bed",
        "max_guests": 1,
        "cancellation_policy": "Free cancellation up to 48 hours prior to arrival."
    },
    {
        "id": "hostel-gmvn-kedarnath",
        "title": "GMVN Tourist Rest House & Pilgrim Dormitory",
        "type": "hostel",
        "category_label": "Sacred Mountain Pilgrim Guest House & Dorms",
        "destination": "Kedarnath Dham, Uttarakhand",
        "city": "Kedarnath",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.70,
        "reviews_count": 1820,
        "is_superhost": False,
        "badge_text": "Official Shrine Board Partner",
        "price_per_night_inr": 650,
        "address": "Temple Path, Kedarnath Base, Rudraprayag, Uttarakhand 246445",
        "proximity": "350 meters from Kedarnath Jyotirlinga Temple",
        "overview": "Official Garhwal Mandal Vikas Nigam (GMVN) pilgrim rest house situated near the holy Kedarnath temple. Provides clean beds, heavy thermal blankets for mountain nights, hot water, and pure vegetarian satvik meals.",
        "amenities": ["🛕 3-Min Walk to Temple", "🛏️ Heavy Woolen Blankets", "🚿 Hot Water Facility", "🍲 Satvik Prasad Dining", "🩺 First Aid & Oxygen"],
        "room_type": "Pilgrim Bunker Bed (Thermal Quilts)",
        "max_guests": 1,
        "cancellation_policy": "Standard pilgrimage cancellation rules apply."
    },
    {
        "id": "hostel-ayodhya-teerth-dharamshala",
        "title": "Shree Ram Janmabhoomi Teerth Guest House",
        "type": "hostel",
        "category_label": "Clean Spiritual Pilgrim Dharamshala",
        "destination": "Ayodhya Dham, Uttar Pradesh",
        "city": "Ayodhya",
        "country": "India",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=80",
        "gallery": [
            "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=80"
        ],
        "rating": 4.85,
        "reviews_count": 1540,
        "is_superhost": True,
        "badge_text": "Divine & Peaceful",
        "price_per_night_inr": 800,
        "address": "Ram Kot, Near Hanumangarhi, Ayodhya 224123",
        "proximity": "0.5 km to Shree Ram Janmabhoomi Mandir & Saryu Ghat",
        "overview": "A clean, modern, and spiritually uplifting pilgrim rest house. Offers air-cooled rooms, clean attached bathrooms, drinking RO water, safe luggage storage for darshan, and morning bhajan gatherings.",
        "amenities": ["🕉️ Darshan Assistance", "❄️ Air-Cooled / AC Rooms", "💧 Pure RO Water", "🧳 Luggage Storage for Temple", "🍲 Pure Vegetarian Bhojanalaya"],
        "room_type": "Family Pilgrim Room (Twin Beds)",
        "max_guests": 2,
        "cancellation_policy": "Free cancellation up to 24 hours prior to darshan."
    }
]


def get_all_stays(
    query: Optional[str] = None,
    lodging_type: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    amenity: Optional[str] = None,
    sort_by: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Filter and sort stays from catalog based on user criteria."""
    results = list(STAYS_CATALOG)

    if query:
        q = query.lower().strip()
        results = [
            s for s in results
            if q in s["title"].lower()
            or q in s["destination"].lower()
            or q in s["city"].lower()
            or q in s["country"].lower()
            or q in s.get("overview", "").lower()
            or any(q in a.lower() for a in s.get("amenities", []))
        ]

    if lodging_type and lodging_type.lower() != "all":
        t = lodging_type.lower()
        results = [s for s in results if s["type"].lower() == t]

    if min_price is not None and min_price > 0:
        results = [s for s in results if s["price_per_night_inr"] >= min_price]

    if max_price is not None and max_price > 0:
        results = [s for s in results if s["price_per_night_inr"] <= max_price]

    if amenity and amenity.lower() != "all":
        a_clean = amenity.lower().strip()
        results = [s for s in results if any(a_clean in a.lower() for a in s.get("amenities", []))]

    # Sorting
    if sort_by == "rating":
        results.sort(key=lambda s: s.get("rating", 0), reverse=True)
    elif sort_by == "price_asc":
        results.sort(key=lambda s: s.get("price_per_night_inr", 0))
    elif sort_by == "price_desc":
        results.sort(key=lambda s: s.get("price_per_night_inr", 0), reverse=True)
    elif sort_by == "reviews":
        results.sort(key=lambda s: s.get("reviews_count", 0), reverse=True)

    return results


def get_stay_by_id(stay_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve single stay metadata by unique ID."""
    for s in STAYS_CATALOG:
        if s["id"] == stay_id:
            return s
    return None


def book_stay_instant(
    stay_id: str,
    guest_name: str,
    guest_email: str,
    check_in: str,
    check_out: str,
    guests_count: int = 1,
    rooms_count: int = 1
) -> Dict[str, Any]:
    """Generate instant simulated reservation voucher for a stay."""
    stay = get_stay_by_id(stay_id)
    if not stay:
        raise ValueError("Stay not found")

    try:
        ci = datetime.strptime(check_in, "%Y-%m-%d").date()
        co = datetime.strptime(check_out, "%Y-%m-%d").date()
        nights = max(1, (co - ci).days)
    except Exception:
        ci = date.today() + timedelta(days=7)
        co = ci + timedelta(days=2)
        nights = 2

    price_per_night = stay["price_per_night_inr"]
    subtotal = price_per_night * nights * max(1, rooms_count)
    taxes = round(subtotal * 0.12, 2)  # 12% GST
    total_amount = round(subtotal + taxes, 2)

    voucher_code = f"TP-{uuid.uuid4().hex[:8].upper()}"

    return {
        "status": "confirmed",
        "voucher_code": voucher_code,
        "stay_id": stay["id"],
        "stay_title": stay["title"],
        "stay_type": stay["type"],
        "category_label": stay["category_label"],
        "destination": stay["destination"],
        "address": stay["address"],
        "guest_name": guest_name or "Valued Traveler",
        "guest_email": guest_email or "traveler@example.com",
        "check_in": ci.isoformat(),
        "check_out": co.isoformat(),
        "nights": nights,
        "guests_count": max(1, guests_count),
        "rooms_count": max(1, rooms_count),
        "currency": "INR",
        "price_per_night": price_per_night,
        "subtotal": subtotal,
        "taxes": taxes,
        "total_amount": total_amount,
        "booked_at": datetime.utcnow().isoformat(),
        "cancellation_policy": stay.get("cancellation_policy", "Standard cancellation"),
        "host_contact": "+91 (0) 800-PACE-STAY",
        "check_in_time": "02:00 PM",
        "check_out_time": "11:00 AM"
    }


def add_stay_to_trip_booking(
    db: Session,
    trip_id: int,
    stay_id: str,
    check_in: str,
    check_out: str,
    guests_count: int = 1
) -> Dict[str, Any]:
    """Attach this stay reservation as an official expense and lodging record in the active trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise ValueError(f"Trip with ID {trip_id} not found")

    stay = get_stay_by_id(stay_id)
    if not stay:
        raise ValueError(f"Stay with ID {stay_id} not found")

    try:
        ci = datetime.strptime(check_in, "%Y-%m-%d").date()
        co = datetime.strptime(check_out, "%Y-%m-%d").date()
        nights = max(1, (co - ci).days)
    except Exception:
        ci = datetime.strptime(trip.start_date, "%Y-%m-%d").date() if trip.start_date else date.today()
        co = ci + timedelta(days=min(3, trip.days_count))
        nights = max(1, (co - ci).days)

    total_cost = round(stay["price_per_night_inr"] * nights, 2)

    # 1. Create Accommodation Expense
    new_expense = Expense(
        trip_id=trip.id,
        title=f"Lodging: {stay['title']} ({stay['category_label']})",
        amount=total_cost,
        category="Accommodation",
        date=ci.isoformat(),
        notes=f"Reserved for {nights} night(s) in {stay['destination']}. Proximity: {stay['proximity']}."
    )
    db.add(new_expense)

    # 2. Update trip notes if not already noted
    booking_note = f"\n[Confirmed Stay: {stay['title']} ({nights} nights, ₹{total_cost:,})]"
    if booking_note not in (trip.notes or ""):
        trip.notes = ((trip.notes or "") + booking_note).strip()

    db.commit()
    db.refresh(new_expense)

    return {
        "message": f"Added {stay['title']} to trip '{trip.title}'",
        "expense_id": new_expense.id,
        "trip_id": trip.id,
        "total_cost": total_cost,
        "nights": nights,
        "stay": stay
    }
