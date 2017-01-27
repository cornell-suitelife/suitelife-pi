"""
This script runs the suitelife_backend application using a development server.
"""

from os import environ
from flask_socketio import SocketIO, emit
from suitelife_backend import app, socketio


if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = 5555
    #except ValueError:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #app.run(HOST, PORT)
    socketio.run(app, host='0.0.0.0')