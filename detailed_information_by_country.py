##
import json
with open('genres.json', 'r') as file:
    genres = list(json.load(file).values())

with open('countries_selected.json', 'r') as file:
    countries_selected = json.load(file)
g = []
for r in countries_selected:
    g += [r[3]]
countries_selected = g

# The following function outputs a list with the different genres that appear on 50 top playlist,
# with the number of votes that have received from the tracks on that playlist. A vote from a track
# means that a genre appears on that track.


def country_list(country_name):
    try:
        index = countries_selected.index(country_name)
        genres_add_up = genres[index]

    # In order to avoid overrepresentation, every list representing a track only can cast "a vote".
    # In other words, if a track has multiple genres, to say, 5, every genre will get 1/5 of a vote.

        g = []
        for r in genres_add_up:
            g += [[x, (1/len(r))] for x in r]
        g_0 = list(set([x[0] for x in g]))
        g_1 = []
        v = 0
        for r in g_0:
            for s in g:
                if s[0] == r:
                    v += s[1]
            g_1 += [[r, v]]

        g = g_1
        g.sort(key=lambda x: len(x[0]), reverse=True)

    # Other important question is overlapping among genres. For example, "rock", "pop" and "pop rock".
    # The way to treat this issue is just make a "loot partition", so given that the words "pop" and
    # "rock" appear in "pop rock", the votes of the latter will be divided among the formers.
    # After this, "pop rock" will be removed from our data.

        j = 0
        k_0 = []
        while j < len(g):
            k_1 = []
            for r in g[j+1:]:
                if r[0] in g[j][0]:
                    k_1 += [r[0]]
            k_0 += [k_1]
            j += 1

        g_as_dict = dict(g)

        for n in range(len(k_0)):
            if k_0[n]:
                l = len(k_0[n])
                r = (g[n][1]) / l
                for m in k_0[n]:
                    g_as_dict[m] += r
                g_0.remove(g[n][0])

        conversion_to_list = []
        for element in g_0:
            conversion_to_list += [[element, g_as_dict[element]]]

        return conversion_to_list

    except ValueError:
        print(f'There is no Spotify 50 top playlist available in that country')


detailed_information_by_country = {}
for element in countries_selected:
    detailed_information_by_country[element] = country_list(element)

with open('detailed_information_by_country.json', 'w') as file:
    json.dump(detailed_information_by_country, file)

##

