# convert GeoJSON LineStrings to gpx routes  # Polygons and Points are discarded
import sys
import geojson
import gpxpy

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )

new = gpxpy.gpx.GPX()   #create a new gpx object

answer = input("Do you want to include waypoints also ? Y or N ")

if 'features' in data:
    features = data['features']
    for feature in features:
        geometry_type = feature['geometry'].get('type', None)
        coordinates = feature['geometry'].get('coordinates', None)
        properties = feature.get('properties', None)

        if answer == 'Y' or answer == 'y':
            if geometry_type == 'Point':
                new_wpt = gpxpy.gpx.GPXWaypoint()    # create new point object
                new_wpt.name = properties.get('name') or properties.get('Name') or properties.get('NAME')
                new_wpt.latitude = coordinates[1]
                new_wpt.longitude = coordinates[0]
                if (len(coordinates)) > 2:
                    new_wpt.elevation = coordinates[2]    
                new.waypoints.append(new_wpt)

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
