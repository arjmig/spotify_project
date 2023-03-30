import json
import geopandas as gpd
import matplotlib.pyplot as plt

# Get select_countries list

with open('fifty_most_populated.json', 'r') as file:
    selected_countries = json.load(file)

# Download world map shapefile

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Get the code iso_3 for every country selected, which is necessary when using geopandas plotting

for n in range(31):
    selected_countries[n] = selected_countries[n][1]

# Create a new column in the GeoDataFrame with a color code different for the two possibilities

world['selected'] = world['iso_a3'].apply(lambda x: 'Country in the analysis'
                                          if x in selected_countries else 'Other country')

fig, ax = plt.subplots()
world.plot(ax=ax, edgecolor='black', linewidth=0.5, scheme=None, column='selected', legend=True,
           cmap='cool')
ax.set_title('Countries selected')
ax.set_axis_off()

# Show a map with the countries selected

plt.show()
