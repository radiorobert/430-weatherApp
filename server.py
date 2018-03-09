import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
from WeatherForecast import WeatherForecast 

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

wf = WeatherForecast()

# Main Splash
@app.route('/', methods = ['GET','POST'])
def home():
    address = ""
    date = ""
    
    if request.method == 'POST':
            address = request.form['address']
            date = request.form['date']

            print("INPUT\nAddress: {0}\nDate: {1}".format(address,date))

            wf.geocode_loc(address)
            locDat = wf.wForecast()


            return render_template('index.html',
                    addr=address,
                    time=date,
                    current=locDat['currently']['temperature'])
    else:
        return render_template('index.html')


# start the server
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)
