import requests
import json

BASE_URL = "http://localhost:5000/playlist/"
def request_spotify_service(input_beer):
    r = requests.get(BASE_URL + input_beer)
    return json.loads(r.content)