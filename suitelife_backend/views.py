from flask import render_template, request, session, redirect, url_for
from flask_socketio import send, emit
from suitelife_backend import app, socketio


@app.route('/')
def home():
    return "<h1>Hi, here is our webpage!</h1>"


@socketio.on('message', namespace='/')
def test_message(message):
    message['data']['id'] = app.MESSAGE_NUMBER
    emit('message', message)
    app.MESSAGE_NUMBER += 1
    print message

@socketio.on('my broadcast event', namespace='/')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)
    print message

@socketio.on('connect', namespace='/')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print "Connected!"

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')