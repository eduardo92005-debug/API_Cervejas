import requests
import json
import time

BASE_URL = "http://172.24.0.2:5000/playlist/"
def request_spotify_service(input_beer):
    r = requests.get(BASE_URL + input_beer)
    try:
        return json.loads(r.content)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"