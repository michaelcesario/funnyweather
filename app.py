from pyrebase import pyrebase
from flask import Flask, jsonify, request
from pushjack import APNSSandboxClient

app = Flask(__name__) #global object for file


config = {
  "apiKey": "AIzaSyCOsBU3ROQlKhuikpRbagIJxl1P7OATfmY",
  "authDomain": "funnyweather-1cf97.firebaseapp.com",
  "databaseURL": "https://funnyweather-1cf97.firebaseio.com/",
  "storageBucket": "funnyweather-1cf97.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

client = APNSSandboxClient(certificate='aps_dev_cert.pem',
                    default_error_timeout=10,
                    default_expiration_offset=2592000,
                    default_batch_size=100)

token = 'd69bd4faa2beca2ff103fb172643d7dfd66304187afcb63cc0ab417856447d33'
alert = 'Hello world.'


@app.route("/hello") #endpoint that clients reach via route
def hello(): #function that will run when client reaches endpoint
    res = client.send(token,
                  alert,
                  badge='badge count',
                  sound='sound to play',
                  category='category',
                  content_available=True,
                  title='Title',
                  title_loc_key='t_loc_key',
                  title_loc_args='t_loc_args',
                  action_loc_key='a_loc_key',
                  loc_key='loc_key',
                  launch_image='path/to/image.jpg',
                  extra={'custom': 'data'})
    return "Hello World!"

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
