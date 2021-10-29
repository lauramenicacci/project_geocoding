import folium
import webbrowser
from folium.plugins import MarkerCluster
import pandas as pd

position_countries = pd.read_csv('position_countries.csv')
lat = position_countries['latitude'].mean()
print(lat)
lon = position_countries['longitude'].mean()

my_map = folium.Map(location = [lat, lon], zoom_start = 4)

for i in range(len(position_countries['longitude'])):
    folium.Marker(
        [position_countries['latitude'][i], position_countries['longitude'][i]],
        tooltip = position_countries['name'][i]).add_to(my_map)

my_map.save("map.html")
webbrowser.open("map.html")
