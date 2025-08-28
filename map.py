from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
import webbrowser

# Create geolocator
geolocator = Nominatim(user_agent="my_app")

# User input
address1 = input("Enter the first address: ")
address2 = input("Enter the second address: ")

# Get coordinates
location1 = geolocator.geocode(address1)
location2 = geolocator.geocode(address2)

if location1 is None or location2 is None:
    print("One of the addresses was not found. Check the spelling and try again.")
else:
    lat1, lon1 = location1.latitude, location1.longitude
    lat2, lon2 = location2.latitude, location2.longitude

    print(f"{address1}: {lat1}, {lon1}")
    print(f"{address2}: {lat2}, {lon2}")

    # Calculate distance in kilometers
    distance = geodesic((lat1, lon1), (lat2, lon2)).km
    print(f"Distance between the addresses: {distance:.2f} km")

    # Create map with Folium
    m = folium.Map(location=[(lat1+lat2)/2, (lon1+lon2)/2], zoom_start=7)

    # Add markers
    folium.Marker([lat1, lon1], popup=address1).add_to(m)
    folium.Marker([lat2, lon2], popup=address2).add_to(m)

    # Draw a line between the points
    folium.PolyLine([(lat1, lon1), (lat2, lon2)], color="blue", weight=2.5, opacity=1).add_to(m)

    # Save the map
    m.save("map.html")
    print("The map has been saved as map.html. Open it in your browser to view it.")
    webbrowser.open("map.html")