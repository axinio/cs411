import pyrebase

# This api key doesn't really exposed anything based on how firebase is developed
config = {
  "apiKey": "AIzaSyAtV9MoA7mm1LYaFDjBe3aPp8PzHAtrHug",
  "authDomain": "medtomed-25098.firebaseapp.com",
  "databaseURL": "https://medtomed-25098-default-rtdb.firebaseio.com",
  "projectId": "medtomed-25098",
  "storageBucket": "medtomed-25098.appspot.com",
  "messagingSenderId": "366650604466",
  "appId": "1:366650604466:web:f5e0ae90e889857aaec2ab"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def addData(user, curr_data):
    data = {"data":curr_data}
    db.child("users").child(user).set(data)

def replaceData(user, curr_data):
    data = {"data":curr_data}
    db.child("users").child(user).update(data)

def userFinder(user):
    users = db.child("users").get()
    users = users.val()
    if users != None:
        users = users.keys()
        if (user not in users):
            return False
        else:
            return True
    else:
        return False
    
def retrieveData(user):
    current_user_data = db.child("users").child(user).child("data").get()
    current_user_data = current_user_data.val()
    return current_user_data