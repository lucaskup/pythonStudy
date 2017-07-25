import folium
import pandas

def color(df,elev):
    minimum = int(min(df['ELEV']))
    maximum = int(max(df['ELEV']))
    step = int((maximum - minimum)/3)
    if elev in range(minimum,minimum+step):
        col = 'green'
    elif elev in range(minimum+step,minimum+step*2):
        col = 'orange'
    else:
        col = 'red'
    return col

df = pandas.read_csv('Volcanoes-USA.txt')
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6, tiles = 'Mapbox Bright')

fg = folium.FeatureGroup(name='Volcanoes-USA')
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
        fg.add_child(folium.Marker(location=[lat,lon],popup=name, icon = folium.Icon(color=color(df,elev))))
#map.simple_marker(location=[45.3311,-121.7311],popup='Timberlake Lodge', marker_color='green')
map.add_child(fg)
map.add_child(folium.GeoJson(data=open('geojson.json'),
name='World Population',
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if x['properties']['POP2005']<=20000000 else 'red' }))
map.add_child(folium.LayerControl())

map.save(outfile='test.html')
