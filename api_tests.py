import os
from darksky import forecast

# Read in token file for DarkSky
# TODO: add exception if file doesn't exist.
with open('darksky_token','r') as f: 
	key = f.read().strip()

boston = forecast(key, 42.3601, -71.0589)

print(boston['currently']['temperature'])
