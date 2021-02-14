# gpx waypoint is mapped to geoJSON Point
# gpx routes and tracks are mapped to geojson LineString

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
    varname = waypoint.name
    my_point = Point((lon, lat))
    my_feature = Feature(geometry=my_point, properties={"name":varname})
    basket.append(my_feature)    

for track in gpx.tracks: 
    varname = track.name
    for segment in track.segments:
        array=[]
        for point in segment.points:
            array.append( (point.longitude, point.latitude) )
    my_line = LineString(array)
    my_feature = Feature(geometry=my_line, properties={"name":varname})
    basket.append(my_feature)   

for route in gpx.routes: 
    varname = route.name
    array=[]
    for point in route.points:
        array.append( (point.longitude, point.latitude) )    
    my_line = LineString(array)
    my_feature = Feature(geometry=my_line, properties={"name":varname})
    basket.append(my_feature)   

print ( FeatureCollection(basket) )

