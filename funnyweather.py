from pyrebase import pyrebase
from flask import Flask, jsonify, request
config = {
  "apiKey": "AIzaSyCOsBU3ROQlKhuikpRbagIJxl1P7OATfmY",
  "authDomain": "funnyweather-1cf97.firebaseapp.com",
  "databaseURL": "https://funnyweather-1cf97.firebaseio.com/",
  "storageBucket": "funnyweather-1cf97.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("cities").push("Toronto")

print("Hello, World!")

app = Flask(__name__) #global object for file

@app.route("/hello") #endpoint that clients reach via route
def hello(): #function that will run when client reaches endpoint
	return "Hello World!";

@app.route("/add_user")#, methods = ['POST'])
def add_user():
	#dict = request.get_json() #save incoming json data from client into dictionary
	#username = dict['username']
	#email = dict['email']
	db.child("cities").push("Toronto")	
	

if __name__ == "__main__": 
	app.run()
