"""
Pretty rudimentary script meant to test some core functions in the
Weather Forecast Script

Exits on 1 if there was an error. Check the test.log
"""

import sys, os
import logging
import exceptions

logging.basicConfig( filename="test.log",
                     filemode='a+',
                     level=logging.DEBUG,
                     format= '%(asctime)s - %(levelname)s - %(message)s',
                   )

# pretty sloppy, but allows for importing a module from the main directory
sys.path.append('../')
from WeatherForecast import WeatherForecast

# Changes to the directory where the API tokens are stored for test access
os.chdir('../')

######################################
""" CREATE WEATHER FORECAST OBJECT """

try:
    test = WeatherForecast()
except exceptions.Exception as e:
    logging.error(
    "Exception {exception_class} ({exception_docstring}): {exception_message}".format(
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
exception_message = e.message))
    sys.exit("Error creating WeatherForecast object. More info in test.log.")



######################################
""" TEST GEOCODE OF HARDCODE LOCATION | ERROR 10, bad geocode"""

try:
    test.geocode_loc('Fredericksburg, VA')
except exceptions.Exception as e:
    logging.error(
    "Exception {exception_class} ({exception_docstring}): {exception_message}".format(
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
exception_message = e.message))
    sys.exit("Error parsing location.\n\tMore info in test.log.")

try:
    # These are the latitudes and longitudes of Fredericksburg VA
    assert test.geoLoc['lat'] == 38.3031837, "Latitude didn't match, expected 38.3031837, got {0}\tERRNO: 10".format(test.geoLoc['lat'])
    assert test.geoLoc['lng'] == -77.4605399, "Longitude didn't match, expected 38.3031837, got {0}\tERRNO: 10".format(test.geoLoc['lng'])
except exceptions.Exception as e:
    logging.error(
    "Exception {exception_class} ({exception_docstring}): {exception_message}".format(
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
exception_message = e.message))
    print("Incorrect latitude or longitude. Check log for more info.")


""" TEST CREATION OF FORECAST OBJECT """
try:
    loc = test.wForecast() 
except exceptions.Exception as e:
    logging.error(
    "Exception {exception_class} ({exception_docstring}): {exception_message}".format(
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
exception_message = e.message))
    sys.exit("Error using darksky API weather forecast. Check log for more info.")

try:
    print("The current temperature in Fredericksburg, VA is {0} F.".format(loc['currently']['temperature']))
except exceptions.Exception as e:
    logging.error(
    "Exception {exception_class} ({exception_docstring}): {exception_message}".format(
    exception_class = e.__class__,
    exception_docstring = e.__doc__,
exception_message = e.message))
    sys.exit("Error parsing darksky location dictionary. Could be connection to darksky. Check log for more info.")

print("All functions were successful!")
