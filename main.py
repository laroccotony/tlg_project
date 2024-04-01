import requests
from datetime import datetime
# Import the login function from login.py. Make sure login.py is in the same directory.
from login import login
from login import login, register, user_exists  # Ensure to import the register function

def main_menu():
    while True:
        choice = input("1: Login\n2: Register\nChoose an option (1 or 2): ")
        if choice == "1":
            username = input("Username: ")
            if not user_exists(username):
                print("Username does not exist. Please register first.")
                continue
            password = input("Password: ")
            if login(username, password):  # Adjust the login function to accept username and password as arguments
                return username
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            register()  # Call register function directly
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Placeholder functions for API interactions
def fetch_weather_data():
    # This function will use the OpenWeatherMap API
    print("Fetching weather data...")

def get_random_cat_image():
    # This function will use The Cat API
    print("Fetching a random cat image...")

def retrieve_country_data():
    # This function will use the REST Countries API
    print("Retrieving country data...")

def geolocate_ip_address():
    # This function will use the IP Geolocation API
    print("Geolocating IP address...")

def display_menu(username):
    print(f"\nWelcome {username}, the current system time and date is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    while True:
        print("""
1. Fetch Weather Data
2. Get Random Cat Images
3. Country Data
4. Geolocate IP Addresses
5. Logout
        """)
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            fetch_weather_data()
        elif choice == "2":
            get_random_cat_image()
        elif choice == "3":
            retrieve_country_data()
        elif choice == "4":
            geolocate_ip_address()
        elif choice == "5":
            print("Logging out...")
            return  # Return to the main loop, allowing the user to see the main menu again
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    while True:  # This loop allows for re-displaying the main menu after logging out
        user_name = main_menu()
        if user_name:
            display_menu(user_name)
        else:
            break  # Exit the program if main_menu() returns None or a similar condition indicating to stop

