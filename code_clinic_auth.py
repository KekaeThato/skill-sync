import pyrebase, click, time
from config import FIREBASECONFIG

firebaseConfig = FIREBASECONFIG

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
        name = click.prompt("Enter your name ")
        email = click.prompt("Enter your email ")
        password = click.prompt("Enter your password ")
        role = click.prompt("What's your role i.e Mentor/Peer ")
        expertise = click.prompt("what's your expertise ")
        user = auth.create_user_with_email_and_password(email, password)
        data = {"name": name, "email": email, "role": role, "expertise": expertise}
        data_base.child("Users").push(data)
        click.echo("\nSuccessfully signed up,Now login")
        log_in()
    except:
        click.echo("Email already exist")

def log_in()->None:
    """
    This function logs in if the user exists else throws an exceptions
    """
    email = click.prompt("Enter your email ")
    password = click.prompt("Enter your password ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        click.echo("\nSuccessfully logged in")
    except:
        click.echo("Invalid password/Email")
def update_users(user:str)->None:
    pass

def view_workshop():
    pass

def request_meeting(requestor:str)->None:

    topic = click.prompt("Enter the topic you want assistance in ")
    date_requested = click.prompt("Enter the date you want your meet in this format(day/month/year)")
    data ={"requestor_id":requestor, "topic":topic, "date_requested":date_requested}
    data_base.child("Meetings").push(data)



def view_bookings():
    pass

def cancel_booking():
    pass


def main()->None:
    user_input = click.prompt("Do you have an account ? (y/n)")
    if user_input == "y":
        log_in()
    elif user_input == "n":
        sign_up()
    else:
        click.echo("wrong input try again!")

if __name__ == "__main__":
    main()