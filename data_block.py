from darksky import forecast
from datetime import datetime as dt

#####################################
# --------- SETUP SECTION --------- #
#####################################

""" Read in your darksky token """
with open('darksky_token','r') as f: 
    ds_key = f.read().strip()


""" These are the coordinates for Fredericksburg, VA """
lat = 38.3031837
lng = -77.4605399



""" Loop through 10 years of the same day 
+ Add it all to list t, of time objects
"""


"""how would you get t from our input though? that's what is tripping me up. """

t = []
for i in range(10):
    t.append(dt((2000+i), 4, 22, 12).isoformat())


""" Loop through 10 years and use the ds API to request it all
+ Add it all to a list of forecast objects """
loc = []
for i in range(10):
    loc.append(forecast(ds_key, lat, lng, t[i]))


# Set it equal to the first entries just to populated them
high_avg = loc[0]['daily']['data'][0]['temperatureHigh']
low_avg = loc[0]['daily']['data'][0]['temperatureLow']

""" Loop through all the objects and pull the data we want """
for i in range(1,10):
    high_avg += loc[i]['daily']['data'][0]['temperatureHigh']
    low_avg += loc[i]['daily']['data'][0]['temperatureLow']

high_avg = high_avg/10
low_avg = low_avg/10

print(high_avg)
print(low_avg)

# loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'])

# This is the darksky forecast call, time is optional

# these are some examples of things 
"""
current = loc['currently']['temperature']
hourlySum = loc['hourly']['summary']
high = loc['daily']['data'][0]['temperatureHigh']
low = loc['daily']['data'][0]['temperatureLow']
"""
