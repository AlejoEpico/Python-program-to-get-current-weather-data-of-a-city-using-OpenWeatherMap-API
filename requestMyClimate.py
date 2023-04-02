import requests
from pprint import pprint

API_KEY = '04cbdd4bb433fc1faa5d12400c2871ff'
city = input('Enter a city: ')
base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
weather_data = requests.get(base_url).json()
pprint(weather_data)