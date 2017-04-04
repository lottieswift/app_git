#App Page

#build welcome page with name
#build entry for location
#this needs to link to url

from flask import Flask, request, render_template
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

url = "/maps.googleapis.com/maps/api/staticmap?center=<user_spot>&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c"

#OR THIS....??
payload = {"/maps.googleapis.com/maps/api/staticmap?", {'center':'user_spot', 'zoom':'16', 'size':'400x400','markers':'[set marker one]|[set marker two]', 'key':'AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c'}
r = requests.get('http://maps.googleapis.com/maps/api/staticmap?', params=payload)
print(r.url)

@app.route("/url", methods=['POST'])
def user_spot():
    print request.form
    form_data = request.form
    print form_data['Place']
#to put the user's address here
    x = user_spot_map(form_data['Place'])
    print x
    return x

app.run(
    debug= True
)
