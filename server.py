import os
from flask import Flask, render_template, request, session, redirect, url_for
from WeatherForecast import WeatherForecast 
from datetime import datetime as dt

app = Flask(__name__)
#for some reason I had to comment the line below in my code before it can run
#app.secret_key = os.urandom(24).encode('hex')

wf = WeatherForecast()

# Main Splash
@app.route('/', methods = ['GET','POST'])
def home():
    address = ""
    date = "" 
    is_future = False
    
    if request.method == 'POST':
            address = request.form['address']
            date = request.form['date']
            print(date)

            print("INPUT\nAddress: {0}\nDate: {1}".format(address,date))

            # Check if future date
            # TODO this could also be past, consider that homie.
            if date != "":
                # automatically just assume it's noon for the response.
                # this isn't really good but you know.
                date = date + "T12:00:00"
                is_future = True


            wf.geocode_loc(address)
            locDat = wf.wForecast(date)


            return render_template('index.html',
                    addr=address,
                    time=date.split('T')[0],
                    current=locDat.temperature,
                    #hourlySum=locDat['hourly']['summary'],
                    #high=locDat['daily']['data'][0]['temperatureHigh'],
                    #low=locDat['daily']['data'][0]['temperatureLow'],
                    isFuture=is_future)
    else:
        return render_template('index.html')


# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)
