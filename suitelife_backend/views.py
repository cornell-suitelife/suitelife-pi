from flask import render_template, request, session, redirect, url_for
from suitelife_backend import app


@app.route('/')
def home():
    return "<h1>Hi, here is our webpage!</h1>"