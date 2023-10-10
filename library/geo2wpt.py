# convert GeoJSON Points to gpx waypoints  # LineString and Polygons are discarded
import sys
import gpxpy
import geojson

with open(sys.argv[1]+'.geojson', 'r') as file:
    data = geojson.load(file)

new = gpxpy.gpx.GPX()   #create a gpx object

if 'features' in data:
    features = data['features']
    
    for feature in features:
        geometry_type = feature['geometry'].get('type', None)
        coordinates = feature['geometry'].get('coordinates', None)
        properties = feature.get('properties', None)

        if geometry_type == 'Point':
            new_wpt = gpxpy.gpx.GPXWaypoint()    # create new point object
            new_wpt.name = properties.get('name') or properties.get('Name') or properties.get('NAME')
            new_wpt.latitude = coordinates[1]
            new_wpt.longitude = coordinates[0]
            if (len(coordinates)) > 2:
                new_wpt.elevation = coordinates[2]    
            new.waypoints.append(new_wpt)
            
print( new.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
    