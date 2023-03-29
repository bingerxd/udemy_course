import requests

api_key = "0dc72a72a5c8b19e674db619831c3f21"
parametrs = {"lat": 51.107883, "lon": 17.038538, "appid": api_key}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parametrs)
print(response.status_code)
