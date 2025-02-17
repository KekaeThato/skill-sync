import pyrebase

firebaseConfig = {"apiKey": "AIzaSyDFui7RW6Xy3yJSIt-dG1qhQPso2u17GVw",
                  "authDomain": "code-clinic-a34a2.firebaseapp.com",
                  "projectId": "code-clinic-a34a2",
                  "storageBucket": "code-clinic-a34a2.firebasestorage.app",
                  "messagingSenderId": "472731779092",
                  "appId": "1:472731779092:web:28c13b339e6d8360a3e701",
                  "measurementId": "G-LDJ6LNXP0K",
                  "databaseURL": ""
                  }

#set up application i.e connect to our firebase project
firebase = pyrebase.initialize_app(firebaseConfig)

#to use the Authenticatio part of the project
auth = firebase.auth()

def sign_up()->None:
    """
    This function creates a new user
    """
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Email already exist")

def log_in():
    """
    This function logs in if the user exists else throws an exceptions
    """
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        print("Invalid password/Email")

sign_up()