import os
from darksky import forecast
import googlemaps

# Read in token file for DarkSky
# TODO: add exception if file doesn't exist.
with open('darksky_token','r') as f: 
	key = f.read().strip()

# Read in token for Google Maps
with open('gmaps_token','r') as f:
	gmapsKey = f.read().strip()


# Connect to googlemaps api
gmaps = googlemaps.Client(gmapsKey)

# Geocoding an address
geocode_result = gmaps.geocode('1301 College Avenue, Fredericksburg, VA')
lat = geocode_result[1]['geometry']['location']['lat']
lng = geocode_result[1]['geometry']['location']['lng']
 
# Fetch conditions at input location
loc = forecast(key, lat, lng)


# Print the current temperature for requested location.
print(loc['currently']['temperature'])

