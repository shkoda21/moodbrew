import requests
from django.conf import settings

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_condition_for_city(city):
    """
    Returns one of: 'rainy', 'sunny', 'cold', 'cloudy', or 'unknown'
    """
    api_key = settings.OPENWEATHER_API_KEY
    if not api_key:
        #print('not api key')
        return None  # caller should handle missing key

    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    try:
        resp = requests.get(OPENWEATHER_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        main = data.get('weather', [{}])[0].get('main', '').lower()
        if 'rain' in main or 'drizzle' in main or 'thunder' in main:
            #print(f"Fetching weather for city={city} → {OPENWEATHER_URL} → {main}")
            return 'rainy'
        if 'clear' in main:
            #print(f"Fetching weather for city={city} → {OPENWEATHER_URL} → {main}")
            return 'sunny'
        if 'snow' in main or 'sleet' in main:
            #print(f"Fetching weather for city={city} → {OPENWEATHER_URL} → {main}")
            return 'cold'
        if 'cloud' in main or 'mist' in main or 'fog' in main:
            #print(f"Fetching weather for city={city} → {OPENWEATHER_URL} → {main}")
            return 'cloudy'
    except requests.RequestException:
        return None
    return 'unknown'
