# GeoJSON
# convert LineStrings to routes
# Polygons and points are discarded

import sys
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
new = gpxpy.gpx.GPX()   #create a new gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']
    
    if ( geom['type'] == 'LineString' ):
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            new_route = gpxpy.gpx.GPXRoute(apple['name'])
        else:
            new_route = gpxpy.gpx.GPXRoute()
        
        new.routes.append(new_route)

        for j in range(len(node)):
            if (len(node[j])) == 2:
                new_route.points.append(gpxpy.gpx.GPXRoutePoint(node[j][1],node[j][0]))
            else:
                new_route.points.append(gpxpy.gpx.GPXRoutePoint(node[j][1],node[j][0],node[j][2]))   

print( new.to_xml() )


