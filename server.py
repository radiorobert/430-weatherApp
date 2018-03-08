import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')
socketio = SocketIO(app)

# Main Splash
@app.route('/', methods = ['GET','POST'])
def home():
	return render_template('index.html')


# start the server
if __name__ == '__main__':
	socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
