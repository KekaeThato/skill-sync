import pyrebase

firebaseConfig = {"apiKey": "AIzaSyDFui7RW6Xy3yJSIt-dG1qhQPso2u17GVw",
                  "authDomain": "code-clinic-a34a2.firebaseapp.com",
                  "projectId": "code-clinic-a34a2",
                  "storageBucket": "code-clinic-a34a2.firebasestorage.app",
                  "messagingSenderId": "472731779092",
                  "appId": "1:472731779092:web:1b0627769e14b831a3e701",
                  "measurementId": "G-9P9WC36LQ7",
                  "databaseURL": "https://code-clinic-a34a2-default-rtdb.firebaseio.com"
                }

#set up application i.e connect to our firebase project
firebase = pyrebase.initialize_app(firebaseConfig)

#to use the Authenticatio part of the project
auth = firebase.auth()
data_base = firebase.database()

def sign_up()->None:
    """
    This function creates a new user
    """
    try:
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        role = input("What's your role i.e Mentor/Peer : ")
        expertise = input("what's your expertise : ")
        user = auth.create_user_with_email_and_password(email, password)
        data = {"name": name, "email": email, "role": role, "expertise": expertise}
        data_base.child("Users").push(data)
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
# def add_users()
def main():
    user_input = input("Do you have an account ? (y/n)").lower()
    if user_input == "y":
        log_in()
    elif user_input == "n":
        sign_up()
    else:
        return "wrong input try again!"

if __name__ == "__main__":
    main()