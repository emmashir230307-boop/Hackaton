from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
import webbrowser

def draw_map(address1,address2,desired_distance):
    match = True
    geolocator = Nominatim(user_agent="my_app")
    location1 = geolocator.geocode(address1)
    location2 = geolocator.geocode(address2)

    if location1 is None or location2 is None:
        print("One of the addresses was not found. Check the spelling and try again.")
    else:
        lat1, lon1 = location1.latitude, location1.longitude
        lat2, lon2 = location2.latitude, location2.longitude

        distance = geodesic((lat1, lon1), (lat2, lon2)).km
        if distance <= desired_distance:
            map = folium.Map(location=[(lat1+lat2)/2, (lon1+lon2)/2], zoom_start=15)

            folium.Marker([lat1, lon1], popup=address1).add_to(map)
            folium.Marker([lat2, lon2], popup=address2).add_to(map)
            folium.PolyLine([(lat1, lon1), (lat2, lon2)], color="blue", weight=2.5, opacity=1).add_to(map)

            map.save("map.html")
            webbrowser.open("map.html")
            return match
        else:
            match = False
            return match

