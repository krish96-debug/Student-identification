import os 

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def authenticate(username, password):
    '''
    Authenticate the user with the given username and pasword .
    Returns True if credentials are valid, otherwise False.'''

    try:
        with open("data/password.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
    except FileNotFoundError:
        print("Error: password.txt file not found")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_user_details(username):
    '''
    Fetch user details from users.txt based on the username.
    Returns a User object if found, otherwise None'''

    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None    
