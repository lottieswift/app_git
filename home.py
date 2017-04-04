#App Page

#build welcome page with name
#build entry for location
#this needs to link to url

from flask import Flask, request, render_template, redirect
import requests
from urllib import urlencode

app = Flask("safe_spot_app")

#top default section

@app.route("/")
#this defines a route for the default page when you get to this part in your app url
def hello():
    return render_template("home.html")

@app.route("/<name>")
#this defines a route for the default page when you get to this part in your app url...run the following
def home_someone(name):
    return render_template("home.html", name=name.title())

@app.route("/safe_spot", methods=['POST'])
def user_spot():
    print request.form
    form_data = request.form
    place_data = form_data['Place']
    new_url = "https://maps.googleapis.com/maps/api/staticmap?zoom=16&size=400x400&maptype=terrain&markers=color:blue%7Clabel:S%7C51.483785,-0.099857&markers=color:blue%7Clabel:S%7C51.481918,-0.099968&markers=color:blue%7Clabel:S%7C51.486224,-0.100990&center=" + place_data
    #new url is constructed with place_data
    return redirect(new_url, code=302)
    #302 as redirect code

app.run(
    debug= True
)
