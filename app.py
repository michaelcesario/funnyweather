from pyrebase import pyrebase
from flask import Flask, jsonify, request
from pyfcm import FCMNotification

app = Flask(__name__) #global object for file


config = {
  "apiKey": "AIzaSyCOsBU3ROQlKhuikpRbagIJxl1P7OATfmY",
  "authDomain": "funnyweather-1cf97.firebaseapp.com",
  "databaseURL": "https://funnyweather-1cf97.firebaseio.com/",
  "storageBucket": "funnyweather-1cf97.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

push_service = FCMNotification(api_key="AAAAOkKnKuU:APA91bHV-cbWn_zGoWcMsIyUb2Vs1TKYh2wk1STLDnRu76O9ADSPgNMIlQkE92M02vfAOTLyvHhM_KG7DQ3l-9cpTMfo2FSkZHxSoSWN-M4G2c5VkG7-lS0HFI1zJfp0sB0Cg42kmxKJ")


@app.route("/hello") #endpoint that clients reach via route
def hello(): #function that will run when client reaches endpoint
    registration_id = "cHzRiWhEqM4:APA91bGpJLlJSlv9T5WjV9uKrI6HPUWZLwHY-t7Q6M2Jvf5nETq3BgCCr0Rtb4a2vqEt6rTIDpWw85t4Q_wsneYZabbnRFeC9KUVGk7oSlL1l9rUJaMs32Je3-tJKKtzBzDyVtSF0EeJ"
    message_title = "update"
    message_body = "test body"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
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
