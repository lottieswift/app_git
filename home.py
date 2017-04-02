#App Page

#build welcome page with name
#build entry for location
#this needs to link to url

from flask import Flask, request, render_template
import requests
from urllib import urlencode
#this is way you are able to import different modules and libraries to use
app = Flask("safe_spot")

@app.route("/")
#this defines a route for the default page when you get to this part in your app url...run the following
def hello():
    return render_template("home.html")

@app.route("/<name>")
#this defines a route for the default page when you get to this part in your app url...run the following
def home_someone(name):
    return render_template("home.html", name=name.title())

#to enter the user_spot
@app.route("/maps.googleapis.com/maps/api/staticmap?center=<user_spot>&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c", methods=['POST'])
def user_spot():
    print request.form
    form_data = request.form
    print form_data['Place']
#to put the user's address here
    user_spot_map(form_data['Place'])
#to return the google static url with chosen place in
    return "All OK"


def user_spot_map(Place):
    #how to take the user address, and return it in the address?
    return render_template("welcome.html", Place=Place.title())


#-----

#set up the email contact
def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox61044a42a32a43f1851ce3532eba9064.mailgun.org/messages",
        auth=("api", "key-c6afc7a40392f81eb5065008c3278897"),
        data={"from": "Excited User <mailgun@sandbox61044a42a32a43f1851ce3532eba9064.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness, to you {name}"})

app.run(
    debug= True
)
