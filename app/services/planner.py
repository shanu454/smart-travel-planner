"""Smart travel itinerary and packing checklist generator specialized for Indian destinations."""
from datetime import datetime, date, timedelta
from typing import Dict, Any, List, Optional
import math
import logging

logger = logging.getLogger(__name__)

# Indian Destinations Knowledge Base
DESTINATION_ACTIVITIES = {
    "jaipur": {
        "full_name": "Jaipur, Rajasthan",
        "days": [
            {
                "theme": "Grand Fortresses & Royal Palaces",
                "early_morning": ("Nahargarh Sunrise Trek & Viewpoint", "Watch the golden sunrise break over the Pink City from the historic ramparts.", "Nahargarh Fort, Jaipur", 26.9372, 75.8155, 100.0, "Attraction"),
                "morning": ("Amer Fort & Sheesh Mahal Mirror Palace", "Marvel at grand Rajput architecture, marble courtyards, and thousand-mirror reflections.", "Amer, Jaipur", 26.9855, 75.8513, 500.0, "Attraction"),
                "afternoon": ("City Palace & Jantar Mantar Astronomical Observatory", "Explore the royal family residence museum and the world's largest stone sundial.", "Old City, Jaipur", 26.9258, 75.8237, 700.0, "Attraction"),
                "late_afternoon": ("Hawa Mahal & Wind View Cafe Photo Stop", "Photograph the iconic 953-window pink sandstone honeycomb facade.", "Badi Choupad, Jaipur", 26.9239, 75.8267, 200.0, "Attraction"),
                "evening": ("Johari Bazaar Jewelry & Bapu Bazaar Mojari Shopping", "Browse authentic lac bangles, bandhani sarees, gemstones, and handcrafted camel leather juttis.", "Johari Bazaar, Jaipur", 26.9198, 75.8260, 350.0, "Leisure")
            },
            {
                "theme": "Artisan Heritage, Jal Mahal & Rajasthani Feast",
                "early_morning": ("Galtaji Monkey Temple & Sacred Kunds", "Visit the historic temple complex set within mountain crevices with natural mineral springs.", "Galta Gorge, Jaipur", 26.9161, 75.8586, 50.0, "Attraction"),
                "morning": ("Jal Mahal Water Palace Promenade", "Admire the red sandstone palace floating serenely in the middle of Man Sagar Lake.", "Amer Road, Jaipur", 26.9535, 75.8462, 0.0, "Attraction"),
                "afternoon": ("Anokhi Block Printing Museum & Craft Workshop", "Hands-on woodblock textile printing workshop preserving ancient Bagru and Sanganer craft.", "Kheri Gate, Amer", 26.9880, 75.8530, 250.0, "Leisure"),
                "late_afternoon": ("Albert Hall Museum & Ram Niwas Garden", "Historic Indo-Saracenic museum showcasing Persian carpets, royal armor, and miniature paintings.", "Ram Niwas Garden, Jaipur", 26.9116, 75.8195, 300.0, "Attraction"),
                "evening": ("Chokhi Dhani Traditional Village & Royal Thali", "Immersive cultural village with puppet shows, kalbelia folk dancers, fire acts, and authentic Dal Baati Churma.", "Tonk Road, Jaipur", 26.7663, 75.8362, 1200.0, "Food")
            },
            {
                "theme": "Stepwells, Heritage Cafes & Sunset Silhouette",
                "early_morning": ("Panna Meena Ka Kund Stepwell", "Photogenic 16th-century geometric symmetrical stepwell near Amer.", "Amer, Jaipur", 26.9883, 75.8569, 0.0, "Attraction"),
                "morning": ("Jaigarh Fort & Jaivana Cannon", "Climb the military stronghold housing the world's largest cannon on wheels.", "Jaigarh, Jaipur", 26.9800, 75.8450, 200.0, "Attraction"),
                "afternoon": ("Kafila & Tattoo Cafe Rooftop Overlooking Hawa Mahal", "Sip cold saffron lassi and savor pyaaz kachoris with an unbeatable view of the palace.", "Opposite Hawa Mahal, Jaipur", 26.9242, 75.8265, 450.0, "Food"),
                "late_afternoon": ("Birla Mandir & Moti Dungri Ganesh Temple", "Pure white marble modern temple dedicated to Lord Vishnu and Goddess Lakshmi.", "Tilak Nagar, Jaipur", 26.8924, 75.8155, 0.0, "Attraction"),
                "evening": ("Padao Open-Air Sunset Restaurant at Nahargarh", "Panoramic sunset drinks and snacks overlooking the twinkling lights of Jaipur city.", "Nahargarh Hills, Jaipur", 26.9375, 75.8150, 800.0, "Food")
            }
        ]
    },
    "goa": {
        "full_name": "Goa, India",
        "days": [
            {
                "theme": "Portuguese Heritage, Cathedrals & Fontainhas",
                "early_morning": ("Miramar Beach Morning Walk", "Tranquil stroll where the Mandovi River meets the Arabian Sea.", "Miramar, Panaji", 15.4820, 73.8070, 0.0, "Leisure"),
                "morning": ("Basilica of Bom Jesus & Se Cathedral (Old Goa)", "UNESCO World Heritage site holding the mortal remains of St. Francis Xavier.", "Old Goa", 15.5009, 73.9116, 100.0, "Attraction"),
                "afternoon": ("Fontainhas Latin Quarter Heritage Walk", "Wander through vibrant pastel-colored Portuguese villas, terracotta roofs, and historic bakeries.", "Panaji, Goa", 15.4989, 73.8278, 150.0, "Leisure"),
                "late_afternoon": ("Dona Paula Viewpoint & Jetty", "Panoramic sea cliff known as the Lovers' Paradise overlooking Mormugao Harbor.", "Dona Paula, Goa", 15.4578, 73.8042, 50.0, "Attraction"),
                "evening": ("Mandovi River Sunset Luxury Cruise", "Glide past casino lights with live Goan folk dance, Konkani music, and cocktails.", "Panaji Jetty, Goa", 15.5020, 73.8290, 650.0, "Attraction")
            },
            {
                "theme": "North Goa Beaches, Fort Aguada & Beach Shacks",
                "early_morning": ("Vagator Cliff Sunrise & Chapora Fort", "Perch atop the famous 'Dil Chahta Hai' fort with cinematic views of the coastline.", "Chapora, Goa", 15.6062, 73.7360, 50.0, "Attraction"),
                "morning": ("Fort Aguada & 19th-Century Portuguese Lighthouse", "17th-century Portuguese fortress overlooking Sinquerim beach and the Arabian Sea.", "Sinquerim, Goa", 15.4925, 73.7736, 100.0, "Attraction"),
                "afternoon": ("Calangute & Baga Beach Watersports", "Parasailing, jet ski rides, banana boat thrills, and sunbathing.", "Baga Beach, Goa", 15.5553, 73.7517, 1500.0, "Leisure"),
                "late_afternoon": ("Anjuna Beach Flea Market & Sunset Rock", "Bohemian handicrafts, tie-dye apparel, handmade silver jewelry, and coconut water.", "Anjuna Beach, Goa", 15.5733, 73.7410, 200.0, "Leisure"),
                "evening": ("Curlies or Thalassa Beach Shack Dinner", "Dine right on the sand with Goan prawn curry, butter garlic crab, and chilled beverages.", "Vagator Beach, Goa", 15.5990, 73.7380, 1400.0, "Food")
            },
            {
                "theme": "Spice Plantations & South Goa Serenity",
                "early_morning": ("Colva Beach Sunrise Stroll", "Quiet silver sands and gentle waves in tranquil South Goa.", "Colva, Goa", 15.2798, 73.9142, 0.0, "Leisure"),
                "morning": ("Sahakari Spice Farm Guided Tour & Herbal Tasting", "Discover cinnamon, cardamom, peri-peri peppers followed by a traditional buffet on banana leaves.", "Ponda, Goa", 15.4120, 74.0250, 600.0, "Attraction"),
                "afternoon": ("Palolem Beach Kayaking & Butterfly Island", "Paddle through turquoise calm waters to secluded dolphin coves.", "Palolem, Canacona", 15.0100, 74.0231, 800.0, "Leisure"),
                "late_afternoon": ("Cabo de Rama Cliff Fortress", "Ancient coastal fortress with sweeping dramatic views of the southern Arabian Sea cliffs.", "Canacona, Goa", 15.0880, 73.9210, 50.0, "Attraction"),
                "evening": ("Fisherman's Wharf Riverside Seafood Feast", "Authentic Goan peri-peri pomfret, bebinca dessert, and feni cocktails along the Sal River.", "Mobor, Cavelossim", 15.1740, 73.9470, 1600.0, "Food")
            }
        ]
    },
    "varanasi": {
        "full_name": "Varanasi, Uttar Pradesh",
        "days": [
            {
                "theme": "Sacred Ganges, Subah-e-Banaras & Evening Aarti",
                "early_morning": ("Subah-e-Banaras Sunrise Wooden Boat Ride", "Glide past 84 sacred stone ghats as the morning sun casts a holy amber glow over the river.", "Assi Ghat, Varanasi", 25.2885, 83.0064, 400.0, "Attraction"),
                "morning": ("Kashi Vishwanath Temple Golden Corridor Darshan", "One of the twelve sacred Jyotirlingas of Lord Shiva; walk through the grand temple corridor.", "Kashi Vishwanath, Varanasi", 25.3109, 83.0107, 300.0, "Attraction"),
                "afternoon": ("Banarasi Silk Saree Weaving Alleys & Blue Lassi Tasting", "Watch master weavers create gold zari brocades and taste hand-churned fruit lassi in earthen pots.", "Bangali Tola, Varanasi", 25.3080, 83.0090, 200.0, "Food"),
                "late_afternoon": ("Manikarnika & Harishchandra Historic Ghats Walk", "Reflective walk through the ancient cobblestone alleys and philosophical sacred ghats.", "Manikarnika Ghat, Varanasi", 25.3108, 83.0142, 0.0, "Attraction"),
                "evening": ("Dashashwamedh Ghat Grand Ganga Maha Aarti", "Spiritual spectacle of conch shells, giant brass fire lamps, incense, and floating earthen diyas.", "Dashashwamedh Ghat, Varanasi", 25.3076, 83.0104, 250.0, "Attraction")
            },
            {
                "theme": "Sarnath Buddhist Pilgrimage & Street Flavors",
                "early_morning": ("Tulsi Ghat Akhada Wrestling Practice", "Witness traditional mud wrestling (Kushti) practiced along the holy riverbanks at dawn.", "Tulsi Ghat, Varanasi", 25.2930, 83.0050, 0.0, "Attraction"),
                "morning": ("Sarnath Dhamek Stupa & Deer Park", "Where Lord Buddha delivered his very first sermon after attaining enlightenment.", "Sarnath, Varanasi", 25.3811, 83.0214, 300.0, "Attraction"),
                "afternoon": ("Sarnath Archaeological Museum & Ashoka Lion Capital", "Behold India's National Emblem: the original 4-lion polished sandstone Ashoka pillar.", "Sarnath, Varanasi", 25.3780, 83.0230, 100.0, "Attraction"),
                "late_afternoon": ("Banaras Hindu University (BHU) & New Vishwanath Temple", "Stroll through the green 1300-acre university campus and the towering marble temple.", "BHU, Varanasi", 25.2677, 82.9913, 0.0, "Leisure"),
                "evening": ("Kachori Gali Street Food Feast & Banarasi Paan", "Savor piping hot kachoris with aloo sabzi, malaiyo winter milk foam, and authentic meetha paan.", "Godowlia, Varanasi", 25.3100, 83.0070, 300.0, "Food")
            }
        ]
    },
    "kerala": {
        "full_name": "Kerala (Munnar & Alleppey)",
        "days": [
            {
                "theme": "Munnar Misty Tea Gardens & Mountain Peaks",
                "early_morning": ("Top Station Sunrise View over the Western Ghats", "Panoramic view of mist-blanketed valleys and rare Neelakurinji flower hills.", "Top Station, Munnar", 10.1250, 77.2450, 100.0, "Attraction"),
                "morning": ("Eravikulam National Park Nilgiri Tahr Safari", "Trek through the sanctuary of the endangered mountain goat species Nilgiri Tahr.", "Rajamalai, Munnar", 10.1983, 77.0603, 400.0, "Attraction"),
                "afternoon": ("KDHP Tata Tea Museum & Tasting", "Watch century-old tea processing machinery and sample freshly plucked orthodox Black Tea.", "Nullatanni, Munnar", 10.0880, 77.0610, 200.0, "Food"),
                "late_afternoon": ("Mattupetty Dam & Echo Point Boating", "Scenic lake enclosed by eucalyptus hills; enjoy speedboating and peaceful horse rides.", "Mattupetty, Munnar", 10.1060, 77.1240, 350.0, "Leisure"),
                "evening": ("Ayurvedic Herbal Rejuvenation Massage", "Relax tired muscles with warm medicated herbal oil (Abhyanga) by trained therapists.", "Munnar Town, Kerala", 10.0889, 77.0595, 1200.0, "Leisure")
            },
            {
                "theme": "Alleppey Backwaters Houseboat Odyssey",
                "early_morning": ("Vembanad Lake Bird Watching", "Spot kingfishers, cormorants, and egrets skimming over calm morning waters.", "Kumarakom / Alleppey", 9.6100, 76.4300, 150.0, "Attraction"),
                "morning": ("Traditional Kettuvallam Houseboat Check-In", "Board a handcrafted thatched-roof wooden houseboat with private sundeck and chef.", "Punnamada Finishing Point, Alleppey", 9.5010, 76.3520, 4500.0, "Transport"),
                "afternoon": ("Serene Canals & Paddy Fields Cruise", "Cruise through tranquil palm-fringed lagoons, village life, and water lilies.", "Kuttanad, Alleppey", 9.4500, 76.3800, 0.0, "Leisure"),
                "late_afternoon": ("Coconut Toddy & Fresh Karimeen Pollichathu", "Savor pearl spot fish marinated in shallots and chili, wrapped in banana leaf and roasted.", "Vembanad Backwaters, Kerala", 9.4800, 76.3700, 700.0, "Food"),
                "evening": ("Sunset Anchor & Candlelit Kerala Sadhya Banquet", "Traditional feast served on fresh banana leaf as the boat anchors in the serene backwaters.", "Kavalam, Alleppey", 9.5100, 76.4000, 600.0, "Food")
            }
        ]
    },
    "udaipur": {
        "full_name": "Udaipur, Rajasthan",
        "days": [
            {
                "theme": "Lakeside Royalty, City Palace & Pichola Cruise",
                "early_morning": ("Ambrai Ghat Sunrise over Lake Pichola", "Watch morning light reflect off the white marble island palaces and ghats.", "Ambrai Ghat, Udaipur", 24.5772, 73.6811, 0.0, "Attraction"),
                "morning": ("Udaipur City Palace & Crystal Gallery", "Rajasthan's largest royal palace complex with ornate peacock mosaics and balconies.", "City Palace, Udaipur", 24.5764, 73.6835, 600.0, "Attraction"),
                "afternoon": ("Lake Pichola Boat Cruise to Jag Mandir Palace", "Sail past the floating Lake Palace to the 17th-century island marble retreat.", "Jag Mandir, Udaipur", 24.5678, 73.6780, 500.0, "Attraction"),
                "late_afternoon": ("Saheliyon-ki-Bari Royal Courtesan Fountains", "Peaceful marble fountain gardens built for royal maidens with lotus pools and marble elephants.", "Panchwati, Udaipur", 24.5980, 73.6880, 100.0, "Leisure"),
                "evening": ("Bagore Ki Haveli Rajasthani Folk & Puppet Dance", "Mesmerizing evening performance with women balancing 9 brass pots on their heads.", "Gangaur Ghat, Udaipur", 24.5794, 73.6800, 250.0, "Attraction")
            },
            {
                "theme": "Monsoon Palace, Craft Bazaars & Candlelit Dinner",
                "early_morning": ("Fateh Sagar Lake Jog & Herbal Juice", "Scenic lakeside walkway surrounded by Aravalli mountain ranges.", "Fateh Sagar, Udaipur", 24.5950, 73.6720, 50.0, "Leisure"),
                "morning": ("Sajjangarh Monsoon Palace High Mountain Vista", "Hilltop palace built to watch monsoon rain clouds; panoramic 360-degree view.", "Sajjangarh, Udaipur", 24.5910, 73.6370, 300.0, "Attraction"),
                "afternoon": ("Hathi Pol Bazaar Miniature Paintings & Silver Jewelry", "Shop directly from miniature artists who paint with single-hair squirrel brushes.", "Hathi Pol, Udaipur", 24.5860, 73.6880, 400.0, "Leisure"),
                "late_afternoon": ("Karni Mata Ropeway Cable Car", "Ascend the Machla Magra hill in a scenic gondola for aerial palace photos.", "Doodh Talai, Udaipur", 24.5690, 73.6870, 150.0, "Attraction"),
                "evening": ("Lakeside Rooftop Candlelit Dinner at Upré", "Romantic dining overlooking illuminated Lake Pichola and the City Palace.", "Lake Pichola, Udaipur", 24.5780, 73.6815, 1800.0, "Food")
            }
        ]
    }
}

# Generic dynamic templates for other Indian destinations (Manali, Rishikesh, Delhi, Agra, Mumbai, etc.)
GENERIC_INDIAN_ACTIVITIES = [
    ("Historic Heritage Fort or Royal Palace Tour", "Explore grand stone architecture, royal courtyards, and deep-rooted local history.", "Heritage Quarter", 300.0, "Attraction"),
    ("Sacred Temple / Gurdwara / Cathedral Morning Visit", "Experience spiritual serenity, morning chants, and holy water rituals.", "Temple Precinct", 50.0, "Attraction"),
    ("Bustling Local Spice & Handicrafts Bazaar", "Browse artisan block prints, handmade textiles, fresh spices, and brass souvenirs.", "Central Bazaar", 200.0, "Leisure"),
    ("Scenic Panoramic Hilltop or Lake Sunset Point", "Unwind as the sunset bathes the landscape in rich crimson and gold.", "Sunset Vista", 100.0, "Attraction"),
    ("Authentic Regional Street Food & Thali Crawl", "Sample regional street delicacies, fresh chaat, hot jalebis, and authentic thalis.", "Food Street", 350.0, "Food"),
    ("Cultural Evening Folk Music & Dance Performance", "Enjoy traditional sitar acoustics, folk dancers, and vibrant regional attire.", "Cultural Auditorium", 400.0, "Leisure"),
    ("Nature Trail, Waterfall or Riverside Sanctuary", "Breathe crisp air along natural mountain trails or sacred riverbanks.", "Nature Reserve", 150.0, "Attraction"),
    ("Heritage Tea / Chai & Royal Sweet Shop Experience", "Sip fragrant cardamom masala chai paired with warm kachoris and gulab jamun.", "Heritage Tea Stall", 120.0, "Food")
]


def generate_smart_itinerary(
    destination: str,
    country: str = "India",
    lat: float = 0.0,
    lon: float = 0.0,
    start_date_str: str = "",
    end_date_str: str = "",
    travel_style: str = "Cultural & Heritage",
    travel_pace: str = "Moderate",
    total_budget: float = 25000.0,
    pace: str = ""
) -> List[Dict[str, Any]]:
    """
    Generate intelligent day-by-day itinerary tailored to destination, dates, and TRAVEL PACE.
    
    Travel Pace impacts:
      - 'Relaxed': 2 activities/day (Morning highlight + Evening sunset/dinner, with free afternoon).
      - 'Moderate': 3 activities/day (Morning, Afternoon, Evening).
      - 'Fast-Paced': 4 to 5 activities/day (Early Morning, Morning, Afternoon, Sunset, Night Bazaar).
    """
    effective_pace = travel_pace or pace or "Moderate"
    effective_pace_lower = effective_pace.lower()

    try:
        start_d = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_d = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        days_count = max(1, (end_d - start_d).days + 1)
    except Exception:
        days_count = 3

    dest_key = destination.strip().lower()
    # Fuzzy match known Indian hubs
    matched_key = None
    for key in DESTINATION_ACTIVITIES.keys():
        if key in dest_key or dest_key in key:
            matched_key = key
            break

    known_days = DESTINATION_ACTIVITIES[matched_key]["days"] if matched_key else []
    items = []
    order_counter = 1
    generic_idx = 0

    for day_num in range(1, days_count + 1):
        day_plan = known_days[(day_num - 1) % len(known_days)] if known_days else None

        # Build day schedule based on TRAVEL PACE
        if "relaxed" in effective_pace_lower:
            # RELAXED PACE: 2 activities per day (Morning + Evening)
            if day_plan:
                morning_act = day_plan.get("morning") or day_plan.get("early_morning")
                evening_act = day_plan.get("evening") or day_plan.get("late_afternoon")
                slots = [
                    ("Morning (9:30 AM)", morning_act),
                    ("Evening (5:30 PM)", evening_act)
                ]
            else:
                m_act = GENERIC_INDIAN_ACTIVITIES[generic_idx % len(GENERIC_INDIAN_ACTIVITIES)]
                generic_idx += 1
                e_act = GENERIC_INDIAN_ACTIVITIES[generic_idx % len(GENERIC_INDIAN_ACTIVITIES)]
                generic_idx += 1
                slots = [
                    ("Morning (9:30 AM)", (m_act[0], m_act[1], m_act[2], lat, lon, m_act[3], m_act[4])),
                    ("Evening (5:30 PM)", (e_act[0], e_act[1], e_act[2], lat, lon, e_act[3], e_act[4]))
                ]

        elif "fast" in effective_pace_lower:
            # FAST-PACED: 4 to 5 activities per day (Early Morning, Morning, Afternoon, Sunset, Night)
            if day_plan:
                slots = [
                    ("Early Morning (6:00 AM)", day_plan.get("early_morning", day_plan.get("morning"))),
                    ("Morning (9:30 AM)", day_plan.get("morning")),
                    ("Afternoon (1:30 PM)", day_plan.get("afternoon")),
                    ("Late Afternoon (5:00 PM)", day_plan.get("late_afternoon", day_plan.get("evening"))),
                    ("Evening (7:30 PM)", day_plan.get("evening"))
                ]
            else:
                slots = []
                slot_labels = [
                    "Early Morning (6:00 AM)",
                    "Morning (9:30 AM)",
                    "Afternoon (1:30 PM)",
                    "Late Afternoon (5:00 PM)",
                    "Evening (7:30 PM)"
                ]
                for label in slot_labels:
                    act = GENERIC_INDIAN_ACTIVITIES[generic_idx % len(GENERIC_INDIAN_ACTIVITIES)]
                    generic_idx += 1
                    jitter_lat = lat + (0.006 * (generic_idx % 5 - 2)) if lat != 0 else None
                    jitter_lon = lon + (0.006 * (generic_idx % 4 - 2)) if lon != 0 else None
                    slots.append((label, (act[0], act[1], act[2], jitter_lat, jitter_lon, act[3], act[4])))

        else:
            # MODERATE PACE (DEFAULT): 3 activities per day (Morning, Afternoon, Evening)
            if day_plan:
                slots = [
                    ("Morning (9:00 AM)", day_plan.get("morning")),
                    ("Afternoon (1:30 PM)", day_plan.get("afternoon")),
                    ("Evening (6:30 PM)", day_plan.get("evening"))
                ]
            else:
                slots = []
                slot_labels = ["Morning (9:00 AM)", "Afternoon (1:30 PM)", "Evening (6:30 PM)"]
                for label in slot_labels:
                    act = GENERIC_INDIAN_ACTIVITIES[generic_idx % len(GENERIC_INDIAN_ACTIVITIES)]
                    generic_idx += 1
                    jitter_lat = lat + (0.005 * (generic_idx % 5 - 2)) if lat != 0 else None
                    jitter_lon = lon + (0.005 * (generic_idx % 4 - 2)) if lon != 0 else None
                    slots.append((label, (act[0], act[1], act[2], jitter_lat, jitter_lon, act[3], act[4])))

        for slot_name, item_tuple in slots:
            if not item_tuple:
                continue
            title, desc, loc, i_lat, i_lon, cost, cat = item_tuple
            
            # Form clean slot label (Morning, Afternoon, Evening)
            simplified_slot = "Morning"
            if "afternoon" in slot_name.lower():
                simplified_slot = "Afternoon"
            elif "evening" in slot_name.lower() or "night" in slot_name.lower():
                simplified_slot = "Evening"

            full_title = f"{title}" if destination.lower() in title.lower() else f"{title} ({destination})"
            items.append({
                "day_number": day_num,
                "time_slot": simplified_slot,
                "title": full_title,
                "description": f"[{slot_name}] {desc}",
                "location": f"{loc}, {destination}" if loc and destination not in loc else loc,
                "latitude": i_lat or lat,
                "longitude": i_lon or lon,
                "estimated_cost": float(cost),
                "category": cat,
                "is_completed": False,
                "order_index": order_counter
            })
            order_counter += 1

    return items


def generate_smart_packing_list(
    destination: str,
    days_count: int,
    weather_forecast: Optional[Dict[str, Any]] = None,
    travel_style: str = "Cultural & Heritage"
) -> List[Dict[str, Any]]:
    """Generate dynamic packing checklist specifically tailored for Indian climate and travel."""
    is_rainy = False
    is_cold = False
    is_hot = False

    if weather_forecast and "daily" in weather_forecast:
        for day in weather_forecast["daily"]:
            if day.get("precip_prob", 0) >= 35:
                is_rainy = True
            if day.get("temp_min", 25) < 16:
                is_cold = True
            if day.get("temp_max", 25) > 32:
                is_hot = True

    items = []

    # 1. Documents & Digital Payments
    items.extend([
        {"category": "Documents", "item_name": "Aadhaar Card / Government Photo ID or Passport"},
        {"category": "Documents", "item_name": "UPI Apps setup (Google Pay / PhonePe / Paytm)"},
        {"category": "Documents", "item_name": "IRCTC Train / Flight e-Tickets & Hotel Bookings"},
        {"category": "Documents", "item_name": "Cash (₹2,000–₹5,000 in small denominations for autos & temples)"}
    ])

    # 2. Electronics
    items.extend([
        {"category": "Electronics", "item_name": "Smartphone with reliable Indian 4G/5G SIM"},
        {"category": "Electronics", "item_name": "Heavy-duty Power Bank (10,000–20,000 mAh)"},
        {"category": "Electronics", "item_name": "Charging Cables & Earphones for train/flight journeys"}
    ])

    # 3. Clothing (Tailored to Indian cultural etiquette & weather)
    items.extend([
        {"category": "Clothing", "item_name": "Lightweight breathable cotton kurtas / t-shirts"},
        {"category": "Clothing", "item_name": "Modest temple wear (Dupatta / Scarf to cover head & shoulders)"},
        {"category": "Clothing", "item_name": "Slip-on footwear / sandals (easy to take off outside temples)"},
        {"category": "Clothing", "item_name": f"{min(days_count, 6)}x Undergarments & breathable cotton socks"}
    ])

    if is_cold:
        items.extend([
            {"category": "Clothing", "item_name": "Thermal innerwear & woolen sweater (for chilly mornings/hill stations)"},
            {"category": "Clothing", "item_name": "Warm shawl or windcheater jacket"}
        ])
    else:
        items.append({"category": "Clothing", "item_name": "Light jacket or stole for chilled AC sleeper trains"})

    if is_hot:
        items.extend([
            {"category": "Clothing", "item_name": "UV-protection sunglasses & wide-brim sun cap"},
            {"category": "Toiletries", "item_name": "Sunscreen (SPF 50+ PA+++)"}
        ])

    if is_rainy:
        items.extend([
            {"category": "Gear", "item_name": "Compact windproof umbrella or rain poncho"},
            {"category": "Clothing", "item_name": "Waterproof sandals or floaters"}
        ])

    # 4. Health & Hygiene (India Travel Essentials)
    items.extend([
        {"category": "Health", "item_name": "Odomos / Mosquito repellent cream or roll-on"},
        {"category": "Health", "item_name": "Electrolyte powder / ORS sachets (for hydration)"},
        {"category": "Health", "item_name": "Hand sanitizer & disinfectant wet wipes"},
        {"category": "Health", "item_name": "Travel medicine kit (Digene, Paracetamol, Band-aids, Motion sickness)"}
    ])

    # 5. Toiletries & Gear
    items.extend([
        {"category": "Toiletries", "item_name": "Toothbrush, toothpaste & personal toiletries kit"},
        {"category": "Gear", "item_name": "Reusable insulated water bottle (fill only sealed/RO filtered water)"},
        {"category": "Gear", "item_name": "Lightweight daypack for daily sightseeing"}
    ])

    return items
