import requests
from pprint import pprint

API_key = '5f92922319455b8a0e4f9434ee33ef3e'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+API_key

weather_data = requests.get(base_url).json()

pprint(weather_data)
