##
import requests
from bs4 import BeautifulSoup
import json
response = requests.get('http://www.geonames.org/countries/')
soup = BeautifulSoup(response.content, 'html.parser')
# find all instances of the <h1> tag
h1_tags = soup.find_all("td")

# print the text inside each <h1> tag
list_0 = []
for tag in h1_tags:
    list_0 += [tag.text]
del list_0[0]
del list_0[0]
list_iso_2 = []
for a in range(250):
    list_iso_2 += [list_0[a*9]]
list_population = []
for a in range(250):
    s = [a for a in list_0[7 + a*9]]
    while ',' in s:
        s.remove(',')
    while '.' in s:
        s.remove('.')
    list_population += [int(''.join(s))]
list_iso_3 = []
for a in range(250):
    list_iso_3 += [list_0[1 + a*9]]
list_iso_4 = []
for a in range(250):
    list_iso_4 += [list_0[4 + a*9]]
pairs_iso_pop = []
for n in range(250):
    pairs_iso_pop += [[list_iso_2[n], list_iso_3[n], list_population[n], list_iso_4[n]]]
countries_by_population = sorted(pairs_iso_pop, key=lambda x: x[2], reverse=True)
with open('countries_by_population.json', 'w') as file:
    json.dump(countries_by_population, file)
