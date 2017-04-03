ef hello():
    return render_template("home.html")

@app.route("/<name>")
#this defines a route for the default page when you get to this part in your app url...run the following
def home_someone(name):
    return render_template("home.html", name=name.title())

#section for user to input address
#work out how to link user input for parameters into Google Maps Static API URL

#OPTION 1:
@app.route("/maps.googleapis.com/maps/api/staticmap?center=<user_spot>&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c", methods=['POST'])
def user_spot():
    print request.form
    form_data = request.form
    print form_data['Place']
#to put the user's address here
    user_spot_map(form_data['Place'])
#to return the google static url with chosen place in
    return "All OK"

#OPTION 2:
payload = {"/maps.googleapis.com/maps/api/staticmap?", {'center':'user_spot', 'zoom':'16', 'size':'400x400','markers':'[set marker one]|[set marker two]', 'key':'AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c'}
r = requests.get('http://maps.googleapis.com/maps/api/staticmap?', params=payload)
print(r.url)

#OPTION 3:
@app.route("/maps.googleapis.com/maps/api/staticmap?center=<user_spot>&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c", methods=['POST'])
def user_spot():
    url = "http:///maps.googleapis.com/maps/api/staticmap?center="+str(user_spot[0])+"&size=640x400&style=element:labels|visibility:off&style=element:geometry.stroke|visibility:off&style=feature:landscape|element:geometry|saturation:-100&style=feature:water|saturation:-100|invert_lightness:true&key=AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c"
    i=0
    print request.form
    form_data = request.form
    print form_data['Place']
#to put the user's address here
    user_spot_map(form_data['Place'])
#to return the google static url with chosen place in
    return url

#OPTION 4:
def _request(self,"/maps.googleapis.com/maps/api/staticmap?",{'center':'user_spot', 'zoom':'16', 'size':'400x400','markers':'[set marker one]|[set marker two]', 'key':'AIzaSyAGCXXvra_pUEjBTEz92VUgAbno-8L4o9c'}, first_request_time=None,retry_counter=0,
        base_url=localhost:5000,accepts_clientid=True,
        extract_body=None, requests_kwargs=None, post_json=None):

authed_url = self._generate_auth_url(url, params, accepts_clientid)

 requests_method = self.session.get
        if post_json is not None:
            requests_method = self.session.post
            final_requests_kwargs["json"] = post_json
        try:
            response = requests_method(base_url + authed_url,
                                       **final_requests_kwargs)


#--------------------------

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
