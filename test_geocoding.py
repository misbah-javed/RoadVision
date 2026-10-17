import certifi
from geopy.geocoders import Nominatim

geolocator = Nominatim(
    user_agent="roadvision_learning_project",
    ssl_context=__import__("ssl").create_default_context(
        cafile=certifi.where()
    ),
)

place = geolocator.geocode("Delhi, India", timeout=20)

if place:
    print("Place found:", place.address)
    print("Latitude:", place.latitude)
    print("Longitude:", place.longitude)
else:
    print("Place not found.")


