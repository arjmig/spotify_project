##
import requests
import base64
import json

with open('secret_variables.json', 'r') as file:
    a = json.load(file)
    client_id = a[0]
    client_secret = a[1]


##
# Request a response with the token to the API

encoded = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " + encoded
}

payload = {
    "grant_type": "client_credentials"
}

response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)

# Get the token from the response
token = json.loads(response.text)['access_token']

# Define a function that gets a new token


def refresh_token():
    response_updated = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
    global token
    token = json.loads(response_updated.text)['access_token']
