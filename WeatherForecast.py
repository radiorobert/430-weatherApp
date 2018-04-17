import os
from darksky import forecast
import googlemaps
from datetime import datetime as dt

class WeatherForecast:
    gmaps = None
    geoLoc = {}
    ds_key = ""
    weather_dat = {"ds_dat": {}, "our_dat": {}}
    curr_year = 0
    forecast_type = "current"

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
        curr_year = dt.today().year



    """
    Time comes in like this: YYYY-MM-DD
    """
    def ten_years_data(self,time):

        t = []
        time = time.split('-')
        self.curr_year = dt.today().year
        for i in range(10):
            t.append(dt(self.curr_year - i,int(time[1]),int(time[2].split('T')[0])))


        """ Loop through 10 years and use the ds API to request it all
        + Add it all to a list of forecast objects """
        loc = []
        for i in range(10):
            print("DEBUG {0}".format(t[i]))
            loc.append(forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'], t[i].strftime('%Y-%m-%d' + 'T12:00:00')))


        # Set it equal to the first entries just to populated them
        high_avg = loc[0]['daily']['data'][0]['temperatureHigh']
        low_avg = loc[0]['daily']['data'][0]['temperatureLow']

        """ Loop through all the objects and pull the data we want """
        for i in range(1,10):
            high_avg += loc[i]['daily']['data'][0]['temperatureHigh']
            low_avg += loc[i]['daily']['data'][0]['temperatureLow']

        high_avg = high_avg/10
        low_avg = low_avg/10

        weather_out = {'high_avg': high_avg, 'low_avg':low_avg}

        return weather_out
        

    """
    Reads in address, sets the geoloc dict
    """
    def geocode_loc(self,address):
        # Geocoding an address
        geocode_result = self.gmaps.geocode(address)
        self.geoLoc['lat'] = geocode_result[0]['geometry']['location']['lat']
        self.geoLoc['lng'] = geocode_result[0]['geometry']['location']['lng']
        
    def get_forecast_type(self):
        return self.forecast_type

    """
    Pretty much a wrapper for the darksky forecast

    Returns loc, which is pretty much all the data
    """
    def wForecast(self,time=None,time_value=0): 
        loc = 0
        if time is None:
            # Fetch conditions at input location
            loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'])
            self.forecast_type = "current"
        else:
            if time_value == 1:
                loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'], time)
                self.forecast_type = "two_weeks"
            elif time_value == 2:
                # This is when we run our own algorithm
                # because it's greater than 2 weeks in the future
                loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'], time)
                self.weather_dat['our_dat'] = self.ten_years_data(time)
                self.forecast_type = "future"


        self.weather_dat['ds_dat'] = loc



        return self.weather_dat 

