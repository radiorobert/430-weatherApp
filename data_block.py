from darksky import forecast
from datetime import datetime as dt


""" Read in your darksky token """
with open('darksky_token','r') as f: 
    ds_key = f.read().strip()


""" These are the coordinates for Fredericksburg, VA """
lat = 38.3031837
lng = -77.4605399



""" year, month, day, hour """
t = dt(2018, 4, 22, 12).isoformat()

data = 10
count = 0 
high = [0] * 10
low = [0] * 10 
humidy =[0] * 10 
dewpoint = [0] * 10 

while count < data: 
	
	loc = forecast(ds_key, lat, lng, t)
	print(count)
	high[count] = loc['daily']['data'][0]['temperatureHigh']
	print(t.year)
	t[0] = t[0] - 1 
	
print(high)

# loc = forecast(self.ds_key, self.geoLoc['lat'], self.geoLoc['lng'])

# This is the darksky forecast call, time is optional
loc = forecast(ds_key, lat, lng, t)

# these are some examples of things 
current = loc['currently']['temperature']
hourlySum = loc['hourly']['summary']
high = loc['daily']['data'][0]['temperatureHigh']
low = loc['daily']['data'][0]['temperatureLow']

print(current, hourlySum, high, low)
