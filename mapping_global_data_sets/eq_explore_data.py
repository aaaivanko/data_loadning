import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/pp.json'

with open(filename) as jso_file:
    content_data = json.load(jso_file)


content_dict = content_data['features']

mags, lons, lats, hover_text = [], [], [], []

for cont in content_dict:
    mag = cont['properties']['mag']
    lon = cont['geometry']['coordinates'][0]
    lat = cont['geometry']['coordinates'][1]
    title = cont['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global.html')

