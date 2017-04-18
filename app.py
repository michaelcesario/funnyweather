from pyrebase import pyrebase
from flask import Flask, jsonify, request
from apns import APNs, Frame, Payload

app = Flask(__name__) #global object for file


config = {
  "apiKey": "AIzaSyCOsBU3ROQlKhuikpRbagIJxl1P7OATfmY",
  "authDomain": "funnyweather-1cf97.firebaseapp.com",
  "databaseURL": "https://funnyweather-1cf97.firebaseio.com/",
  "storageBucket": "funnyweather-1cf97.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

apns = APNs(use_sandbox=True, cert_file='aps_dev_cert.pem', key_file='aps_dev_key.pem')

# Send an iOS 10 compatible notification
token_hex = 'd69bd4faa2beca2ff103fb172643d7dfd66304187afcb63cc0ab417856447d33'
payload = Payload(alert="Hello World!", sound="default", badge=1, mutable_content=True)
apns.gateway_server.send_notification(token_hex, payload)

# Send multiple notifications in a single transmission
frame = Frame()
identifier = 1
expiry = time.time()+3600
priority = 10
frame.add_item('b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87', payload, identifier, expiry, priority)




@app.route("/hello") #endpoint that clients reach via route
def hello(): #function that will run when client reaches endpoint
    apns.gateway_server.send_notification_multiple(frame)
	return "Hello World!";

@app.route("/add_city", methods = ['POST'])
def add_city():
	dict = request.get_json() #save incoming json data from client into dictionary
	city = dict['city']
	weather = dict['weather']
	
	data = {"city":city,"weather":weather}
	db.child("cities").push(data)
	return jsonify(success=True);
	

if __name__ == "__main__": 
	app.run()
