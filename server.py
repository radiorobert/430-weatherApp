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

            # Time_value: 0 = not set, -1 past date, 1 = within two weeks, 2 = future
            time_value = 0 
            print(date)

            print("INPUT\nAddress: {0}\nDate: {1}".format(address,date))

            # Check if future date
            # TODO this could also be past, consider that homie.
            if date != "":
                # automatically just assume it's noon for the response.
                # this isn't really good but you know.
                d = date.split('-')
                date = date + "T12:00:00"

                """ Logic for determining what future thing to use """
                timed = dt(int(d[0]),int(d[1]),int(d[2]))
                t_now = dt.today()

                time_diff = timed - t_now
                if(time_diff.days < 0):
                    time_value = -1
                    print("Processing PAST date")
                elif(time_diff.days > 0 and time_diff.days <= 14):
                    """ here we're just going to use the normal forecast
                    since we're within 2 weeks """
                    time_value = 1
                    print("Processing date within 2 weeks")
                else:
                    time_value = 2
                    print("Processing FUTURE date")


            
            wf.geocode_loc(address)

            # there's two keys in this, one for our data one for darkskies.
            # it's a mess now
            locDat = wf.wForecast(date,time_value)


            return render_template('index.html',
                    forecast_type=wf.forecast_type,
                    addr=address,
                    time=date.split('T')[0],

                    current=locDat['ds_dat']['currently']['temperature'],
                    hourlySum=locDat['ds_dat']['hourly']['summary'],
                    high=locDat['ds_dat']['daily']['data'][0]['temperatureHigh'],
                    low=locDat['ds_dat']['daily']['data'][0]['temperatureLow'],
                    time_ind=time_value)
    else:
        return render_template('index.html')


# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)
