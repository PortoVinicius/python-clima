from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="brumado"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("WEATHER_API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n***Get current Weather Conditions***\n")

    city = input("Enter the city name: ")

    # Check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "brumado"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
