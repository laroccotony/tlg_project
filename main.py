from datetime import datetime
from crayons import cyan, magenta
import requests
from api_keys import weather, cat_image
from login import login, register, user_exists

def main_menu():
    while True:
        choice = input("1: Login\n2: Register\nQ: Quit\nChoose an option (1 or 2): ")
        if choice == "1":
            username = input("Username: ")
            if not user_exists(username):
                print("Username does not exist. Please register first.")
                continue
            password = input("Password: ")
            if login(username, password):
                return username
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            register()
        elif choice.lower() == "q":
            print("Exiting program...")
            return None
        else:
            print("Invalid choice. Please enter 1 or 2.")

def fetch_weather_data():
    city = input("Enter the city name: ")
    api_key = weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        temp = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        print(f"\nThe weather in {cyan(city)} is: {cyan(temp)}°C, {cyan(weather_description)}.")
    except requests.RequestException as e:
        print("Error fetching weather data:", e)

def get_random_cat_image():
    api_key = cat_image
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        cat_data = response.json()

        cat_image_url = cat_data[0]['url']
        print(f"Random Cat Image URL: {magenta(cat_image_url)}")
        print("Copy and paste the URL into your browser to view the image.")
    except requests.RequestException as e:
        print("Error fetching cat image:", e)

def retrieve_country_data():
    country_name = input("\nEnter the country name: ")
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        country_data = response.json() 
        country_info = country_data[0]
        capital = country_info['capital'][0] if 'capital' in country_info else 'No capital'
        population = country_info['population']
        region = country_info['region']
        coatOfArms = country_info['flags']['png'] if 'flags' in country_info else 'No coat of arms'
        languages = country_info['languages'] if 'languages' in country_info else 'No languages'
        subregion = country_info['subregion'] if 'subregion' in country_info else 'No subregion'
        maps = country_info['maps']['googleMaps'] if 'maps' in country_info else 'No maps'

        print(f"\033[33mCountry\033[0m: {country_name}")
        print(f"\033[33mCapital\033[0m: {capital}")
        print(f"\033[33mPopulation\033[0m: {population}")
        print(f"\033[33mRegion\033[0m: {region}")
        print(f"\033[33mSubregion\033[0m: {subregion}")
        print(f"\033[33mCoat of Arms\033[0m: {coatOfArms}")
        if isinstance(languages, dict):
            languages = list(languages.values())
        print(f"\033[33mLanguages\033[0m: {', '.join(languages)}")
        print(f"\033[33mGoogle Maps\033[0m: {maps}")
    
    except requests.RequestException as e:
        print("Error fetching country data:", e)

def geolocate_ip_address():
    ip_address = input("\nEnter the IP address: ")
    url = f"https://ipapi.co/{ip_address}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        ip_data = response.json()
        city = ip_data.get('city', 'Not available')
        region = ip_data.get('region', 'Not available')
        country = ip_data.get('country_name', 'Not available')
        isp = ip_data.get('org', 'Not available')
        print(f"\033[32mIP Address\033[0m: {ip_address}")
        print(f"\033[32mCity\033[0m: {city}")
        print(f"\033[32mRegion\033[0m: {region}")
        print(f"\033[32mCountry\033[0m: {country}")
        print(f"\033[32mISP\033[0m: {isp}")
    except requests.RequestException as e:
        print("Error fetching IP geolocation data:", e)

def display_menu(username):
    print(f"\nWelcome {username}, the current system time and date is: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}")
    while True:
        print("""
1. Fetch Weather Data
2. Get Random Cat Images
3. Country Data
4. Geolocate IP Addresses
5. Logout
6. Q: Quit
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
            return
        elif choice.lower() == "q":
            print("Exiting program...")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    while True:
        user_name = main_menu()
        if user_name:
            display_menu(user_name)
        else:
            break
