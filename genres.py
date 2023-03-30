##
import requests
from api_token import token, refresh_token
import json

with open('dict_country_artists.json', 'r') as file:
    dict_references = json.load(file)
refresh_token()
headers = {'Authorization': "Bearer " + token}
response = {}

for n in range(len(dict_references)):
    response[n] = []
    for m in range(len(dict_references[str(n)])):
        response[n] += [json.loads(requests.get(url=dict_references[str(n)][m],
                                                headers=headers).text)['genres']]
with open('genres.json', 'w') as file:
    json.dump(response, file)
print('Done')

##

