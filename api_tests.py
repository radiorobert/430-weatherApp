import os
from darksky import forecast
import googlemaps
from datetime import datetime as dt

WITH_INPUT = True

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
	lat = geocode_result[0]['geometry']['location']['lat']
	lng = geocode_result[0]['geometry']['location']['lng']

	return [lat,lng]
 
"""
Returns the 10-day forcast for a location
If time is input then it will do a future forcast

PARAM: darksky_api token, latitude,longitude
RETURN: location_data
"""
def ds_forecast(darksky_key, lat,lng, time=False):
	if time == False:
		# Fetch conditions at input location
		loc = forecast(darksky_key, lat, lng)
	else:
		loc = forecast(darksky_key, lat, lng, time)

	return loc


def main():

	if not WITH_INPUT:
		address = '1301 College Avenue, Fredericksburg, VA'
		t = dt(2018, 4, 22, 12).isoformat()
	if WITH_INPUT:
		address = input('Input Address: ').strip()
		print(address)
		time = input("Input Date (YYYY/MM/DD/HH): ").split('/')
		if time[0] != "False":
			t = dt(int(time[0]),int(time[1]),int(time[2]),int(time[3])).isoformat()
		else:
			t = dt(2018, 4, 22, 12).isoformat()
		
	keys = read_tokens()
	gmaps = connect_gmaps(keys[0])
	loc = geocode_addr(address, gmaps)
	
	# Forecast with Darksky
	weather_dat = ds_forecast(keys[1],loc[0],loc[1]) 
	
	# Future Forecast
	weather_dat_fut = ds_forecast(keys[1],loc[0],loc[1],t)

	
	# Print the current temperature for requested location.
	print(weather_dat['currently']['temperature'])
	print("---- FUTURE ----")
	print(weather_dat_fut['daily'])

main()
