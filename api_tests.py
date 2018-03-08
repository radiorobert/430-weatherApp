import os
from darksky import forecast
import googlemaps


""" 
Read in token file for DarkSky
Returns a list [gmaps_key, darksky_key]
"""
def read_tokens():
	# TODO: add exception if file doesn't exist.
	with open('darksky_token','r') as f: 
		key = f.read().strip()

	# Read in token for Google Maps
	with open('gmaps_token','r') as f:
		gmapsKey = f.read().strip()

	return [gmapsKey,key]

"""
Connect to googlemaps api
Pass in the token key
Returns a connection to the gmaps api
"""
def connect_gmaps(gmapsKey):
	gmaps = googlemaps.Client(gmapsKey)
	return gmaps

"""
Takes in addresss and geocodes using gmaps api
INPUT: address
OUTPUT: [latitude, longitude]
"""
def geocode_addr(address,gmaps):
	geocode_result = gmaps.geocode(address)
	lat = geocode_result[1]['geometry']['location']['lat']
	lng = geocode_result[1]['geometry']['location']['lng']

	return [lat,lng]
 
"""
Returns the 10-day forcast for a location
PARAM: darksky_api token, latitude,longitude
RETURN: location_data
"""
def ds_forecast(darksky_key, lat,lng):
	# Fetch conditions at input location
	loc = forecast(darksky_key, lat, lng)
	return loc


def main():

	address = '1301 College Avenue, Fredericksburg, VA'
	keys = read_tokens()
	gmaps = connect_gmaps(keys[0])
	loc = geocode_addr(address, gmaps)
	
	weather_dat = ds_forecast(keys[1],loc[0],loc[1]) 
	
	
	
		
	# Print the current temperature for requested location.
	print(weather_dat['currently']['temperature'])

main()
