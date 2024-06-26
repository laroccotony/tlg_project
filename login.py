import hashlib
import os

# Hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter a new username: ")
    if user_exists(username):
        print("\033[91m\nError: This username already exists. Please choose a different username.\033[0m\n")
        return

    password = input("Enter a new password: ")
    hashed_password = hash_password(password)

    with open("user_credentials.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")
    print("\033[92m\nRegistration successful.\033[0m\n")

def user_exists(username):
    if os.path.exists("user_credentials.txt"):
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(",", 1)
                if stored_username == username:
                    return True
    return False

def login(username, password):

    hashed_password = hash_password(password)

    if os.path.exists("user_credentials.txt"):
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_hashed_password = line.strip().split(",")
                if stored_username == username and stored_hashed_password == hashed_password:
                    return True
    print("\033[91m\nInvalid username or password.\033[0m\n")
    return False

def main():
    while True:
        choice = input("1: Register\n2: Login\nChoose an option (1 or 2): ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
        else:
            print("\033[91m\nInvalid option, please choose 1 or 2.\033[0m\n")

def main_menu():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if login(username, password):
        return username
    return None

def display_menu(username):
    print("\033[93m\nWelcome, {username}!\033[0m\n")

if __name__ == "__main__":
    user_name = main_menu()
    if user_name:
        display_menu(user_name)

