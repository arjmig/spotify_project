##
import requests
import json
from api_token import token, refresh_token
##
# Get a list with the different countries in which Spotify is available
refresh_token()
url_market_countries = "https://api.spotify.com/v1/markets"
headers = {'Authorization': "Bearer " + token}
market_list_call = requests.get(url=url_market_countries, headers=headers)
market_list = json.loads(market_list_call.text)['markets']

# Load the list of lists [iso_2, iso_3, population] of the different countries

with open('countries_by_population.json', 'r') as file:
    countries_by_population = json.load(file)

# Make a request to get the 50 most populated countries in which Spotify is available.
url_search = 'https://api.spotify.com/v1/search?include_external=audio'
headers = {'Authorization': 'Bearer ' + token}
id_tracks_by_country = {}
playlist_by_country = {}
countries_selected = [country for country in countries_by_population if country[0] in market_list]
countries_selected = countries_selected[:50]

# Write a json with the list above.

# Make a dictionary with the selected countries. Items will be tracks from the top 50 songs playlist
# by country.

dict_country_tracks = {}
countries_with_no_playlist = []
for iso_2, iso_3, population, country_name in countries_selected:
    query_params = {
        "q": f"top 50-{country_name}",
        "type": "playlist",
        "limit": 15,
        'market': f'{iso_2}'
    }

    raw_requested_playlist_response = requests.get(url=url_search,
                                                   headers=headers, params=query_params)

    raw_playlist = json.loads(raw_requested_playlist_response.text)['playlists']['items']
    length = len(raw_playlist)
    if length == 0:
        print(f'Problem with {country_name} availability')
        continue
    for n in range(length):
        if 'Your daily update of the most played tracks right now' in raw_playlist[n]['description']:
            dict_country_tracks[iso_2] = raw_playlist[n]['tracks']['href']
            break
        if n == (length - 1):
            countries_with_no_playlist += [iso_2]
# Save as a json dict_country_tracks
countries_selected = [x for x in countries_selected if not(x[0] in countries_with_no_playlist)]

with open('dict_country_tracks.json', 'w') as file:
    json.dump(dict_country_tracks, file)

with open('countries_selected.json', 'w') as file:
    json.dump(countries_selected, file)
