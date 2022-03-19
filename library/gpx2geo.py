# gpx waypoint is mapped to geoJSON Point
# gpx routes and tracks are mapped to geojson LineString
# gpx elevation is added as the third parameter in geometry

import sys
import gpxpy
import gpxpy.gpx
from geojson import FeatureCollection, Feature, Point, LineString

filename = (sys.argv[1]+'.gpx')
with open( filename ) as infile:
    gpx = gpxpy.parse(infile)
    
basket = []    

for waypoint in gpx.waypoints:
    lat = float(waypoint.latitude)
    lon = float(waypoint.longitude)
    ele = int(waypoint.elevation)
    varname = waypoint.name
    my_point = Point((lon, lat, ele))
    my_feature = Feature(geometry=my_point, properties={"name":varname})
    basket.append(my_feature)    

for track in gpx.tracks: 
    varname = track.name
    for segment in track.segments:
        array=[]
        for point in segment.points:
            array.append( (point.longitude, point.latitude, point.elevation) )
        my_line = LineString(array)
        my_feature = Feature(geometry=my_line, properties={"name":varname})
        basket.append(my_feature)   

for route in gpx.routes: 
    varname = route.name
    array=[]
    for point in route.points:
        array.append( (point.longitude, point.latitude, point.elevation) )    
    my_line = LineString(array)
    my_feature = Feature(geometry=my_line, properties={"name":varname})
    basket.append(my_feature)   

print ( FeatureCollection(basket) )

