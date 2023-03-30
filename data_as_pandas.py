##
import json
import pandas as pd
from pandas import NA as NA

with open('detailed_information_by_country.json') as file:
    detailed_information_by_country = json.load(file)

for list_0 in detailed_information_by_country:
    while len(detailed_information_by_country[list_0]) < 10:
        detailed_information_by_country[list_0] += [[NA, NA]]

l_0 = list(detailed_information_by_country.keys())
l_1 = list(detailed_information_by_country.values())
##
t = []
for n in range(31):
    r = []
    for s in l_1[n]:
        r += [[l_0[n]] + s]
    t += r

detailed_information_by_country = t

pd.DataFrame(detailed_information_by_country).to_json('data_as_pandas.json')

##

