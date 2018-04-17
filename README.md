# 430 Group Assignment Weather Application

## BRANCH INFO
This branch is for setting up a 10 year data forecast.
This is done by using 10 darksky api calls and decrementing the date that is requested. 

## Setup
### Need to Install:
- [darkskylib](https://github.com/lukaskubis/darkskylib) 
```
pip install darkskylib
```
- [google-maps python api](https://github.com/googlemaps/google-maps-services-python)
```
pip install -U googlemaps
```
- Flask 
```
pip install Flask
pip install flask-socketio
```

### API Keys
- [Dark Sky API](https://darksky.net/dev) : Create an account to get a private key 
- [Google Dev Account](https://developers.google.com/console)
Create a new project and select the geocoding API when getting credentials. 

### API Keys/Request Token
The current test script just references two different files stored locally with the respective dark sky and google maps tokens. 


