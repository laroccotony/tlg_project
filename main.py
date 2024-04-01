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
    city = input("Enter the city name: ")
    api_key = "5643450b393b6370c42a23b189715aba"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        weather_data = response.json()

        # Extract and print some data
        temp = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C, {weather_description}.")
    except requests.RequestException as e:
        print("Error fetching weather data:", e)


def get_random_cat_image():
    api_key = "live_X0BZo5UefOAxA2ONfc54iic4CDfubQUfF2HzHIhpaU9rrquoDhyTkb1UdNzcnupk"  # Replace with your actual The Cat API key
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key}  # The Cat API requires the API key in the request header

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        cat_data = response.json()

        # Extract and print the image URL
        cat_image_url = cat_data[0]['url']
        print(f"Random Cat Image URL: {cat_image_url}")
        print("Copy and paste the URL into your browser to view the image.")
    except requests.RequestException as e:
        print("Error fetching cat image:", e)

def retrieve_country_data():
    country_name = input("Enter the country name: ")
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        country_data = response.json()

        # Extract and print some country data
        country_info = country_data[0]
        capital = country_info['capital'][0] if 'capital' in country_info else 'No capital'
        population = country_info['population']
        region = country_info['region']
        subregion = country_info['subregion'] if 'subregion' in country_info else 'No subregion'
        print(f"Country: {country_name}")
        print(f"Capital: {capital}")
        print(f"Population: {population}")
        print(f"Region: {region}")
        print(f"Subregion: {subregion}")
    except requests.RequestException as e:
        print("Error fetching country data:", e)

def geolocate_ip_address():
    ip_address = input("Enter the IP address: ")
    url = f"https://ipapi.co/{ip_address}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        ip_data = response.json()

        # Extract and print some geolocation data
        city = ip_data.get('city', 'Not available')
        region = ip_data.get('region', 'Not available')
        country = ip_data.get('country_name', 'Not available')
        isp = ip_data.get('org', 'Not available')
        print(f"IP Address: {ip_address}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"ISP: {isp}")
    except requests.RequestException as e:
        print("Error fetching IP geolocation data:", e)

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

