from pyrebase import pyrebase

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