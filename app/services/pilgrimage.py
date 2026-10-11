"""Comprehensive database and budget calculation engine for Indian Temples & Dham Yatras."""
from typing import Dict, List, Any
from datetime import datetime, timedelta

# Complete Catalog of Major Indian Temples & Sacred Dham Circuits
PILGRIMAGE_CIRCUITS: Dict[str, Dict[str, Any]] = {
    "do-dham-kedarnath-badrinath": {
        "id": "do-dham-kedarnath-badrinath",
        "title": "6-Day Sacred Do Dham Yatra: Kedarnath Jyotirlinga & Badrinath Vishal",
        "destination": "Kedarnath & Badrinath",
        "country": "India",
        "state": "Uttarakhand",
        "latitude": 30.7352,
        "longitude": 79.0669,
        "recommended_days": 6,
        "cover_image": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
        "description": "High Himalayan sacred pilgrimage to Baba Kedar Jyotirlinga amidst snow peaks and Lord Badrinath Vishal along the Alaknanda river, including hot Tapt Kund snan and Mana village.",
        "cost_model": {
            "Budget": {"transport": 4500.0, "stay": 4800.0, "pooja": 1100.0, "food": 3600.0, "extras": 1500.0},
            "Standard": {"transport": 9800.0, "stay": 9000.0, "pooja": 2500.0, "food": 5400.0, "extras": 2800.0},
            "Premium": {"transport": 22500.0, "stay": 18000.0, "pooja": 6500.0, "food": 8500.0, "extras": 5000.0} # Includes Helicopter shuttle Phata-Kedarnath
        },
        "transports": [
            ("Helicopter / Hill Cab", "Kedarnath Heli Shuttle (Phata/Sirsi ⇄ Kedarnath) or AC Innova", "Haridwar/Rishikesh ⇄ Guptkashi ⇄ Kedarnath", 8500.0, "Book Heli tickets on official IRCTC Heli Yatra portal; carries 2 kg cabin baggage."),
            ("Cab/Taxi", "Private Hill Cab to Badrinath via Joshimath", "Guptkashi ⇄ Chopta ⇄ Joshimath ⇄ Badrinath", 4800.0, "Scenic mountain route through Alaknanda-Mandakini sangam."),
            ("Pony / Palki", "Gaurikund to Kedarnath Base Trek Mule/Palki Allowance", "Gaurikund (1,982m) → Kedarnath Mandir (3,584m - 16km)", 3200.0, "Fixed government rates set by Rudraprayag District Administration.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Haridwar Ganga Snan & Drive to Guptkashi", "Haridwar / Guptkashi", 30.5228, 79.0760, 400.0, "Attraction", "Holy dip at Har Ki Pauri and scenic mountain drive along Devprayag Sangam."),
            (1, "Evening", "Kashi Vishwanath Mandir Sandhya Aarti (Guptkashi)", "Guptkashi Town", 30.5228, 79.0760, 200.0, "Attraction", "Ancient stone temple where Pandavas sought Lord Shiva's blessings."),
            (2, "Morning", "Helicopter / 16km Holy Trek from Gaurikund to Kedarnath", "Kedarnath Trek Trail", 30.6500, 79.0600, 1500.0, "Transport", "Scenic alpine ascent crossing Lincholi and Bhimbali with views of Kedar dome."),
            (2, "Evening", "Grand Sandhya Aarti at Kedarnath Jyotirlinga", "Kedarnath Temple Sanctum", 30.7352, 79.0669, 500.0, "Attraction", "Soul-stirring conch shells and mantra chanting in front of the 8th-century stone temple."),
            (3, "Morning", "Kedarnath Shringar Darshan & Bhairavnath Temple Trek", "Kedarnath & Bhairav Ghati", 30.7390, 79.0700, 300.0, "Attraction", "Early morning darshan followed by a 1km trek to Kshetrapal Bhairavnath shrine."),
            (3, "Afternoon", "Descent to Sonprayag & Drive to Chopta (Mini Switzerland)", "Chopta Meadows", 30.4855, 79.1764, 400.0, "Leisure", "Scenic drive through rhododendron forests with views of Chaukhamba peaks."),
            (4, "Morning", "Drive from Chopta to Joshimath & Badrinath Dham", "Badrinath Road", 30.7443, 79.4930, 600.0, "Transport", "Traverse Vishnuprayag and enter the sacred Neelkanth valley."),
            (4, "Evening", "Tapt Kund Holy Snan & Badrinath Shayan Aarti", "Badrinath Temple", 30.7443, 79.4930, 500.0, "Attraction", "Natural sulfur thermal spring bath followed by peaceful evening darshan."),
            (5, "Morning", "Badrinath Maha Abhishek Darshan & Brahma Kapal Pitru Tarpan", "Badrinath Dham", 30.7443, 79.4930, 800.0, "Attraction", "Witness divine morning abhishek of Lord Badri Vishal carved from black Saligram stone."),
            (5, "Afternoon", "Excursion to Mana: The First Indian Village, Vyas Gufa & Saraswati River", "Mana Village, Indo-Tibetan Border", 30.7719, 79.4958, 400.0, "Attraction", "Visit the cave where Maharishi Ved Vyas dictated the Mahabharata to Lord Ganesha."),
            (6, "Morning", "Return Journey Badrinath to Rishikesh / Haridwar", "Rishikesh", 30.0869, 78.2676, 500.0, "Transport", "Drop at Rishikesh with cherished sacred memories and holy Ganga snan.")
        ],
        "packing_extras": [
            "Heavy thermal innerwear & fleece jackets (Kedarnath drops below 0°C at night)",
            "Waterproof rain poncho or windcheater with hood",
            "Sturdy hiking boots with ankle support & wool socks",
            "Portable power bank (power cuts common in upper Kedarnath)",
            "Personal medical kit: Camphor tablets (helps breathing at high altitude), Diamox, ORS, pain spray",
            "Aadhaar Card copy & Yatra Biometric Registration QR code"
        ]
    },

    "char-dham-uttarakhand": {
        "id": "char-dham-uttarakhand",
        "title": "10-Day Complete Uttarakhand Char Dham Yatra: Yamunotri, Gangotri, Kedarnath & Badrinath",
        "destination": "Char Dham (Uttarakhand)",
        "country": "India",
        "state": "Uttarakhand",
        "latitude": 30.7443,
        "longitude": 79.4930,
        "recommended_days": 10,
        "cover_image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "description": "The ultimate Sanatana Dharma mountain pilgrimage visiting all 4 sacred abodes in divine sequence: Yamunotri, Gangotri, Kedarnath, and Badrinath Vishal.",
        "cost_model": {
            "Budget": {"transport": 7500.0, "stay": 8500.0, "pooja": 1800.0, "food": 6000.0, "extras": 2500.0},
            "Standard": {"transport": 16000.0, "stay": 15000.0, "pooja": 4000.0, "food": 9000.0, "extras": 4500.0},
            "Premium": {"transport": 35000.0, "stay": 28000.0, "pooja": 9500.0, "food": 14000.0, "extras": 8000.0}
        },
        "transports": [
            ("Bus / Hill Cab", "10-Day Dedicated AC Hill Coach / Tempo Traveller", "Haridwar ⇄ Barkot ⇄ Uttarkashi ⇄ Guptkashi ⇄ Badrinath", 12500.0, "Authorized green card commercial vehicle for hill circuit."),
            ("Pony / Doli", "Yamunotri & Kedarnath Trek Assistance (Janki Chatti / Gaurikund)", "Base to Temple Sanctuaries", 4800.0, "Registered pre-paid counter tickets with pilgrim insurance."),
            ("Auto-Rickshaw", "Haridwar Railway Station ⇄ Har Ki Pauri Shuttle", "Station ⇄ Ghat", 300.0, "E-rickshaw for quick river commute.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Haridwar to Barkot via Kempty Falls Mussoorie", "Barkot, Uttarkashi", 30.8124, 78.2045, 500.0, "Transport", "Scenic drive climbing into the Garhwal Himalayas."),
            (2, "Morning", "Holy Yamunotri Dham Darshan, Divya Shila & Surya Kund Snan", "Yamunotri Temple", 31.0140, 78.4600, 800.0, "Attraction", "Cook raw rice in boiling thermal spring of Surya Kund as sacred prasad."),
            (3, "Morning", "Barkot to Uttarkashi & Kashi Vishwanath Temple Aarti", "Uttarkashi", 30.7268, 78.4354, 400.0, "Attraction", "Visit the ancient 6-meter-high copper trident (Shakti Trishul) temple."),
            (4, "Morning", "Holy Gangotri Dham Darshan & Bhagirath Shila", "Gangotri Temple", 30.9947, 78.9398, 700.0, "Attraction", "Sacred river bath at the source of Holy River Ganga amidst granite cliffs."),
            (5, "Morning", "Uttarkashi to Guptkashi via Tehri Dam Lake", "Guptkashi", 30.5228, 79.0760, 600.0, "Transport", "Drive along the colossal blue waters of Tehri Dam reservoir."),
            (6, "Morning", "Gaurikund to Baba Kedarnath Mandir Ascent", "Kedarnath", 30.7352, 79.0669, 1200.0, "Attraction", "Arrival at Baba Kedar's divine altar and participate in evening Maha Aarti."),
            (7, "Morning", "Kedarnath Puja & Descent to Sonprayag / Guptkashi", "Guptkashi", 30.5228, 79.0760, 500.0, "Transport", "Early morning darshan followed by scenic descent."),
            (8, "Morning", "Guptkashi to Badrinath Dham via Chopta & Joshimath", "Badrinath", 30.7443, 79.4930, 700.0, "Transport", "Traverse picturesque high alpine pastures and Alaknanda valley."),
            (9, "Morning", "Badrinath Darshan, Mana Village, Vyas Gufa & Bhim Pul", "Badrinath & Mana", 30.7719, 79.4958, 600.0, "Attraction", "Explore the mythical Saraswati River origin and stone bridge laid by Bhima."),
            (10, "Morning", "Return from Badrinath to Rishikesh & Haridwar Drop", "Haridwar", 29.9457, 78.1642, 500.0, "Transport", "Culmination of the holy Char Dham yatra with evening Ganga Aarti.")
        ],
        "packing_extras": [
            "Waterproof trekking shoes with extra woolen socks",
            "Thermals (2 pairs), windproof fleece jacket, woolen cap & gloves",
            "Raincoat/Poncho and sturdy foldable umbrella",
            "Mosquito repellent, lip balm, cold cream, SPF 50 sunscreen",
            "Personal water purification bottle / thermosteel flask",
            "Valid Govt ID & Char Dham Yatra Registration E-Pass"
        ]
    },

    "vaishno-devi-shiv-khori": {
        "id": "vaishno-devi-shiv-khori",
        "title": "4-Day Sacred Mata Vaishno Devi Dham & Shiv Khori Cave Yatra",
        "destination": "Vaishno Devi (Katra)",
        "country": "India",
        "state": "Jammu & Kashmir",
        "latitude": 33.0308,
        "longitude": 74.9490,
        "recommended_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
        "description": "Sacred pilgrimage to the Holy Cave Shrine of Mata Vaishno Devi in Trikuta Hills, Bhairon Baba ropeway darshan, and natural stalagmite Shivling cave of Shiv Khori.",
        "cost_model": {
            "Budget": {"transport": 3200.0, "stay": 3000.0, "pooja": 600.0, "food": 2400.0, "extras": 1200.0},
            "Standard": {"transport": 6500.0, "stay": 6000.0, "pooja": 1500.0, "food": 3600.0, "extras": 2000.0},
            "Premium": {"transport": 14000.0, "stay": 11000.0, "pooja": 4000.0, "food": 5500.0, "extras": 3500.0} # Includes Katra-Sanjichhat Helicopter
        },
        "transports": [
            ("Train", "Vande Bharat Express (New Delhi to Shri Mata Vaishno Devi Katra)", "New Delhi (NDLS) → Katra (SVDK)", 1650.0, "Ultra-fast direct train arriving at Katra in just 8 hours."),
            ("Helicopter / Ropeway", "Katra to Sanjichhat Helicopter or Bhairon Ghati Ropeway", "Katra ⇄ Sanjichhat / Bhawan ⇄ Bhairon Ghati", 2100.0, "Book helicopter on official Shri Mata Vaishno Devi Shrine Board (SMVDSB) website."),
            ("Cab/Taxi", "Katra to Shiv Khori Natural Cave Excursion Cab", "Katra ⇄ Ransoo / Shiv Khori (75 km roundtrip)", 2800.0, "Scenic mountain drive via Reasi and Chenab River bridge.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Katra Station & Check-in at Hotel / Shrine Board Guest House", "Katra Town", 32.9922, 74.9317, 300.0, "Lodging", "Collect RFID Yatra Access Card at Katra counter."),
            (1, "Evening", "Banganga Holy Snan & Evening Trek Commencement to Ardhkuwari", "Banganga Gate", 33.0050, 74.9400, 200.0, "Attraction", "Begin the illuminated 12km paved path with chantings of 'Jai Mata Di'."),
            (2, "Morning", "Ardhkuwari Garbha Joon Cave Darshan & Proceed to Bhawan", "Ardhkuwari Temple", 33.0200, 74.9450, 400.0, "Attraction", "Crawl through the sacred womb-like cave where Mata meditated for 9 months."),
            (2, "Afternoon", "Holy Darshan of Natural Pindies (Maha Kali, Maha Lakshmi, Maha Saraswati)", "Vaishno Devi Bhawan", 33.0308, 74.9490, 500.0, "Attraction", "Divine darshan of the eternal Swayambhu rock pindies inside the sanctum."),
            (2, "Evening", "Bhairon Ghati Ropeway Ride & Bhairavnath Temple Darshan", "Bhairon Ghati", 33.0350, 74.9520, 300.0, "Attraction", "Pilgrimage is considered complete only after paying homage at Bhairon Mandir."),
            (3, "Morning", "Descent to Katra & Full-Day Day Excursion to Shiv Khori Cave", "Shiv Khori Cave, Reasi", 33.0667, 74.5333, 800.0, "Attraction", "Marvel at the 150m natural limestone cave with self-manifested 4ft Shivling with milky water drip."),
            (4, "Morning", "Katra Local Market (Dry fruits, Walnuts, Kashmiri Shawls) & Departure", "Katra Market", 32.9922, 74.9317, 400.0, "Shopping", "Board return Vande Bharat Express back home refreshed.")
        ],
        "packing_extras": [
            "Comfortable sports/walking shoes with thick soles (12-14 km hill trek)",
            "Light jacket / sweater (Bhawan & Sanjichhat can be chilly at night)",
            "Knee support brace or walking stick for trek descent",
            "Valid Govt photo ID (mandatory for RFID yatra card issuance)"
        ]
    },

    "tirupati-balaji": {
        "id": "tirupati-balaji",
        "title": "3-Day Divine Tirupati Balaji: Venkateswara Temple & Srikalahasti",
        "destination": "Tirupati Balaji",
        "country": "India",
        "state": "Andhra Pradesh",
        "latitude": 13.6833,
        "longitude": 79.3472,
        "recommended_days": 3,
        "cover_image": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?auto=format&fit=crop&w=1200&q=80",
        "description": "Sacred pilgrimage to Kaliyuga Vaikuntam - Lord Venkateswara Swamy on Tirumala Hills, authentic Laddu Mahaprasadam, Padmavathi Temple, and Rahu-Ketu Srikalahasti Kshetra.",
        "cost_model": {
            "Budget": {"transport": 2800.0, "stay": 2400.0, "pooja": 600.0, "food": 2000.0, "extras": 1000.0},
            "Standard": {"transport": 5800.0, "stay": 5500.0, "pooja": 1800.0, "food": 3200.0, "extras": 1800.0},
            "Premium": {"transport": 12000.0, "stay": 11000.0, "pooja": 4500.0, "food": 5000.0, "extras": 3000.0} # Includes VIP Break Darshan & Private AC Toyota Fortuner
        },
        "transports": [
            ("Train / Flight", "Vande Bharat / Domestic Flight to Tirupati (TIR)", "Chennai/Bangalore/Hyderabad → Tirupati", 3200.0, "Renigunta Airport is 15 km from Tirupati town."),
            ("Cab/Taxi", "Tirupati to Tirumala Hill Ghat Road AC Taxi (Both ways)", "Tirupati Foot Hill ⇄ Tirumala 7 Hills Peak", 1800.0, "Official APSRTC or TTD registered cab navigating the scenic 21 km ghats."),
            ("Cab/Taxi", "Srikalahasti Rahu-Ketu Temple Day Excursion", "Tirupati ⇄ Srikalahasteeswara Temple (38 km)", 1400.0, "Private cab with temple waiting time.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Tirupati & Alipiri Foot Steps / Ghat Road Ascent to Tirumala", "Alipiri Foot Hills", 13.6500, 79.3800, 300.0, "Transport", "Traditional pilgrimage ascent or scenic ghat road climb to the 7 sacred hills."),
            (1, "Evening", "Swami Pushkarini Holy Teertham Snan & Varahaswamy Darshan", "Tirumala Hills", 13.6833, 79.3472, 200.0, "Attraction", "Per ancient tradition, offer prayers to Adi Varahaswamy before visiting Lord Balaji."),
            (2, "Morning", "Special Entry Darshan (SED ₹300) of Lord Venkateswara Swamy", "Sri Venkateswara Temple, Tirumala", 13.6833, 79.3472, 600.0, "Attraction", "Gaze upon the magnificent 8-foot bejewelled idol of Lord Balaji under the Ananda Nilayam vimana."),
            (2, "Afternoon", "Collecting Blessed Tirupati GI-Tagged Laddu Mahaprasad", "TTD Laddu Complex", 13.6833, 79.3472, 300.0, "Food", "World-renowned aromatic besan, ghee, cardamom, cashew and sugar candy laddus."),
            (2, "Evening", "Descent to Tirupati & Sri Padmavathi Ammavari Temple (Tiruchanur)", "Tiruchanur", 13.6067, 79.4500, 300.0, "Attraction", "Darshan of Goddess Lakshmi incarnate, divine consort of Lord Venkateswara."),
            (3, "Morning", "Excursion to Srikalahasteeswara Temple (Vayu Linga & Rahu-Ketu Nivarana Pooja)", "Srikalahasti", 13.7500, 79.7000, 800.0, "Attraction", "Ancient Chola Dravidian temple where air/wind element of Shiva is worshipped with oil lamps flickering sans wind.")
        ],
        "packing_extras": [
            "Traditional Indian attire (Strict TTD Dress Code: Dhoti/Kurta for Men; Saree/Salwar Kameez with Dupatta for Women)",
            "Original Aadhaar Card (Mandatory for entry queue verification matching booked ticket)",
            "Small cloth bag to carry holy Laddu Prasadam safely",
            "Slip-on sandals (shoes deposited outside queue complex for several hours)"
        ]
    },

    "ayodhya-kashi": {
        "id": "ayodhya-kashi",
        "title": "4-Day Awadh & Kashi: Ram Mandir Ayodhya & Kashi Vishwanath Dham",
        "destination": "Ayodhya & Varanasi",
        "country": "India",
        "state": "Uttar Pradesh",
        "latitude": 26.7922,
        "longitude": 82.1998,
        "recommended_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
        "description": "Grand spiritual corridor journey from Lord Rama's Janmabhoomi temple and holy Saryu river in Ayodhya to Mahadev's eternal Kashi Vishwanath Dham and Ganga Aarti.",
        "cost_model": {
            "Budget": {"transport": 2500.0, "stay": 3200.0, "pooja": 800.0, "food": 2200.0, "extras": 1100.0},
            "Standard": {"transport": 5200.0, "stay": 6500.0, "pooja": 2000.0, "food": 3800.0, "extras": 2200.0},
            "Premium": {"transport": 11000.0, "stay": 12500.0, "pooja": 4500.0, "food": 6000.0, "extras": 3500.0}
        },
        "transports": [
            ("Train", "Vande Bharat Express (Delhi to Ayodhya Cantt & Varanasi)", "New Delhi → Ayodhya (AY) → Varanasi (BSB)", 2200.0, "Superfast AC Chair Car transit on the sacred heritage corridor."),
            ("Cab/Taxi", "Private AC Sedan Intercity Cab (Ayodhya to Varanasi)", "Ram Janmabhoomi ⇄ Kashi Vishwanath (210 km / 4.5 hrs)", 3800.0, "Comfortable highway transit through Sultanpur and Jaunpur."),
            ("Boat", "Sunrise Hand-Rowed Ganges Boat Ride in Varanasi", "Assi Ghat ⇄ Dashashwamedh Ghat", 800.0, "Traditional wooden boat during morning sunrise prayers.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Maharishi Valmiki Airport / Ayodhya Dham Station & Check-in", "Ayodhya Dham", 26.7922, 82.1998, 300.0, "Lodging", "Check into heritage boutique stay near Ramkot."),
            (1, "Afternoon", "Hanuman Garhi Fort Mandir Darshan & Kanak Bhawan", "Hanuman Garhi", 26.7950, 82.2000, 200.0, "Attraction", "Climb 76 steps to seek Bajrangbali's blessings before visiting Ram Janmabhoomi."),
            (1, "Evening", "Ram Ki Paidi & Grand Evening Saryu River Maha Aarti", "Saryu Ghat, Ayodhya", 26.8020, 82.2050, 300.0, "Attraction", "Mesmerizing floating lamps and Vedic hymns along the illuminated Saryu banks."),
            (2, "Morning", "Grand Darshan of Ram Lalla at Shri Ram Janmabhoomi Mandir", "Ram Janmabhoomi Complex", 26.7956, 82.1944, 500.0, "Attraction", "Marvel at the pink Bansi Paharpur stone Nagara-style temple and 51-inch Balak Ram idol."),
            (2, "Afternoon", "Scenic Intercity Drive from Ayodhya to Kashi (Varanasi)", "National Highway 330", 25.3176, 82.9739, 700.0, "Transport", "Comfortable transit into the oldest living city in the world."),
            (2, "Evening", "Dashashwamedh Ghat Grand Maha Aarti from a Decorated Boat", "Dashashwamedh Ghat", 25.3076, 83.0107, 600.0, "Attraction", "Breathtaking multi-tiered brass lamp ritual dedicated to Lord Shiva and River Ganga."),
            (3, "Morning", "Subah-e-Banaras Sunrise Boat Ride & Kashi Vishwanath Golden Temple Darshan", "Kashi Vishwanath Corridor", 25.3109, 83.0107, 800.0, "Attraction", "Sugam Darshan of the sacred Jyotirlinga and Annapurna Devi temple."),
            (3, "Afternoon", "Kaal Bhairav Mandir (Kotwal of Kashi) & Sankat Mochan Darshan", "Kaal Bhairav, Varanasi", 25.3200, 83.0150, 300.0, "Attraction", "Traditional protection thread (Kaala Dhaga) and delicious besan laddus."),
            (4, "Morning", "Sarnath Buddhist Stupa, Deer Park & Banarasi Silk Weaving Trail", "Sarnath", 25.3811, 83.0214, 500.0, "Attraction", "Site of Lord Buddha's first sermon, Ashoka Lion Capital museum, and weaver looms.")
        ],
        "packing_extras": [
            "Modest Indian traditional clothing suitable for temple sanctums",
            "Small waterproof pouch for mobile & prasad",
            "Slip-on shoes / sandals easy to remove outside temple gates",
            "Government Photo ID for Ram Janmabhoomi & Kashi VIP counters"
        ]
    },

    "jagannath-puri": {
        "id": "jagannath-puri",
        "title": "4-Day Eastern Dham: Shree Jagannath Puri & Konark Sun Temple",
        "destination": "Puri & Konark",
        "country": "India",
        "state": "Odisha",
        "latitude": 19.8049,
        "longitude": 85.8179,
        "recommended_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
        "description": "Sacred Bada Dham on the Bay of Bengal: Shree Jagannath Mahaprabhu's 12th-century sanctum, Anandabazar Chhappan Bhog, Golden Beach, and Konark Sun Temple architecture.",
        "cost_model": {
            "Budget": {"transport": 2400.0, "stay": 2800.0, "pooja": 500.0, "food": 2000.0, "extras": 1000.0},
            "Standard": {"transport": 4800.0, "stay": 5800.0, "pooja": 1500.0, "food": 3400.0, "extras": 1800.0},
            "Premium": {"transport": 10500.0, "stay": 11500.0, "pooja": 3500.0, "food": 5500.0, "extras": 3000.0}
        },
        "transports": [
            ("Train", "Vande Bharat Express (Howrah / Rourkela to Puri)", "Howrah / Bhubaneswar → Puri (PURI)", 1450.0, "Fast coastal rail service arriving right near Golden Beach."),
            ("Cab/Taxi", "Puri to Konark Sun Temple Marine Drive Day Cab", "Puri ⇄ Chandrabhaga Beach ⇄ Konark (35 km)", 1600.0, "Scenic coastal highway running parallel to casuarina groves."),
            ("Auto-Rickshaw", "Puri Town & Gundicha Temple Electric Auto", "Grand Road (Bada Danda) ⇄ Temple Gates", 250.0, "Eco-friendly shuttle on Grand Road.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Puri Railway Station & Check-in at Marine Drive Beachfront Resort", "Puri Beach", 19.8000, 85.8200, 300.0, "Lodging", "Holy dip at sacred Mahodadhi (Bay of Bengal Golden Beach)."),
            (1, "Evening", "Singhadwara Arrival & Evening Darshan of Jagannath, Balabhadra & Subhadra", "Shree Jagannath Temple", 19.8049, 85.8179, 500.0, "Attraction", "Witness the breathtaking 5:00 PM Patitapavana flag-changing ceremony (Chuna ceremony)."),
            (2, "Morning", "Mahaprasad Feast at Anandabazar (World's Largest Open-Air Food Market)", "Anandabazar, Puri", 19.8049, 85.8179, 400.0, "Food", "Sample steaming earthen pots of Kanika, Dalma, and Khaja cooked in solar-aligned earthen ovens."),
            (2, "Afternoon", "Gundicha Temple (Mausi Maa Temple) & Narendra Sarovar Teertham", "Puri Town", 19.8200, 85.8250, 300.0, "Attraction", "Visit the garden abode where Lord Jagannath resides during the annual Ratha Yatra."),
            (3, "Morning", "Excursion via Marine Drive to UNESCO World Heritage Konark Sun Temple", "Konark Sun Temple", 19.8876, 86.0945, 600.0, "Attraction", "Marvel at the monumental stone chariot with 24 carved wheels and 7 galloping horses."),
            (3, "Afternoon", "Chandrabhaga Clean Blue Flag Beach & Sand Art Demonstration", "Chandrabhaga", 19.8650, 86.1100, 300.0, "Leisure", "Famous sun salutation beach and world-renowned sand sculptures."),
            (4, "Morning", "Raghurajpur Heritage Pattachitra Crafts Village & Departure", "Raghurajpur", 19.8800, 85.8200, 400.0, "Shopping", "Watch traditional artisans paint palm-leaf scrolls and wooden Jagannath idols.")
        ],
        "packing_extras": [
            "Modest cotton garments (Strict rule: Leather belts, wallets, and bags are prohibited inside Jagannath Temple)",
            "Sun hat and sunglasses for Konark Sun Temple open complex",
            "Cloth bag for taking home blessed Puri Khaja sweets"
        ]
    },

    "dwarka-somnath": {
        "id": "dwarka-somnath",
        "title": "5-Day Western Dham: Dwarkadhish Mandir, Bet Dwarka & Somnath Jyotirlinga",
        "destination": "Dwarka & Somnath",
        "country": "India",
        "state": "Gujarat",
        "latitude": 22.2442,
        "longitude": 68.9685,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
        "description": "Lord Krishna's submerged golden kingdom of Dwarkadhish, Sudama Setu, holy Gomti Ghat snan, and the first among 12 Jyotirlingas: Somnath Mahadev overlooking the Arabian Sea.",
        "cost_model": {
            "Budget": {"transport": 3400.0, "stay": 3600.0, "pooja": 700.0, "food": 2600.0, "extras": 1200.0},
            "Standard": {"transport": 7200.0, "stay": 7500.0, "pooja": 1800.0, "food": 4200.0, "extras": 2200.0},
            "Premium": {"transport": 15000.0, "stay": 14000.0, "pooja": 4000.0, "food": 6500.0, "extras": 3500.0}
        },
        "transports": [
            ("Train / Flight", "Saurashtra Mail / Vande Bharat to Rajkot/Dwarka", "Ahmedabad → Dwarka (DWK)", 1650.0, "Comfortable coastal express train connecting Gujarat Dhams."),
            ("Cab/Taxi", "Dwarka to Somnath via Porbandar Coastal AC Cab", "Dwarka ⇄ Porbandar ⇄ Somnath (235 km)", 4200.0, "Scenic highway halt at Kirti Mandir (Mahatma Gandhi birthplace) and Madhavpur Beach."),
            ("Ferry", "Okha to Bet Dwarka Island Ferry Boat", "Okha Port ⇄ Bet Dwarka Island", 250.0, "Scenic 20-minute Arabian Sea ferry or crossing the new Sudarshan Setu bridge.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Dwarka & Gomti Ghat Holy River Dip", "Gomti Ghat, Dwarka", 22.2400, 68.9650, 300.0, "Attraction", "Holy snan where sacred Gomti river meets the Arabian Sea."),
            (1, "Evening", "Dwarkadhish Jagat Mandir Evening Aarti & Dhwajarohan (Flag Ceremony)", "Dwarkadhish Temple", 22.2442, 68.9685, 500.0, "Attraction", "Witness the grand 52-yard triangular flag hoisting atop the 5-storey limestone spire."),
            (2, "Morning", "Ferry across Sudarshan Setu to Bet Dwarka & Nageshwar Jyotirlinga", "Bet Dwarka & Nageshwar", 22.4500, 69.0800, 700.0, "Attraction", "Darshan of Lord Krishna's residential palace and the 80ft colossal Shiva statue at Nageshwar."),
            (2, "Afternoon", "Rukmini Devi Mandir & Gopi Talav Holy Mud Snan", "Rukmini Temple", 22.2600, 68.9900, 300.0, "Attraction", "12th-century shrine dedicated to Krishna's queen Rukmini."),
            (3, "Morning", "Scenic Coastal Drive to Somnath with Stopover at Porbandar & Sudama Temple", "Porbandar Coastal Road", 21.6417, 69.6293, 800.0, "Transport", "Visit the only temple in the world dedicated to Sudama, Krishna's childhood friend."),
            (4, "Morning", "First Jyotirlinga Darshan at Shree Somnath Mahadev Temple", "Somnath Temple", 20.8880, 70.4012, 600.0, "Attraction", "Majestic temple standing proud where Arabian Sea waves crash at its foundation walls."),
            (4, "Evening", "Spectacular Sound & Light Show (Amitabh Bachchan voiceover) & Triveni Sangam", "Somnath Sea Front", 20.8880, 70.4012, 400.0, "Attraction", "Confluence of Hiran, Kapila, and mythical Saraswati rivers where Lord Krishna rested."),
            (5, "Morning", "Bhalka Teerth (Dehotsarg Teerth) & Return Departure", "Veraval / Rajkot", 20.9000, 70.3800, 500.0, "Transport", "Sacred banyan tree site where Lord Krishna ascended to his heavenly abode.")
        ],
        "packing_extras": [
            "Comfortable light cotton clothing (breezy coastal climate)",
            "Strict temple rule: Cell phones, smart watches, and leather belts must be left in free clock rooms",
            "Govt ID proof for temple security gates"
        ]
    },

    "ujjain-omkareshwar": {
        "id": "ujjain-omkareshwar",
        "title": "3-Day Mahakaal Darshan: Ujjain Mahakaleshwar & Omkareshwar Jyotirlinga",
        "destination": "Ujjain & Omkareshwar",
        "country": "India",
        "state": "Madhya Pradesh",
        "latitude": 23.1827,
        "longitude": 75.7682,
        "recommended_days": 3,
        "cover_image": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
        "description": "Holy Avantika Kshetra: Experience the legendary 4:00 AM Bhasma Aarti at Mahakaleshwar Jyotirlinga, grand Mahakal Lok Corridor, Kal Bhairav liquor offering, and Om-shaped Narmada island Jyotirlinga.",
        "cost_model": {
            "Budget": {"transport": 2200.0, "stay": 2400.0, "pooja": 700.0, "food": 1800.0, "extras": 900.0},
            "Standard": {"transport": 4500.0, "stay": 4800.0, "pooja": 1800.0, "food": 2800.0, "extras": 1600.0},
            "Premium": {"transport": 9500.0, "stay": 9800.0, "pooja": 3800.0, "food": 4500.0, "extras": 2500.0} # Includes VIP Bhasma Aarti Protocol Entry
        },
        "transports": [
            ("Train", "Vande Bharat Express (Bhopal / Indore to Ujjain Jn)", "Indore/Bhopal → Ujjain Jn (UJN)", 1100.0, "Modern AC train running directly into Ujjain city center."),
            ("Cab/Taxi", "Private AC Cab from Ujjain to Omkareshwar Island & Return", "Ujjain ⇄ Omkareshwar (140 km roundtrip)", 2800.0, "Comfortable highway ride along Malwa plains to Narmada gorge."),
            ("Boat", "Narmada Holy River Boat Parikrama at Omkareshwar", "Ghat to Mandhata Island", 300.0, "Scenic rowboat on River Narmada circling the holy Om symbol island.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Ujjain & Ram Ghat Holy Shipra River Snan", "Ram Ghat, Ujjain", 23.1800, 75.7600, 200.0, "Attraction", "Historic Kumbh Mela riverbank with centuries-old Shiva shrines."),
            (1, "Evening", "Illuminated Mahakal Lok Corridor Walk & Evening Sandhya Aarti", "Shri Mahakal Lok", 23.1827, 75.7682, 400.0, "Attraction", "Grand 900-meter corridor with 108 sculpted pillars depicting Shiva Leelas."),
            (2, "Morning", "World-Famous 4:00 AM Bhasma Aarti at Mahakaleshwar Jyotirlinga", "Mahakaleshwar Temple", 23.1827, 75.7682, 800.0, "Attraction", "Sacred ritual worshipping the Lord of Time with holy cow-dung bhasma."),
            (2, "Afternoon", "Kal Bhairav Mandir (Famous Prasad Offering) & Harsiddhi Mata Shaktipeeth", "Kal Bhairav, Ujjain", 23.2000, 75.7800, 300.0, "Attraction", "Witness the unbroken mystical tradition where deity is offered liquor."),
            (3, "Morning", "Day Excursion to Omkareshwar Jyotirlinga & Mamleshwar Mandir", "Omkareshwar Island", 22.2450, 76.1500, 700.0, "Attraction", "Darshan of the 4th Jyotirlinga on Mandhata island shaped like sacred ॐ symbol.")
        ],
        "packing_extras": [
            "Traditional dress for Bhasma Aarti (Men: Unstitched Cotton Dhoti & Angavastram; Women: Saree only)",
            "Pre-booking Bhasma Aarti registration slip printout",
            "Comfortable sandals"
        ]
    },

    "rameswaram-madurai": {
        "id": "rameswaram-madurai",
        "title": "5-Day Southern Dham: Rameswaram 22 Theerthams, Dhanushkodi & Madurai Meenakshi",
        "destination": "Rameswaram & Madurai",
        "country": "India",
        "state": "Tamil Nadu",
        "latitude": 9.2881,
        "longitude": 79.3174,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "description": "Southern Char Dham on Pamban Island: Holy snan in 22 sacred temple wells, Lord Rama's Ram Setu starting point at Dhanushkodi, and architectural marvel Madurai Meenakshi Amman temple.",
        "cost_model": {
            "Budget": {"transport": 3600.0, "stay": 4000.0, "pooja": 700.0, "food": 2800.0, "extras": 1400.0},
            "Standard": {"transport": 7500.0, "stay": 8000.0, "pooja": 2000.0, "food": 4500.0, "extras": 2400.0},
            "Premium": {"transport": 16000.0, "stay": 15000.0, "pooja": 4500.0, "food": 7000.0, "extras": 4000.0}
        },
        "transports": [
            ("Train", "Rameswaram Express crossing Sea Pamban Bridge", "Madurai / Chennai → Rameswaram (RMM)", 1500.0, "Iconic railway crossing open waters of the Indian Ocean."),
            ("Cab/Taxi", "Dhanushkodi Ram Setu Point 4x4 Beach Cab Excursion", "Rameswaram ⇄ Dhanushkodi Ghost Town & Vibhishan Temple", 1800.0, "Drive to the tip of India where Indian Ocean and Bay of Bengal meet."),
            ("Cab/Taxi", "Intercity Cab Rameswaram to Madurai", "Rameswaram ⇄ Madurai Meenakshi Temple (170 km)", 3400.0, "Comfortable 3-hour journey through Tamil hinterlands.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival across Pamban Sea Bridge into Rameswaram & Agni Teertham Snan", "Agni Teertham", 9.2881, 79.3174, 300.0, "Attraction", "Holy sea bath on the peaceful shores of the Bay of Bengal."),
            (1, "Evening", "Sacred Bath in 22 Holy Theerthams inside Ramanathaswamy Temple", "Ramanathaswamy Temple", 9.2881, 79.3174, 500.0, "Attraction", "Well water bath carrying healing minerals followed by Spatika Lingam darshan."),
            (2, "Morning", "Darshan of Jyotirlinga Consecrated by Mata Sita & Pillar Hall (1212 Pillars)", "Ramanathaswamy Temple", 9.2881, 79.3174, 400.0, "Attraction", "World's longest temple corridor with carved granite pillars."),
            (2, "Afternoon", "4x4 Excursion to Dhanushkodi (Ghost Town) & Ram Setu Adam's Bridge View", "Dhanushkodi", 9.1780, 79.4180, 600.0, "Attraction", "Eerie submerged ruins of the 1964 cyclone and floating stones of Rama's bridge."),
            (3, "Morning", "Scenic Transit to Madurai & Evening Chithirai Street Walk", "Madurai", 9.9195, 78.1194, 600.0, "Transport", "Arrive in Tamil Nadu's cultural capital."),
            (4, "Morning", "Magnificent Madurai Meenakshi Sundareswarar Temple Darshan", "Meenakshi Amman Temple", 9.9195, 78.1194, 700.0, "Attraction", "Explore the 14 multi-colored gopurams and the Thousand Pillar Museum Hall."),
            (5, "Morning", "Thirumalai Nayakkar Palace, Madurai Jigarthanda & Departure", "Madurai Town", 9.9150, 78.1200, 300.0, "Food", "Taste authentic chilled Jigarthanda and buy famous Madurai Sungudi cotton sarees.")
        ],
        "packing_extras": [
            "Change of dry clothes after bathing in the 22 holy theerthams",
            "Modest attire (Dhoti/pants for men, Sarees/churidars for women; shorts prohibited)",
            "Flip-flops (marble floors can be warm during mid-day)"
        ]
    }
}

# Additional Curated Indian Destinations (Heritage, Beaches, Mountains, Culture & Temples)
ADDITIONAL_INDIAN_DESTINATIONS: Dict[str, Dict[str, Any]] = {
    "jaipur-pink-city": {
        "id": "jaipur-pink-city",
        "title": "5-Day Royal Rajputana: Amber Fort, Hawa Mahal & Desert Heritage",
        "destination": "Jaipur",
        "country": "India",
        "state": "Rajasthan",
        "category": "Heritage & Palaces",
        "latitude": 26.9124,
        "longitude": 75.7873,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "description": "Grand palaces, UNESCO hilltop forts, vibrant bazaars, authentic Rajasthani thali, and sunset over Nahargarh Fort.",
        "cost_model": {
            "Budget": {"transport": 2200.0, "stay": 3500.0, "pooja": 1200.0, "food": 2500.0, "extras": 1200.0},
            "Standard": {"transport": 5500.0, "stay": 8000.0, "pooja": 2800.0, "food": 4500.0, "extras": 2500.0},
            "Premium": {"transport": 14000.0, "stay": 18000.0, "pooja": 6000.0, "food": 8500.0, "extras": 4500.0}
        },
        "transports": [
            ("Train / Flight", "Vande Bharat Express (Delhi to Jaipur Jn)", "Delhi Cantt → Jaipur (JP)", 1350.0, "Fast 3.5 hour AC chair car transit."),
            ("Cab/Taxi", "Full-Day Sightseeing AC Sedan with Chauffeur", "Jaipur City ⇄ Amer Fort ⇄ Nahargarh ⇄ Jaigarh", 2200.0, "Covers all uphill forts with waiting time included.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival & Check-in at Heritage Haveli", "Old City Jaipur", 26.9124, 75.7873, 400.0, "Lodging", "Check into traditional boutique Haveli stay."),
            (1, "Evening", "Hawa Mahal Sunset & Johari Bazaar Walk", "Hawa Mahal", 26.9239, 75.8267, 300.0, "Attraction", "Marvel at 953 honeycomb windows and explore gemstone markets."),
            (2, "Morning", "Grand Amber Fort & Sheesh Mahal Exploration", "Amer Fort", 26.9855, 75.8513, 800.0, "Attraction", "Monumental fort with exquisite mirror palace."),
            (3, "Morning", "City Palace Museum & Jantar Mantar Observatory", "City Palace", 26.9258, 75.8237, 600.0, "Attraction", "Royal residence and world's largest stone sundial."),
            (4, "Morning", "Nahargarh & Jaigarh Forts Cannon Viewpoint", "Nahargarh Fort", 26.9370, 75.8155, 500.0, "Attraction", "Panoramic view over the entire Pink City."),
            (5, "Morning", "Chokhi Dhani Rajasthani Cultural Village Feast & Departure", "Chokhi Dhani", 26.7670, 75.8330, 900.0, "Food", "Traditional folk dances, camel rides, and grand thali.")
        ],
        "packing_extras": ["Comfortable walking shoes for stone fort ramps", "Sun hat and SPF 50 sunscreen", "Light cotton clothes and scarf"]
    },

    "goa-sun-sand": {
        "id": "goa-sun-sand",
        "title": "5-Day Coastal Bliss: North & South Goa Beaches, Forts & Cruises",
        "destination": "Goa",
        "country": "India",
        "state": "Goa",
        "category": "Beach & Coastal",
        "latitude": 15.2993,
        "longitude": 74.1240,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "description": "Pristine white sand beaches, Portuguese baroque churches, water sports at Calangute, sunset catamaran cruise, and serene Palolem bay.",
        "cost_model": {
            "Budget": {"transport": 2500.0, "stay": 4000.0, "pooja": 1500.0, "food": 3000.0, "extras": 1500.0},
            "Standard": {"transport": 6500.0, "stay": 9500.0, "pooja": 3500.0, "food": 5500.0, "extras": 3000.0},
            "Premium": {"transport": 16000.0, "stay": 22000.0, "pooja": 8000.0, "food": 11000.0, "extras": 5000.0}
        },
        "transports": [
            ("Flight / Train", "Direct Flight / Tejas Express to Goa (GOI/GOX)", "Metro → Goa Dabolim/Mopa", 3500.0, "Fast connectivity to both North & South Goa."),
            ("Rental Scooter / Cab", "Self-Drive Activa Scooter / AC Cab Rental", "Panaji ⇄ Calangute ⇄ Anjuna ⇄ Palolem", 600.0, "Most convenient and breezy way to explore coastal roads.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival & Beachfront Resort Check-in", "Candolim / Calangute", 15.5170, 73.7630, 500.0, "Lodging", "Check in and relax with coconut water by the waves."),
            (1, "Evening", "Sunset at Aguada Fort & Lighthouse", "Aguada Fort", 15.4920, 73.7737, 300.0, "Attraction", "17th-century Portuguese coastal fortress overlooking Arabian Sea."),
            (2, "Morning", "Calangute & Baga Water Sports Adventure", "Baga Beach", 15.5553, 73.7517, 1500.0, "Attraction", "Parasailing, banana boat ride, and jet skiing."),
            (3, "Morning", "Old Goa Basilica of Bom Jesus & Fontainhas Latin Quarter", "Old Goa", 15.5009, 73.9116, 400.0, "Attraction", "UNESCO World Heritage churches and pastel Portuguese mansions."),
            (4, "Morning", "South Goa Day Trip: Colva, Benaulim & Palolem Beach", "Palolem Beach", 15.0100, 74.0230, 800.0, "Leisure", "Scenic crescent bay with calm turquoise waters and dolphin spotting."),
            (5, "Evening", "Mandovi River Sunset Catamaran Cruise & Departure", "Panaji Jetty", 15.4989, 73.8278, 600.0, "Leisure", "Live Goan folk music, dances, and scenic river evening.")
        ],
        "packing_extras": ["Swimwear & quick-dry microfiber towel", "Sunglasses, sun hat & reef-safe sunscreen", "Flip-flops & beach sandals", "Waterproof dry bag for phone"]
    },

    "manali-solang-snow": {
        "id": "manali-solang-snow",
        "title": "5-Day Himalayan Escape: Manali, Solang Valley & Atal Tunnel",
        "destination": "Manali",
        "country": "India",
        "state": "Himachal Pradesh",
        "category": "Mountains & Snow",
        "latitude": 32.2396,
        "longitude": 77.1887,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
        "description": "Snow-capped Pir Panjal peaks, pine forests, Hadimba Devi temple, Solang Valley adventure, and scenic drive through the engineering marvel Atal Tunnel.",
        "cost_model": {
            "Budget": {"transport": 2800.0, "stay": 3800.0, "pooja": 1500.0, "food": 2800.0, "extras": 1400.0},
            "Standard": {"transport": 6800.0, "stay": 8500.0, "pooja": 3500.0, "food": 4800.0, "extras": 2800.0},
            "Premium": {"transport": 16500.0, "stay": 19000.0, "pooja": 7500.0, "food": 9000.0, "extras": 4500.0}
        },
        "transports": [
            ("Bus / Hill Cab", "Overnight Volvo AC Coach (Delhi/Chandigarh to Manali)", "Delhi/Chandigarh → Manali Private Stand", 1600.0, "Comfortable semi-sleeper coach with hill driving."),
            ("Cab/Taxi", "Dedicated 4x4 Hill Cab for Solang Valley & Atal Tunnel", "Manali ⇄ Solang ⇄ Sissu / Lahaul Valley", 3200.0, "High ground clearance vehicle with snow chains if required.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Manali & Check-in at Riverside Cottage", "Old Manali", 32.2530, 77.1850, 400.0, "Lodging", "Breathe crisp mountain pine air along Beas river."),
            (1, "Evening", "Hadimba Temple, Vashisht Hot Springs & Mall Road", "Hadimba Temple", 32.2483, 77.1695, 300.0, "Attraction", "Ancient wooden pagoda temple amidst towering deodars."),
            (2, "Morning", "Solang Valley Snow Sports, Paragliding & Zorbing", "Solang Valley", 32.3160, 77.1570, 1600.0, "Attraction", "Thrilling snow adventures and ropeway cable car rides."),
            (3, "Morning", "Atal Tunnel Drive into Lahaul Valley & Sissu Waterfalls", "Atal Tunnel (Rohtang)", 32.3640, 77.1350, 800.0, "Attraction", "World's longest highway tunnel above 10,000 feet into trans-Himalayan Lahaul."),
            (4, "Morning", "Jogini Waterfalls Nature Hike & Old Manali Cafes", "Jogini Falls, Vashisht", 32.2680, 77.1950, 300.0, "Leisure", "Scenic trail through apple orchards and mountain streams."),
            (5, "Morning", "Tibetan Monastery, Souvenir Shopping & Departure", "Manali Mall Road", 32.2396, 77.1887, 400.0, "Shopping", "Pick up Kullu shawls, pure mountain honey, and apple cider.")
        ],
        "packing_extras": ["Heavy warm jacket, thermals & woolen gloves", "Waterproof snow boots with good grip", "Sunglasses for snow glare protection", "Moisturizer & lip balm for mountain dry air"]
    },

    "munnar-alleppey-kerala": {
        "id": "munnar-alleppey-kerala",
        "title": "5-Day God's Own Country: Munnar Tea Hills & Alleppey Houseboat",
        "destination": "Munnar & Alleppey",
        "country": "India",
        "state": "Kerala",
        "category": "Mountains & Coastal",
        "latitude": 10.0889,
        "longitude": 77.0595,
        "recommended_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
        "description": "Rolling emerald tea plantations, Eravikulam Nilgiri Tahr sanctuary, spice gardens, and an overnight luxury houseboat cruise on tranquil backwaters.",
        "cost_model": {
            "Budget": {"transport": 2600.0, "stay": 4200.0, "pooja": 1400.0, "food": 2800.0, "extras": 1300.0},
            "Standard": {"transport": 6200.0, "stay": 9800.0, "pooja": 3200.0, "food": 5000.0, "extras": 2600.0},
            "Premium": {"transport": 15000.0, "stay": 24000.0, "pooja": 7500.0, "food": 9500.0, "extras": 4500.0}
        },
        "transports": [
            ("Flight / Cab", "Flight to Cochin (COK) + AC Intercity Cab", "Kochi Airport → Munnar → Alleppey → Kochi", 4500.0, "Comfortable AC sedan with experienced hill driver."),
            ("Houseboat", "Private Deluxe Kettuvallam Houseboat on Vembanad Lake", "Alleppey Punnamada Jetty Roundtrip", 8500.0, "Includes freshly prepared Kerala meals (Karimeen Pollichathu, payasam).")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Cochin & Scenic Drive to Munnar via Cheeyappara Falls", "Munnar Road", 10.0400, 76.9500, 400.0, "Transport", "Ascend through misty Western Ghats with cascading roadside waterfalls."),
            (2, "Morning", "Eravikulam National Park & Rajamalai Nilgiri Tahr", "Eravikulam", 10.1500, 77.0600, 600.0, "Attraction", "Spot the endangered mountain goat amidst Neelakurinji slopes."),
            (2, "Afternoon", "Tata Tea Museum & Tea Tasting Experience", "Munnar Town", 10.0889, 77.0595, 300.0, "Attraction", "Learn the art of orthodox tea processing from fresh leaf to brew."),
            (3, "Morning", "Mattupetty Dam, Echo Point & Kundala Lake Boating", "Mattupetty", 10.1060, 77.1240, 500.0, "Attraction", "High altitude lake surrounded by shola forests and tea gardens."),
            (4, "Morning", "Transfer to Alleppey & Check-in to Deluxe Backwater Houseboat", "Alleppey Backwaters", 9.4981, 76.3388, 1200.0, "Lodging", "Glide past paddy fields, Chinese fishing nets, and coconut palms."),
            (5, "Morning", "Traditional Backwater Breakfast, Village Canoe Ride & Departure", "Alleppey Jetty", 9.4981, 76.3388, 400.0, "Leisure", "Return to Cochin with aromatic spices and coconut oil souvenirs.")
        ],
        "packing_extras": ["Light sweaters for Munnar evenings (12-15°C)", "Cotton clothes for Alleppey humidity", "Mosquito repellent lotion for backwaters", "Umbrella or light raincoat (frequent tropical showers)"]
    },

    "leh-ladakh-high-passes": {
        "id": "leh-ladakh-high-passes",
        "title": "7-Day Land of High Passes: Leh, Pangong Tso, Nubra Valley & Khardung La",
        "destination": "Leh Ladakh",
        "country": "India",
        "state": "Ladakh",
        "category": "Himalayas & High Altitude",
        "latitude": 34.1526,
        "longitude": 77.5771,
        "recommended_days": 7,
        "cover_image": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
        "description": "Cross the highest motorable road at Khardung La, ride double-humped camels in Nubra sand dunes, and camp beside the surreal blue waters of Pangong Tso.",
        "cost_model": {
            "Budget": {"transport": 5500.0, "stay": 6500.0, "pooja": 1800.0, "food": 4500.0, "extras": 2500.0},
            "Standard": {"transport": 12500.0, "stay": 14000.0, "pooja": 4200.0, "food": 7500.0, "extras": 4500.0},
            "Premium": {"transport": 28000.0, "stay": 32000.0, "pooja": 9500.0, "food": 14000.0, "extras": 8000.0}
        },
        "transports": [
            ("Flight", "Direct Flight to Kushok Bakula Rimpochee Airport (IXL)", "Delhi → Leh (IXL)", 6500.0, "Spectacular flight over snow-capped Himalayan ridges."),
            ("Cab/Taxi", "Dedicated 4x4 Scorpio/Innova for High Pass Circuit", "Leh ⇄ Nubra ⇄ Pangong ⇄ Leh", 14500.0, "Authorized local Leh union taxi with high altitude reliability.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Leh (3,500m) & Mandatory Acclimatization Rest", "Leh City", 34.1526, 77.5771, 300.0, "Lodging", "Full day rest to adapt to thin air with garlic soup and fluids."),
            (2, "Morning", "Shanti Stupa, Leh Palace & Hall of Fame Museum", "Leh Town", 34.1643, 77.5847, 500.0, "Attraction", "White-domed stupa offering 360-degree views of the Indus Valley."),
            (3, "Morning", "Drive over Khardung La Pass (17,982 ft) into Nubra Valley", "Khardung La Pass", 34.2787, 77.6047, 800.0, "Transport", "One of the world's highest motorable mountain passes."),
            (3, "Evening", "Hunder White Sand Dunes & Double-Humped Bactrian Camel Ride", "Hunder, Nubra", 34.5800, 77.4700, 600.0, "Attraction", "Desert dunes framed by soaring snow-capped granite peaks."),
            (4, "Morning", "Diskit Monastery 106-foot Maitreya Buddha & Drive to Pangong", "Diskit & Shyok Valley", 34.5420, 77.5600, 700.0, "Attraction", "Majestic outdoor golden Buddha statue overlooking the river valley."),
            (5, "Morning", "Sunrise over Color-Changing Pangong Tso Lake (14,270 ft)", "Pangong Lake", 33.7595, 78.6674, 900.0, "Attraction", "Spectacular 134km lake spanning India and Tibet changing shades from turquoise to cobalt."),
            (6, "Morning", "Return to Leh via Chang La Pass & Thiksey Monastery", "Thiksey Monastery", 34.0583, 77.6667, 600.0, "Attraction", "12-storey monastery resembling the Potala Palace of Lhasa."),
            (7, "Morning", "Leh Main Bazaar Shopping & Airport Departure", "Leh Bazaar", 34.1526, 77.5771, 400.0, "Shopping", "Collect authentic Pashmina shawls, Ladakhi apricots, and prayer wheels.")
        ],
        "packing_extras": ["Diamox (acetazolamide) tablets for Acute Mountain Sickness (AMS)", "Thermal base layers, down jacket & windproof pants", "UV400 polarized sunglasses & high SPF sunblock (strong UV rays)", "Hydration bladder / thermos flask for warm water"]
    },

    "udaipur-city-of-lakes": {
        "id": "udaipur-city-of-lakes",
        "title": "4-Day Venice of the East: Udaipur Lake Pichola, City Palace & Jag Mandir",
        "destination": "Udaipur",
        "country": "India",
        "state": "Rajasthan",
        "category": "Heritage & Palaces",
        "latitude": 24.5854,
        "longitude": 73.7125,
        "recommended_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
        "description": "Fairytale marble palaces rising from shimmering lakes, romantic sunset boat rides on Lake Pichola, Saheliyon-ki-Bari, and vintage car museum.",
        "cost_model": {
            "Budget": {"transport": 2200.0, "stay": 3600.0, "pooja": 1100.0, "food": 2400.0, "extras": 1200.0},
            "Standard": {"transport": 5400.0, "stay": 8200.0, "pooja": 2600.0, "food": 4400.0, "extras": 2400.0},
            "Premium": {"transport": 14500.0, "stay": 26000.0, "pooja": 6500.0, "food": 9500.0, "extras": 4500.0}
        },
        "transports": [
            ("Train / Flight", "Vande Bharat / Direct Flight to Maharana Pratap Airport (UDR)", "Metro → Udaipur (UDZ/UDR)", 2800.0, "Convenient connectivity into the City of Lakes."),
            ("Boat / Cab", "Private Solar Boat Cruise on Lake Pichola to Jag Mandir", "City Palace Ghat ⇄ Jag Mandir Island", 850.0, "Golden hour boat ride passing the floating Lake Palace.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival & Check-in at Lake View Heritage Haveli", "Lake Pichola Shore", 24.5760, 73.6800, 400.0, "Lodging", "Breathtaking views of the serene lake and Aravalli hills."),
            (1, "Evening", "Bagore Ki Haveli Dharohar Rajasthani Dance Show", "Gangaur Ghat", 24.5794, 73.6828, 350.0, "Attraction", "Vibrant Kalbelia dance, puppet shows, and Rajasthani folklore."),
            (2, "Morning", "Monumental Udaipur City Palace & Crystal Gallery", "City Palace", 24.5764, 73.6835, 750.0, "Attraction", "Rajasthan's largest palace complex with intricate mirror work."),
            (2, "Evening", "Sunset Boat Cruise on Lake Pichola to Jag Mandir Island", "Jag Mandir", 24.5678, 73.6778, 800.0, "Leisure", "Magical island palace illuminated under evening twilight."),
            (3, "Morning", "Saheliyon-ki-Bari Royal Fountains & Monsoon Palace (Sajjangarh)", "Sajjangarh Fort", 24.5900, 73.6300, 500.0, "Attraction", "Hilltop palace built to watch monsoon clouds roll over Aravallis."),
            (4, "Morning", "Jagdish Mandir Darshan, Miniature Painting Studio & Departure", "Jagdish Temple", 24.5795, 73.6841, 300.0, "Attraction", "Detailed stone carved Vishnu temple and traditional Mewar silk paintings.")
        ],
        "packing_extras": ["Traditional attire for photo ops against white marble palaces", "Comfortable walking slip-ons", "Sunglasses and sun hat"]
    },

    "amritsar-golden-temple": {
        "id": "amritsar-golden-temple",
        "title": "3-Day Holy Amritsar: Sri Harmandir Sahib, Langar & Wagah Border",
        "destination": "Amritsar",
        "country": "India",
        "state": "Punjab",
        "category": "Spiritual & Heritage",
        "latitude": 31.6200,
        "longitude": 74.8765,
        "recommended_days": 3,
        "cover_image": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",
        "description": "Sacred nectar pool of Sri Harmandir Sahib, the world's largest community kitchen serving 100,000 pilgrims daily, historic Jallianwala Bagh, and patriotic Wagah Border retreat.",
        "cost_model": {
            "Budget": {"transport": 1800.0, "stay": 2200.0, "pooja": 400.0, "food": 1600.0, "extras": 800.0},
            "Standard": {"transport": 4200.0, "stay": 5000.0, "pooja": 1200.0, "food": 3000.0, "extras": 1600.0},
            "Premium": {"transport": 9500.0, "stay": 11000.0, "pooja": 3000.0, "food": 5500.0, "extras": 2800.0}
        },
        "transports": [
            ("Train", "Vande Bharat Express / Shatabdi Express (Delhi to Amritsar)", "New Delhi → Amritsar Jn (ASR)", 1350.0, "Fast direct 5.5 hour AC train connection."),
            ("Cab/Taxi", "Dedicated AC Cab for Wagah Border Beating Retreat Ceremony", "Amritsar City ⇄ Attari-Wagah Border (32 km)", 1600.0, "Covers roundtrip transit and reserved seating queue waiting.")
        ],
        "itinerary_highlights": [
            (1, "Morning", "Arrival at Amritsar & Heritage Street Walk", "Heritage Street", 31.6200, 74.8765, 300.0, "Lodging", "Walk down pedestrian stone street to Golden Temple."),
            (1, "Evening", "Night Palki Sahib Ceremony at Sri Harmandir Sahib", "Golden Temple", 31.6200, 74.8765, 300.0, "Attraction", "Witness the holy Guru Granth Sahib carried in a golden palanquin amidst soul-stirring Gurbani kirtan."),
            (2, "Morning", "Amrit Vela Darshan, Sacred Sarovar Snan & Guru Ka Langar Seva", "Harmandir Sahib Complex", 31.6200, 74.8765, 400.0, "Attraction", "Participate in holy communal service preparing rotis and dal in the monumental langar."),
            (2, "Afternoon", "Jallianwala Bagh Memorial & Partition Museum", "Jallianwala Bagh", 31.6206, 74.8804, 300.0, "Attraction", "Pay homage at the historic national memorial and evocative partition archives."),
            (2, "Evening", "Patriotic Wagah Border Beating Retreat Ceremony", "Attari-Wagah Border", 31.6047, 74.5714, 600.0, "Attraction", "Electrifying military march, bugles, and national flag lowering ceremony."),
            (3, "Morning", "Authentic Amritsari Kulcha Breakfast & Departure", "Bhai Kulwant Singh Kulchian", 31.6250, 74.8700, 300.0, "Food", "Savor piping hot tandoori layered kulchas smothered in pure butter with chole.")
        ],
        "packing_extras": ["Head scarf / Rumal (mandatory for all genders inside Golden Temple complex)", "Slip-on shoes easy to deposit at free Jora Ghar counters", "Comfortable cotton clothes"]
    }
}

# Unified catalog containing both Dham Pilgrimages and All India Holiday Destinations
ALL_DESTINATIONS_CATALOG: Dict[str, Dict[str, Any]] = {**PILGRIMAGE_CIRCUITS, **ADDITIONAL_INDIAN_DESTINATIONS}


def get_all_pilgrimage_circuits() -> List[Dict[str, Any]]:
    """Return summary list of all sacred Dham & Temple circuits."""
    res = []
    for c in PILGRIMAGE_CIRCUITS.values():
        res.append({
            "id": c["id"],
            "title": c["title"],
            "destination": c["destination"],
            "state": c["state"],
            "recommended_days": c["recommended_days"],
            "cover_image": c["cover_image"],
            "description": c["description"],
            "base_budget_inr": c["cost_model"]["Budget"]["transport"] + c["cost_model"]["Budget"]["stay"] + c["cost_model"]["Budget"]["pooja"] + c["cost_model"]["Budget"]["food"] + c["cost_model"]["Budget"]["extras"]
        })
    return res


def get_all_destination_catalog_items() -> List[Dict[str, Any]]:
    """Return complete list of all supported destinations (Temples, Heritage, Beaches, Mountains, etc.)."""
    res = []
    for c in ALL_DESTINATIONS_CATALOG.values():
        res.append({
            "id": c["id"],
            "title": c["title"],
            "destination": c["destination"],
            "state": c.get("state", "India"),
            "category": c.get("category", "Spiritual & Pilgrimage"),
            "recommended_days": c["recommended_days"],
            "cover_image": c["cover_image"],
            "description": c["description"],
            "base_budget_inr": c["cost_model"]["Budget"]["transport"] + c["cost_model"]["Budget"]["stay"] + c["cost_model"]["Budget"]["pooja"] + c["cost_model"]["Budget"]["food"] + c["cost_model"]["Budget"]["extras"]
        })
    return res


def calculate_universal_destination_budget(
    destination: str = None,
    circuit_id: str = None,
    days: int = None,
    travel_tier: str = "Standard",
    num_travelers: int = 1,
    travel_style: str = "Leisure & Sightseeing",
    departure_date: str = None
) -> Dict[str, Any]:
    """Calculate instant, realistic budget for ANY Indian place (Dham, Heritage, Beach, Mountain, or custom city)."""
    tier = travel_tier if travel_tier in ["Budget", "Standard", "Premium"] else "Standard"
    n = max(1, num_travelers)

    # 1. Match from catalog by circuit_id or destination string
    matched_circuit = None
    if circuit_id and circuit_id in ALL_DESTINATIONS_CATALOG:
        matched_circuit = ALL_DESTINATIONS_CATALOG[circuit_id]
    elif destination:
        dest_clean = destination.strip().lower()
        for c in ALL_DESTINATIONS_CATALOG.values():
            if c["destination"].lower() in dest_clean or dest_clean in c["destination"].lower() or c["id"] == dest_clean:
                matched_circuit = c
                break

    if matched_circuit:
        # Use precise calibrated cost model from catalog
        costs = matched_circuit["cost_model"][tier]
        duration_days = days if (days and days > 0) else matched_circuit["recommended_days"]
        scale_ratio = duration_days / max(1, matched_circuit["recommended_days"])

        discount_factor = 1.0 if n == 1 else (0.85 if n == 2 else 0.75)
        transport_per_person = (costs["transport"] * (1.0 if n == 1 else 0.88)) * (0.8 + 0.2 * scale_ratio)
        stay_per_person = (costs["stay"] * discount_factor) * scale_ratio
        activities_per_person = costs["pooja"] * scale_ratio
        food_per_person = costs["food"] * scale_ratio
        extras_per_person = costs["extras"] * scale_ratio

        total_per_person = transport_per_person + stay_per_person + activities_per_person + food_per_person + extras_per_person
        total_group = round(total_per_person * n, 2)

        return {
            "circuit_id": matched_circuit["id"],
            "title": matched_circuit["title"],
            "destination": matched_circuit["destination"],
            "recommended_days": duration_days,
            "tier": tier,
            "num_travelers": n,
            "currency": "INR",
            "total_budget": total_group,
            "per_person_budget": round(total_per_person, 2),
            "breakdown": {
                "transport": round(transport_per_person * n, 2),
                "stay": round(stay_per_person * n, 2),
                "activities_entry": round(activities_per_person * n, 2),
                "food_dining": round(food_per_person * n, 2),
                "support_extras": round(extras_per_person * n, 2)
            },
            "highlights": [h[2] for h in matched_circuit["itinerary_highlights"][:4]],
            "key_transport": [t[1] for t in matched_circuit["transports"][:2]]
        }

    # 2. Arbitrary Custom Indian Destination Dynamic Cost Generation
    # Realistic Indian daily rates based on tier
    d = max(1, days or 4)
    dest_name = destination.strip() if destination else "Custom Indian Journey"

    if tier == "Budget":
        daily_stay = 900.0
        daily_food = 550.0
        daily_activities = 350.0
        daily_extras = 200.0
        base_transit = 1800.0  # Sleeper / 3AC / Intercity Bus
    elif tier == "Premium":
        daily_stay = 5800.0
        daily_food = 2000.0
        daily_activities = 1600.0
        daily_extras = 1100.0
        base_transit = 7800.0  # Flight / Innova Crysta
    else:  # Standard
        daily_stay = 2200.0
        daily_food = 950.0
        daily_activities = 700.0
        daily_extras = 500.0
        base_transit = 3400.0  # Vande Bharat / 2AC / Private Cab

    group_room_discount = 1.0 if n == 1 else (0.60 if n == 2 else 0.50)  # Shared hotel rooms
    group_transit_discount = 1.0 if n == 1 else 0.85

    transport_pp = (base_transit + (d * 300.0)) * group_transit_discount
    stay_pp = (daily_stay * d) * group_room_discount
    food_pp = daily_food * d
    act_pp = daily_activities * d
    extras_pp = daily_extras * d

    total_pp = transport_pp + stay_pp + food_pp + act_pp + extras_pp
    total_group = round(total_pp * n, 2)

    return {
        "circuit_id": f"custom-{dest_name.lower().replace(' ', '-')}",
        "title": f"{d}-Day Custom Journey to {dest_name}",
        "destination": dest_name,
        "recommended_days": d,
        "tier": tier,
        "num_travelers": n,
        "currency": "INR",
        "total_budget": total_group,
        "per_person_budget": round(total_pp, 2),
        "breakdown": {
            "transport": round(transport_pp * n, 2),
            "stay": round(stay_pp * n, 2),
            "activities_entry": round(act_pp * n, 2),
            "food_dining": round(food_pp * n, 2),
            "support_extras": round(extras_pp * n, 2)
        },
        "highlights": [
            f"Arrival and orientation in {dest_name}",
            f"Iconic sightseeing, culture and local markets in {dest_name}",
            f"Regional cuisine tasting & sunset viewpoints in {dest_name}",
            f"Scenic return transit and souvenir collection"
        ],
        "key_transport": [
            f"AC Train / Flight connectivity to {dest_name}",
            f"Local dedicated AC cab for sightseeing and transfers in {dest_name}"
        ]
    }


def calculate_dham_budget(circuit_id: str, travel_tier: str = "Standard", num_travelers: int = 1, departure_date: str = None) -> Dict[str, Any]:
    """Compatibility wrapper around calculate_universal_destination_budget."""
    return calculate_universal_destination_budget(
        destination=None,
        circuit_id=circuit_id,
        travel_tier=travel_tier,
        num_travelers=num_travelers,
        departure_date=departure_date
    )


# Curated, authentic high-resolution image registry for all Indian destinations
DESTINATION_IMAGE_REGISTRY: Dict[str, str] = {
    # Sacred Circuits & Temples
    "kedarnath": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
    "badrinath": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
    "char dham": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
    "gangotri": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
    "yamunotri": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
    "vaishno": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
    "katra": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
    "tirupati": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?auto=format&fit=crop&w=1200&q=80",
    "balaji": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?auto=format&fit=crop&w=1200&q=80",
    "ayodhya": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "varanasi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "kashi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "banaras": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "puri": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
    "konark": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
    "jagannath": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
    "dwarka": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
    "somnath": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
    "ujjain": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
    "omkareshwar": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
    "mahakal": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
    "rameswaram": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
    "madurai": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
    "meenakshi": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
    "amritsar": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",
    "golden temple": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",
    "harmandir": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",

    # Holiday, Mountains, Heritage, Nature & Cities
    "jaipur": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
    "hawa mahal": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
    "amer": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
    "udaipur": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
    "pichola": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
    "lake palace": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
    "goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
    "calangute": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
    "baga": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
    "manali": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
    "solang": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
    "kullu": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
    "atal tunnel": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
    "leh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "ladakh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "pangong": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "nubra": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
    "munnar": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "alleppey": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "kerala": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "kochi": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
    "rishikesh": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
    "haridwar": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
    "ganga": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
    "ooty": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
    "nilgiri": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
    "coonoor": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
    "mussoorie": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
    "mussorie": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
    "shimla": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=1200&q=80",
    "kufri": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=1200&q=80",
    "darjeeling": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
    "sikkim": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
    "gangtok": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
    "agra": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
    "taj mahal": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
    "delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "new delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "mohali": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "chandigarh": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "punjab": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
    "mumbai": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
    "bombay": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
    "kolkata": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1200&q=80",
    "calcutta": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1200&q=80",
    "chennai": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
    "madras": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
    "bangalore": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
    "bengaluru": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
    "hyderabad": "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=1200&q=80",
    "kashmir": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80",
    "srinagar": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80",
    "dal lake": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80",
}


def get_indian_destination_image(destination_str: str) -> str:
    """Resolve an authentic, place-specific cover image URL for any Indian destination."""
    if not destination_str:
        return "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80"

    clean = destination_str.lower().strip()

    # Exact key match in catalog
    if clean in ALL_DESTINATIONS_CATALOG:
        return ALL_DESTINATIONS_CATALOG[clean]["cover_image"]

    # Substring match in registry
    for key, img_url in DESTINATION_IMAGE_REGISTRY.items():
        if key in clean:
            return img_url

    # Check separate words
    words = clean.replace("-", " ").replace(",", " ").split()
    for w in words:
        if w in DESTINATION_IMAGE_REGISTRY:
            return DESTINATION_IMAGE_REGISTRY[w]

    # Authentic fallback: Himalayan peak landscape
    return "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80"


