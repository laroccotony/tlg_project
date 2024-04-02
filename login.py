import hashlib
import os

# Hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ASCII Art for the application
def display_art(text):
    if text == "welcome":
        print("""
  __        __   _          
  \ \      / /__| | ___ ___  _ __ ___   ___   
   \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
    \ V  V /  __/ | (_| (_) | | | | | |  __/ 
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                                           
        """)

# Register a new user
def register():
    username = input("Enter a new username: ")
    if user_exists(username):
        print("Error: This username already exists. Please choose a different username.")
        return  # Exit the function if the user exists

    password = input("Enter a new password: ")
    hashed_password = hash_password(password)

    with open("user_credentials.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")
    print("Registration successful.")

# Add a function to check if a user already exists
def user_exists(username):
    if os.path.exists("user_credentials.txt"):
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",", 1)
                if stored_username == username:
                    return True
    return False

# Adjust the login function to only handle logging in
# and potentially move registration logic to its function if mixed.

# Other parts of login.py remain the same

# Login existing user
# Adjusted login function in login.py
def login(username, password):
    # Assuming you have a hash_password function as before
    hashed_password = hash_password(password)

    if os.path.exists("user_credentials.txt"):
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(",")
                if stored_username == username and stored_hashed_password == hashed_password:
                    print(f"Welcome back, {username}!")
                    return True
    print("Invalid username or password.")
    return False


# Main CLI
def main():
    display_art
    while True:
        choice = input("1: Register\n2: Login\nChoose an option (1 or 2): ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
        else:
            print("Invalid option, please choose 1 or 2.")

# main.py corrected bottom part
if __name__ == "__main__":
    user_name = main_menu()  # This replaces the direct call to login() with the main_menu function.
    if user_name:
        display_menu(user_name)

