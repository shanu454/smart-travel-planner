"""Local Travel Guides Directory and Direct Connection Service.

Provides verified tour guides, spiritual scholars, trekking sherpas, and heritage
experts with direct contact channels (Live Chat, WhatsApp, Phone, Booking Inquiries).
"""
from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime

GUIDES_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "guide_varanasi_acharya",
        "name": "Pt. Rameshwar Shastri",
        "title": "Vedic Scholar & Chief Ghat Historian",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
        "destination": "Varanasi",
        "country": "India",
        "region": "Spiritual & Pilgrimage",
        "experience_years": 16,
        "rating": 4.98,
        "reviews_count": 384,
        "accreditation": "Ministry of Tourism Certified • Kashi Vishwanath Trust Recognized",
        "badge": "Top Spiritual Scholar 🕉️",
        "specialties": ["Ganga Aarti VIP Darshan", "Ancient Ghats Walking Tour", "Kashi Vishwanath Temple History", "Sunrise Vedic Boat Excursion"],
        "languages": ["Hindi", "English", "Sanskrit"],
        "rate_per_day": 2400,
        "rate_per_hour": 450,
        "direct_phone": "+91 98391 24580",
        "direct_whatsapp": "+919839124580",
        "direct_email": "rameshwar.shastri@travelpace.com",
        "bio": "Born and raised along the Manikarnika and Dashashwamedh Ghats. For over 16 years, I have guided spiritual seekers, historians, and pilgrims through the mystical sacred geography and rituals of the world's oldest living city.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Sacred Dawn Boat & Ghats Heritage Walk",
                "duration": "3 Hours",
                "price": 1200,
                "included": ["Subah-e-Banaras Boat Ride", "Assi to Dashashwamedh Ghat walk", "Morning tea & kachori tasting", "Temple lore explanation"]
            },
            {
                "title": "Complete Kashi Darshan & Evening Maha Aarti VIP",
                "duration": "Full Day (7 Hours)",
                "price": 2400,
                "included": ["Kashi Vishwanath Corridor guidance", "Sankat Mochan & BHU Darshan", "Reserved boat view for evening Aarti", "Spiritual discourse"]
            }
        ]
    },
    {
        "id": "guide_kedarnath_sherpa",
        "name": "Tenzing Negi",
        "title": "Senior Himalayan Trekking Sherpa & Char Dham Guide",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
        "destination": "Kedarnath & Badrinath",
        "country": "India",
        "region": "Spiritual & Pilgrimage",
        "experience_years": 14,
        "rating": 4.99,
        "reviews_count": 426,
        "accreditation": "IMF Certified Mountaineer • Uttarakhand Tourism Licensed",
        "badge": "High Altitude Sherpa 🏔️",
        "specialties": ["Gaurikund to Kedarnath Trek", "Badrinath & Mana Border Exploration", "Altitude Acclimatization", "Helicopter & Pony Logistics"],
        "languages": ["Hindi", "Garhwali", "English"],
        "rate_per_day": 3200,
        "rate_per_hour": 550,
        "direct_phone": "+91 94120 78310",
        "direct_whatsapp": "+919412078310",
        "direct_email": "tenzing.negi@travelpace.com",
        "bio": "Certified high-altitude trekker with 14 seasons on the Garhwal Himalayas. I prioritize traveler safety, weather timing, high-altitude hydration, and seamless temple darshan coordination for families and solo pilgrims.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Kedarnath Guided Ascent & Temple Escort",
                "duration": "2 Days / 1 Night",
                "price": 4500,
                "included": ["Pacing support on 16km trek", "Emergency first aid & oxygen kit", "Temple queue coordination", "Bhairavnath temple visit"]
            },
            {
                "title": "Badrinath, Mana Village & Vasudhara Falls Day Tour",
                "duration": "Full Day (8 Hours)",
                "price": 2800,
                "included": ["Badrinath Temple Darshan", "Tapt Kund holy dip assistance", "India's last village Mana exploration", "Vyasa Gufa & Saraswati river origin"]
            }
        ]
    },
    {
        "id": "guide_jaipur_heritage",
        "name": "Bhawani Singh Rathore",
        "title": "Royal Rajasthan Historian & Palace Curator",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "destination": "Jaipur",
        "country": "India",
        "region": "Cultural & Heritage",
        "experience_years": 12,
        "rating": 4.96,
        "reviews_count": 295,
        "accreditation": "ASI Certified • Rajasthan Department of Tourism Licensed",
        "badge": "Master Historian 🏰",
        "specialties": ["Amber Fort Secret Passages", "City Palace Royal Galleries", "Jantar Mantar Astronomical Science", "Bazaar Gem & Textile Walk"],
        "languages": ["Hindi", "English", "Rajasthani", "French"],
        "rate_per_day": 2200,
        "rate_per_hour": 400,
        "direct_phone": "+91 98290 61420",
        "direct_whatsapp": "+919829061420",
        "direct_email": "bhawani.rathore@travelpace.com",
        "bio": "Direct descendant of Rajput court chroniclers. I bring the architecture, astronomical genius of Sawai Jai Singh, and forgotten royal legends of the Pink City to life with infectious energy and insider access.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Majestic Forts & Royal Palaces Odyssey",
                "duration": "Full Day (8 Hours)",
                "price": 2400,
                "included": ["Amber Fort guided tour with hidden chambers", "Nahargarh panoramic sunset overlook", "Hawa Mahal photo viewpoints", "City Palace museum lore"]
            },
            {
                "title": "Walled Pink City Bazaars & Culinary Walk",
                "duration": "3.5 Hours",
                "price": 1400,
                "included": ["Johari & Bapu Bazaar spice & craft secrets", "Lassi & Pyaz Kachori tastings", "Heritage havelis architecture tour"]
            }
        ]
    },
    {
        "id": "guide_goa_watersports",
        "name": "Capt. Mario D'Souza",
        "title": "Coastal Marine Guide & Latin Quarter Explorer",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "destination": "Goa",
        "country": "India",
        "region": "Relaxation & Beach",
        "experience_years": 10,
        "rating": 4.94,
        "reviews_count": 260,
        "accreditation": "Goa Tourism Development Corp (GTDC) Certified Marine Skipper",
        "badge": "Coastal Explorer 🏖️",
        "specialties": ["Fontainhas Latin Quarter Heritage Walk", "Dolphin & Island Backwater Kayaking", "South Goa Hidden Coves", "Goan Portuguese Culinary Trail"],
        "languages": ["English", "Konkani", "Hindi", "Portuguese"],
        "rate_per_day": 2000,
        "rate_per_hour": 380,
        "direct_phone": "+91 98221 45900",
        "direct_whatsapp": "+919822145900",
        "direct_email": "mario.dsouza@travelpace.com",
        "bio": "Lifelong Panaji resident and licensed marine adventurer. I show travelers the soul of Goa beyond ordinary tourist traps—charming Portuguese heritage homes, pristine secluded beaches, and authentic Konkani seafood joints.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Fontainhas Latin Quarter & Portuguese Heritage Walk",
                "duration": "2.5 Hours",
                "price": 1100,
                "included": ["Colourful colonial alleyways", "Historical bakeries & bebinca tasting", "Old chapel stories", "Photography assistance"]
            },
            {
                "title": "Wild South Goa & Cola Lagoon Expedition",
                "duration": "Full Day (7 Hours)",
                "price": 2200,
                "included": ["Cabo de Rama Fort cliff views", "Freshwater Cola lagoon exploration", "Secret Butterfly Beach boat ride"]
            }
        ]
    },
    {
        "id": "guide_manali_mountains",
        "name": "Kishan Thakur",
        "title": "Himachal Alpine Naturalist & Adventure Guide",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
        "destination": "Manali",
        "country": "India",
        "region": "Adventure & Mountain",
        "experience_years": 11,
        "rating": 4.97,
        "reviews_count": 310,
        "accreditation": "Atal Bihari Vajpayee Institute of Mountaineering Certified",
        "badge": "Mountain Guide 🏔️",
        "specialties": ["Solang Valley & Rohtang Pass Adventures", "Old Manali Cedar Forest Trails", "Jogini Waterfall Hike", "Traditional Kathkuni Architecture"],
        "languages": ["Hindi", "English", "Pahari"],
        "rate_per_day": 2200,
        "rate_per_hour": 400,
        "direct_phone": "+91 98160 33450",
        "direct_whatsapp": "+919816033450",
        "direct_email": "kishan.thakur@travelpace.com",
        "bio": "Born in Naggar village near Manali. I specialize in snow trekking, secret cedar forest viewpoints, and guiding families safely through Solang and Rohtang with zero stress and unforgettable Himalayan vistas.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Jogini Waterfall & Vashisht Hot Springs Trek",
                "duration": "4 Hours",
                "price": 1200,
                "included": ["Pine forest ridge walk", "Scenic Jogini waterfall cascades", "Vashisht hot sulphur spring dip", "Local apple tea"]
            },
            {
                "title": "Rohtang Pass & Atal Tunnel High Snow Day",
                "duration": "Full Day (8 Hours)",
                "price": 2500,
                "included": ["Rohtang Pass scenic permit guidance", "Atal Tunnel Lahaul valley crossing", "Snow point adventure assistance"]
            }
        ]
    },
    {
        "id": "guide_rishikesh_yoga",
        "name": "Acharya Devrat",
        "title": "Spiritual Master, Yoga Teacher & Ganga Guide",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "destination": "Rishikesh",
        "country": "India",
        "region": "Spiritual & Pilgrimage",
        "experience_years": 13,
        "rating": 4.98,
        "reviews_count": 275,
        "accreditation": "Yoga Alliance Certified RYT-500 • Shivananda Ashram Scholar",
        "badge": "Yoga & Ganga Guide 🧘",
        "specialties": ["Triveni Ghat Evening Aarti", "Beatles Ashram Hidden Murals", "Morning Ganga Sunrise Meditation", "Neer Garh Waterfall Hike"],
        "languages": ["Hindi", "English", "Sanskrit"],
        "rate_per_day": 2000,
        "rate_per_hour": 380,
        "direct_phone": "+91 97580 12890",
        "direct_whatsapp": "+919758012890",
        "direct_email": "acharya.devrat@travelpace.com",
        "bio": "Rishikesh native and lifelong spiritual practitioner. I help travelers discover the true serenity of the Himalayas through authentic sunrise pranayama, secluded river beaches, and the profound wisdom of Parmarth and Beatles Ashram.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Beatles Ashram & Tapovan Spiritual Trail",
                "duration": "3 Hours",
                "price": 1100,
                "included": ["Beatles meditation cave exploration", "Graffiti hall stories", "Ram Jhula suspension bridge lore", "Herbal chai"]
            },
            {
                "title": "Sunrise Meditation & Triveni Ghat Aarti Ceremony",
                "duration": "Full Day (6 Hours)",
                "price": 2100,
                "included": ["Dawn breathwork session by holy Ganga", "Vashistha Cave quiet visit", "Evening Aarti VIP lamp offering"]
            }
        ]
    },
    {
        "id": "guide_ayodhya_ramayana",
        "name": "Dr. Virendra Tripathi",
        "title": "Ayodhya Heritage Historian & Ramayana Scholar",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "destination": "Ayodhya",
        "country": "India",
        "region": "Spiritual & Pilgrimage",
        "experience_years": 18,
        "rating": 4.99,
        "reviews_count": 412,
        "accreditation": "Ph.D. Ancient Indian History • UP Tourism Approved",
        "badge": "Ram Mandir Specialist 🛕",
        "specialties": ["Ram Janmabhoomi Mandir Darshan Guidance", "Hanuman Garhi VIP Entry", "Sarayu River Evening Aarti & Cruise", "Kanak Bhawan Royal Lore"],
        "languages": ["Hindi", "English", "Awadhi", "Sanskrit"],
        "rate_per_day": 2400,
        "rate_per_hour": 450,
        "direct_phone": "+91 94500 89210",
        "direct_whatsapp": "+919450089210",
        "direct_email": "virendra.tripathi@travelpace.com",
        "bio": "Dedicated 18 years to the preservation and storytelling of sacred Ayodhya. I provide orderly, comfortable temple darshan pathways and deep architectural narratives of the new grand Ram Mandir and historical ghats.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Complete Ram Janmabhoomi & Hanuman Garhi Darshan",
                "duration": "4.5 Hours",
                "price": 1400,
                "included": ["Seamless security navigation", "Detailed temple architecture narrative", "Hanuman Garhi blessing", "Prasad offering"]
            },
            {
                "title": "Sacred Ayodhya Circuit & Sarayu Ghats Twilight Tour",
                "duration": "Full Day (7 Hours)",
                "price": 2400,
                "included": ["Kanak Bhawan & Dashrath Mahal", "Guptar Ghat historical excursion", "Sarayu River sunset cruise", "Maha Aarti at Ram Ki Paidi"]
            }
        ]
    },
    {
        "id": "guide_udaipur_palaces",
        "name": "Chandraveer Singh Mewar",
        "title": "Mewar Royalty & Lake Heritage Chronicler",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
        "destination": "Udaipur",
        "country": "India",
        "region": "Cultural & Heritage",
        "experience_years": 15,
        "rating": 4.97,
        "reviews_count": 334,
        "accreditation": "Mewar Trust Scholar • Govt of Rajasthan Heritage License",
        "badge": "Lake City Chronicler ✨",
        "specialties": ["City Palace Private Quarters", "Lake Pichola Sunset Yacht Commentary", "Jagdish Temple Stone Carvings", "Bagore Ki Haveli Folk Arts"],
        "languages": ["Hindi", "English", "German"],
        "rate_per_day": 2300,
        "rate_per_hour": 420,
        "direct_phone": "+91 98291 90870",
        "direct_whatsapp": "+919829190870",
        "direct_email": "chandraveer.mewar@travelpace.com",
        "bio": "Deeply versed in 1,400 years of unbroken Mewar chivalry and romantic architecture. I ensure travelers discover Udaipur's hidden frescoes, intimate rooftop lookouts, and regal hospitality with aristocratic grace.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "City Palace Complex & Zenana Mahal Deep Dive",
                "duration": "3 Hours",
                "price": 1300,
                "included": ["Curator level commentary", "Crystal gallery lore", "Peacock courtyard photography tips"]
            },
            {
                "title": "Romantic Lakes, Saheliyon Ki Bari & Sunset Overlook",
                "duration": "Full Day (7 Hours)",
                "price": 2300,
                "included": ["Monsoon Palace Sajjangarh vista", "Lake Pichola private boat coordination", "Evening Dharohar dance show escort"]
            }
        ]
    },
    {
        "id": "guide_tokyo_cultural",
        "name": "Kenji Takahashi",
        "title": "Tokyo Certified Bilingual Cultural Scholar",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "destination": "Tokyo",
        "country": "Japan",
        "region": "World - East Asia",
        "experience_years": 9,
        "rating": 4.98,
        "reviews_count": 320,
        "accreditation": "Japan National Tourism Organization (JNTO) Licensed Guide-Interpreter",
        "badge": "Tokyo Master Guide 🗾",
        "specialties": ["Asakusa Senso-ji & Shinto Traditions", "Tsukiji Outer Market Culinary Walk", "Akihabara Subculture Secrets", "Shibuya & Shinjuku Neon Night Walk"],
        "languages": ["Japanese", "English"],
        "rate_per_day": 8500,
        "rate_per_hour": 1400,
        "direct_phone": "+81 90 4421 8890",
        "direct_whatsapp": "+819044218890",
        "direct_email": "kenji.takahashi@travelpace.com",
        "bio": "Former university lecturer in Edo history and licensed national tour guide. I seamlessly bridge the divide between ancient samurai traditions in Asakusa and Tokyo's cutting-edge anime and culinary culture.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Old Edo to Neo Tokyo: Asakusa & Akihabara",
                "duration": "4 Hours",
                "price": 4800,
                "included": ["Senso-ji fortune reading etiquette", "Nakamise snack tastings", "Akihabara retro tech alleys", "Tokyo Metro navigation coaching"]
            },
            {
                "title": "Ultimate Tokyo Highlights & Tsukiji Food Tour",
                "duration": "Full Day (8 Hours)",
                "price": 8500,
                "included": ["Tsukiji sushi & wagyu skewer tastings", "Meiji Shrine serene forest walk", "Shibuya Crossing panoramic lookout", "Customized subway route guide"]
            }
        ]
    },
    {
        "id": "guide_paris_docent",
        "name": "Claire Delacroix",
        "title": "Louvre Art Docent & Parisian Historian",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "destination": "Paris",
        "country": "France",
        "region": "World - Western Europe",
        "experience_years": 11,
        "rating": 4.97,
        "reviews_count": 348,
        "accreditation": "French Ministry of Culture Certified Guide-Conférencier",
        "badge": "Paris Art Docent 🗼",
        "specialties": ["Louvre Museum Masterpieces Without Lines", "Montmartre Bohemian Artists Walk", "Latin Quarter Hidden Courtyards", "Boutique Pâtisserie & Wine Tasting"],
        "languages": ["French", "English", "Spanish"],
        "rate_per_day": 9200,
        "rate_per_hour": 1600,
        "direct_phone": "+33 6 12 34 56 78",
        "direct_whatsapp": "+33612345678",
        "direct_email": "claire.delacroix@travelpace.com",
        "bio": "Art history graduate from Sorbonne University with 11 years as an official French guide-conférencier. I unlock the hidden secrets behind the Mona Lisa, Haussmann's grand boulevards, and Montmartre's romantic cobblestones.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Skip-the-Line Louvre Museum Highlights",
                "duration": "2.5 Hours",
                "price": 5200,
                "included": ["Curated walkthrough of top 10 masterworks", "Crowd-avoidance routes", "Vivid historical context"]
            },
            {
                "title": "Montmartre Bohemian Village & Eiffel Twilight",
                "duration": "Full Day (7 Hours)",
                "price": 9200,
                "included": ["Sacré-Cœur panorama", "Picasso & Van Gogh studios", "Seine river promenade", "Trocadéro sparkling Eiffel view"]
            }
        ]
    },
    {
        "id": "guide_rome_archaeologist",
        "name": "Marco Bellini",
        "title": "Classical Archaeologist & Colosseum Specialist",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
        "destination": "Rome",
        "country": "Italy",
        "region": "World - Southern Europe",
        "experience_years": 14,
        "rating": 4.98,
        "reviews_count": 390,
        "accreditation": "Licensed Guide of the City of Rome • Vatican Museums Authorized",
        "badge": "Roman Archaeologist 🏛️",
        "specialties": ["Colosseum Arena Floor & Underground", "Roman Forum & Palatine Hill Lore", "Vatican City & Sistine Chapel Secrets", "Trastevere Authentic Roman Cuisine"],
        "languages": ["Italian", "English"],
        "rate_per_day": 8800,
        "rate_per_hour": 1500,
        "direct_phone": "+39 340 987 6543",
        "direct_whatsapp": "+393409876543",
        "direct_email": "marco.bellini@travelpace.com",
        "bio": "Trained classical archaeologist who has worked on excavations in the Imperial Fora. I bring the stones of ancient Rome back to vivid life, separating Hollywood fiction from gladiatorial and senatorial reality.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Gladiators & Emperors: Colosseum & Forum",
                "duration": "3 Hours",
                "price": 4900,
                "included": ["Gladiator arena reconstruction", "Julius Caesar's altar", "Palatine Hill imperial residences"]
            },
            {
                "title": "Full Day Rome of the Caesars & Popes",
                "duration": "Full Day (8 Hours)",
                "price": 8800,
                "included": ["Pantheon architectural engineering", "Trevi Fountain & Piazza Navona", "St. Peter's Basilica skip-the-line escort"]
            }
        ]
    },
    {
        "id": "guide_cairo_egyptologist",
        "name": "Dr. Tarek El-Masry",
        "title": "Egyptologist & Giza Pyramids Master Guide",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "cover_image": "https://images.unsplash.com/photo-1572252009286-268acec5ca0a?auto=format&fit=crop&w=1200&q=80",
        "destination": "Cairo",
        "country": "Egypt",
        "region": "World - North Africa",
        "experience_years": 17,
        "rating": 4.99,
        "reviews_count": 450,
        "accreditation": "Egyptian General Tourist Guides Syndicate (EGTGS) Licensed Egyptologist",
        "badge": "Pharaonic Egyptologist 🏺",
        "specialties": ["Giza Plateau & Great Sphinx Secrets", "Grand Egyptian Museum (GEM) Royal Treasures", "Saqqara Step Pyramid & Tombs", "Khan el-Khalili Bazaar Navigation"],
        "languages": ["Arabic", "English", "French"],
        "rate_per_day": 7200,
        "rate_per_hour": 1200,
        "direct_phone": "+20 100 123 4567",
        "direct_whatsapp": "+201001234567",
        "direct_email": "tarek.masry@travelpace.com",
        "bio": "Ph.D. in Pharaonic Archaeology from Cairo University. I protect travelers from hawkers while deciphering 4,500-year-old hieroglyphs, pyramid construction mysteries, and Tutankhamun's gold treasures.",
        "verified": True,
        "online_status": "Online Now",
        "sample_tours": [
            {
                "title": "Wonders of Giza: Great Pyramid & Sphinx Revealed",
                "duration": "4 Hours",
                "price": 4000,
                "included": ["Panoramic pyramid photo viewpoints", "Sphinx paw causeway lore", "Camel caravan coordination without scams", "Hieroglyphic reading lesson"]
            },
            {
                "title": "Complete Pharaonic Day: Giza, Saqqara & Museum",
                "duration": "Full Day (8 Hours)",
                "price": 7200,
                "included": ["King Djoser Step Pyramid", "Grand Egyptian Museum highlights", "Traditional Egyptian koshari lunch escort"]
            }
        ]
    }
]

# Simulated in-memory store for submitted guide booking inquiries
GUIDE_INQUIRIES: List[Dict[str, Any]] = []


def get_all_guides(
    query: Optional[str] = None,
    destination: Optional[str] = None,
    region: Optional[str] = None,
    language: Optional[str] = None,
    specialty: Optional[str] = None,
    sort_by: Optional[str] = "rating"
) -> List[Dict[str, Any]]:
    """Retrieve catalog of guides with dynamic search, destination, and filter rules."""
    results = list(GUIDES_CATALOG)

    if query:
        q = query.lower().strip()
        results = [
            g for g in results
            if q in g["name"].lower()
            or q in g["destination"].lower()
            or q in g["country"].lower()
            or q in g["title"].lower()
            or any(q in s.lower() for s in g["specialties"])
            or any(q in l.lower() for l in g["languages"])
            or q in g["bio"].lower()
        ]

    if destination and destination.lower() != "all":
        d = destination.lower().strip()
        results = [
            g for g in results
            if d in g["destination"].lower()
            or d in g["country"].lower()
        ]

    if region and region.lower() != "all":
        r = region.lower().strip()
        results = [g for g in results if r in g.get("region", "").lower()]

    if language and language.lower() != "all":
        l_req = language.lower().strip()
        results = [g for g in results if any(l_req in lang.lower() for lang in g["languages"])]

    if specialty and specialty.lower() != "all":
        s_req = specialty.lower().strip()
        results = [g for g in results if any(s_req in s.lower() for s in g["specialties"])]

    # Sorting
    if sort_by == "rating":
        results.sort(key=lambda x: (x.get("rating", 0), x.get("reviews_count", 0)), reverse=True)
    elif sort_by == "price_asc":
        results.sort(key=lambda x: x.get("rate_per_day", 0))
    elif sort_by == "price_desc":
        results.sort(key=lambda x: x.get("rate_per_day", 0), reverse=True)
    elif sort_by == "experience":
        results.sort(key=lambda x: x.get("experience_years", 0), reverse=True)
    elif sort_by == "reviews":
        results.sort(key=lambda x: x.get("reviews_count", 0), reverse=True)

    return results


def get_guide_by_id(guide_id: str) -> Optional[Dict[str, Any]]:
    """Look up a specific guide profile by ID."""
    for g in GUIDES_CATALOG:
        if g["id"] == guide_id:
            return g
    return None


def get_guides_for_destination(destination: str, limit: int = 4) -> List[Dict[str, Any]]:
    """Find top recommended guides matching a specific destination name."""
    d_clean = destination.lower().strip()
    matches = []
    for g in GUIDES_CATALOG:
        g_dest = g["destination"].lower()
        g_country = g["country"].lower()
        if d_clean in g_dest or g_dest in d_clean or d_clean in g_country:
            matches.append(g)

    # Fallback to top rated if no exact match
    if not matches:
        matches = sorted(GUIDES_CATALOG, key=lambda x: x["rating"], reverse=True)[:limit]
    return matches[:limit]


def create_guide_inquiry(guide_id: str, inquiry_data: Dict[str, Any]) -> Dict[str, Any]:
    """Process customer's direct booking inquiry and return confirmed voucher."""
    guide = get_guide_by_id(guide_id)
    if not guide:
        raise ValueError(f"Guide with ID {guide_id} does not exist.")

    inquiry_code = f"TPG-{uuid.uuid4().hex[:7].upper()}"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    tour_date = inquiry_data.get("tour_date", datetime.now().strftime("%Y-%m-%d"))
    group_size = int(inquiry_data.get("group_size", 1))
    duration_type = inquiry_data.get("duration_type", "full_day")  # full_day, half_day, custom
    client_name = inquiry_data.get("client_name", "Valued Traveler")
    client_email = inquiry_data.get("client_email", "traveler@example.com")
    client_phone = inquiry_data.get("client_phone", "")
    special_notes = inquiry_data.get("special_notes", "")

    # Calculate estimated fee
    base_rate = guide["rate_per_day"] if duration_type == "full_day" else int(guide["rate_per_day"] * 0.6)
    if group_size > 4:
        base_rate += int(base_rate * 0.25)  # Group supplement

    voucher = {
        "voucher_id": inquiry_code,
        "status": "Inquiry Confirmed & Dispatched",
        "created_at": now_str,
        "guide": {
            "id": guide["id"],
            "name": guide["name"],
            "title": guide["title"],
            "avatar": guide["avatar"],
            "destination": guide["destination"],
            "accreditation": guide["accreditation"],
            "direct_phone": guide["direct_phone"],
            "direct_whatsapp": guide["direct_whatsapp"],
            "direct_email": guide["direct_email"]
        },
        "booking_details": {
            "client_name": client_name,
            "client_email": client_email,
            "client_phone": client_phone,
            "tour_date": tour_date,
            "group_size": group_size,
            "duration_type": "Full Day (6-8 Hours)" if duration_type == "full_day" else "Half Day (3-4 Hours)",
            "special_notes": special_notes,
            "estimated_fee": base_rate,
            "currency": "INR"
        },
        "direct_connect": {
            "whatsapp_url": f"https://wa.me/{guide['direct_whatsapp'].replace('+', '').replace(' ', '')}?text=Hello%20{guide['name'].replace(' ', '%20')},%20my%20Travel%20Pace%20guide%20voucher%20is%20{inquiry_code}%20for%20{tour_date}.%20I%20would%20like%20to%20confirm%20our%20tour!",
            "phone_call": f"tel:{guide['direct_phone'].replace(' ', '')}",
            "response_time": "Within 15 minutes"
        }
    }

    GUIDE_INQUIRIES.append(voucher)
    return voucher


def generate_guide_chat_reply(guide_id: str, message: str, traveler_name: str = "Traveler") -> Dict[str, Any]:
    """Generate realistic, contextual, and helpful direct responses from the guide."""
    guide = get_guide_by_id(guide_id)
    if not guide:
        raise ValueError(f"Guide with ID {guide_id} not found.")

    m = message.lower()
    dest = guide["destination"]
    guide_name = guide["name"]

    # Contextual dynamic replies based on guide specialty and user queries
    if any(w in m for w in ["price", "cost", "fee", "rate", "how much", "charges"]):
        reply = (
            f"Namaste {traveler_name}! My standard full-day guided rate for {dest} is ₹{guide['rate_per_day']:,} "
            f"(or ₹{guide['rate_per_hour']:,}/hour for custom walks). This covers my full-time local guidance, "
            f"historical storytelling, and queue navigation. We can also customize the timing to suit your schedule!"
        )
    elif any(w in m for w in ["timing", "time", "best time", "darshan", "aarti", "when"]):
        if "varanasi" in dest.lower():
            reply = (
                f"For Varanasi, early mornings (5:30 AM) are magical for the Ganga boat sunrise at Assi Ghat, "
                f"and evening Maha Aarti begins around 6:45 PM at Dashashwamedh. I can reserve an exclusive boat viewpoint "
                f"so you can avoid the crowded ghat steps!"
            )
        elif "kedarnath" in dest.lower() or "badrinath" in dest.lower():
            reply = (
                f"The temple doors open at 5:00 AM for early morning Maha Abhishek. If you are trekking from Gaurikund, "
                f"we should start by 5:30 AM to beat the afternoon mist and ensure an easy pace. I will monitor the "
                f"weather forecast constantly for your safety!"
            )
        elif "ayodhya" in dest.lower():
            reply = (
                f"In Ayodhya, the Ram Mandir morning darshan runs from 6:30 AM to 11:30 AM, and evening darshan from 2:00 PM "
                f"to 9:00 PM. Evening Sarayu Aarti at Ram Ki Paidi at 7:00 PM is an unforgettable spiritual experience!"
            )
        elif "jaipur" in dest.lower():
            reply = (
                f"In Jaipur, Amber Fort is best visited right at 8:30 AM before the heat and tour buses arrive. In the "
                f"late afternoon, Nahargarh Fort offers the most spectacular sunset overlook across the entire Pink City!"
            )
        elif "tokyo" in dest.lower():
            reply = (
                f"Konnichiwa {traveler_name}! Asakusa Senso-ji is most peaceful at 8:00 AM before Nakamise street gets busy. "
                f"For Tsukiji market, 9:00 AM to 11:00 AM is ideal for fresh seafood tastings!"
            )
        elif "paris" in dest.lower():
            reply = (
                f"Bonjour {traveler_name}! The Louvre is best visited on Wednesday or Friday evenings or right at 9:00 AM. "
                f"I take you through the secret Richelieu entrance to bypass the massive pyramid queues completely!"
            )
        else:
            reply = (
                f"The optimal time for exploring {dest} is in the morning hours (8:00 AM - 11:30 AM) when the sights are serene, "
                f"followed by late afternoon cultural strolls. I will craft our exact hours around your personal pace!"
            )
    elif any(w in m for w in ["custom", "family", "kids", "elderly", "parents", "slow"]):
        reply = (
            f"Absolutely! I customize all my journeys for families with elderly parents and children. We can travel at a "
            f"relaxed pace, arrange wheelchair or battery cart access where available, and schedule gentle rest stops with "
            f"refreshing local refreshments."
        )
    elif any(w in m for w in ["book", "hire", "available", "tomorrow", "date", "weekend"]):
        reply = (
            f"I would be honored to guide you! I have availability for this upcoming week. You can click '📅 Hire / Book Guide' "
            f"right here on Travel Pace to generate our confirmed booking voucher, or reach me directly on WhatsApp at "
            f"{guide['direct_whatsapp']}."
        )
    elif any(w in m for w in ["whatsapp", "phone", "call", "contact", "number"]):
        reply = (
            f"You can reach me directly anytime via WhatsApp or Call at {guide['direct_phone']}! "
            f"Feel free to send me your dates and hotel location so I can organize your pickup."
        )
    else:
        reply = (
            f"Hello {traveler_name}! Thank you for reaching out. As your certified local guide for {dest}, "
            f"I am here to ensure you experience the most authentic, safe, and memorable journey. What places or "
            f"experiences are you most excited to see?"
        )

    return {
        "guide_id": guide_id,
        "guide_name": guide_name,
        "reply": reply,
        "timestamp": datetime.now().strftime("%I:%M %p"),
        "status": "delivered"
    }
