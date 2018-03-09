from api_tests import WeatherForecast

test = WeatherForecast()
test.geocode_loc('8847 Riverside Drive, Richmond, VA')

loc = test.wForecast()

print(loc['currently']['temperature'])
