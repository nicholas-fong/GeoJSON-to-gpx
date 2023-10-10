# convert GeoJSON LineStrings to gpx routes  # Polygons and Points are discarded
import sys
import geojson
import gpxpy

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )

new = gpxpy.gpx.GPX()   #create a new gpx object

if 'features' in data:
    features = data['features']
    for feature in features:
        geometry_type = feature['geometry'].get('type', None)
        coordinates = feature['geometry'].get('coordinates', None)
        properties = feature.get('properties', None)
            
        if geometry_type == 'LineString':
            route_name =  properties.get('name') or properties.get('Name') or properties.get('NAME')
            new_route =  gpxpy.gpx.GPXRoute( route_name )        
            new.routes.append(new_route)
            for item in coordinates:
                if len(item)==2:
                    new_route.points.append(gpxpy.gpx.GPXRoutePoint(item[1],item[0]))
                else:    
                    new_route.points.append(gpxpy.gpx.GPXRoutePoint(item[1],item[0],item[2]))

print( new.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
