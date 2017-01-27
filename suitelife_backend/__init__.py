from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__,static_folder='static')
app.config["SECRET_KEY"] = "super secret"
app.MESSAGE_NUMBER = 1
socketio = SocketIO(app)


import suitelife_backend.views
