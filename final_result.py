##
import json
import pandas as pd
import plotly.express as px

with open('data_as_pandas.json', 'r') as file:
    data_as_pandas = json.load(file)

data_as_pandas = pd.DataFrame(data_as_pandas)


def genitive_word(w):
    if w[-1] == 's':
        return w + "'"
    return w + "'s"


def chart_by_country(name_country):

    fig = px.pie(data_as_pandas[data_as_pandas['0'] == name_country], values='2', names='1', hole=.3,
                 title=f"{genitive_word(name_country)} genre distribution")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()
