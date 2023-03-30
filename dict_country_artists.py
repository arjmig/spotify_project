##
import requests
from api_token import token, refresh_token
import json

refresh_token()
headers = {'Authorization': "Bearer " + token}

with open('dict_country_tracks.json', 'r') as file:
    dict_country_tracks = json.load(file)

values = list(dict_country_tracks.values())

# Get a list with an api reference for every country top list

request = []
for url in values:
    request += [json.loads(requests.get(url, headers=headers).text)]
    
# Make a dictionary with integer keys, which represents the order of the countries selected.
# Given a key it returns a list with API reference for every track on the top 50 playlist.

dict_0 = {}
for n in range(len(request)):
    dict_0[n] = []
    r = min([len(request[n]['items']), 50])
    for m in range(r):
        dict_0[n] += [request[n]['items'][m]['track']['album']['artists'][0]['href']]
print('Done')

with open('dict_country_artists.json', 'w') as file:
    json.dump(dict_0, file)
