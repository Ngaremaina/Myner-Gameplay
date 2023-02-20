from mynergameplay import app
from flask import render_template
from mynergameplay.forms import ContactForm
from flask import request
import pandas as pd

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/playlist")
def playlist():
    return render_template('playlist.html')

@app.route("/videos")
def videos():
    return render_template('video.html')

@app.route("/about us")
def about():
    return render_template('about.html')

@app.route("/privacy policy")
def privacy():
    return render_template('privacy.html')

@app.route("/contact us", methods=["GET","POST"])
def contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contat
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        print("The data are saved !")
    else:
        return render_template('contact.html', form=form)