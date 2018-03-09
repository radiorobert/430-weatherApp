import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')
socketio = SocketIO(app)

# Main Splash
@app.route('/', methods = ['GET','POST'])
def home():

	address = ""
	date = ""
	if request.method == 'POST':
		address = request.form['address']
		date = request.form['date']

	print("Here's the input: {0}\t{1}".format(address,date))

	return render_template('index.html')


############## SOCKETIO ###############
"""
@socketio.on('connect', namespace='/')
def makeConnection():
	print("Connected to Splashpage")


@socketio.on('makeForecast')
def make_forecast(address, date):
	print('Input was {0} and {1}'.format(address,date))
	outputs = {'address': address, 'date': date}
	emit('print_input', outputs)
"""

# start the server
if __name__ == '__main__':
	app.run(host=os.getenv('IP','0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)
