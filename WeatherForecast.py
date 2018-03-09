import os
from darksky import forecast
import googlemaps

class WeatherForecast:
    gmaps = None
    geoLoc = {}
    ds_key = ""

    """
    Creates an instance.
    Reads in the token files for DarkSky and Google Maps API.
    """
    def __init__(self):
        # TODO: add a default look location, or override for file location
        # TODO: add exception if file doesn't exist.
        with open('darksky_token','r') as f: 
            self.ds_key = f.read().strip()

        # Read in token for Google Maps
        with open('gmaps_token','r') as f:
            gmapsKey = f.read().strip()

        # Connect to googlemaps api
        self.gmaps = googlemaps.Client(gmapsKey)

    """
    Reads in address, sets the geoloc dict
    """
    def geocode_loc(self,address):
        # Geocoding an address
        geocode_result = self.gmaps.geocode(address)
        self.geoLoc['lat'] = geocode_result[0]['geometry']['location']['lat']
        self.geoLoc['lng'] = geocode_result[0]['geometry']['location']['lng']
        

    """
    Pretty much a wrapper for the darksky forecast

    Returns loc, which is pretty much all the data
    """
    def wForecast(self,time=None): 
        if time is None:
            # Fetch conditions at input location
            loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'])
        else:
            loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'], time)

        return loc

