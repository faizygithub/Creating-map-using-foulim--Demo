import folium
import pandas
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'blue'


map2=folium.Map(location=[46.058828,14.506673],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
#for coordinate in [[46,14],[44,12],[43,14]]: # using for loop we can wite multiple marker with explicitly wrriting code for it
for lt,ln ,el in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=coordinate,popup="Hi I'm a Marker",icon=folium.Icon(color="green")))
    #fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+" m",fill_color=color_producer(el),color='grey',fill_opacity=0.7))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
#fg.add_child(folium.Marker(location=[44,12],popup="Hi I'm a Marker",icon=folium.Icon(color="green")))
map2.add_child(fgv)
map2.add_child(fgp)
map2.add_child(folium.LayerControl())                                                                       # for adding another method to the method we can use them between map
map2.save("Map2.html")
