import requests

API_KEY = 'e264e603a1031011c3492b4c06c59e99'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
