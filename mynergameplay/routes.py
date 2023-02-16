from mynergameplay import app
from flask import render_template

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

@app.route("/videos")
def videos():
    return render_template('video.html')