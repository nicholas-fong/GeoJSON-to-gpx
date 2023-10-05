# GeoJSON
# convert Points to waypoints
# convert polygons to waypoints based on polygon's centroid
# LineStrings are discarded

import sys
from statistics import mean
import geojson
import gpxpy
import gpxpy.gpx

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )
infile.close()

new = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']
    
    if ( geom['type'] == 'Point' ):         # Point, simple lat lon output
        new_wpt = gpxpy.gpx.GPXWaypoint()    # create new point object
        try:
            myname = data['features'][i]['properties']['name']
        except:
            try:
                myname = data['features'][i]['properties']['Name']
            except:
                myname = 'noname'
        new_wpt.name = myname
        if (len(node)) == 2:
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
        else:    
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
            new_wpt.elevation = node[2]    
        new.waypoints.append(new_wpt)

    if ( geom['type'] == 'Polygon' ):     # if Polygon, calculate centroid and consider it as a Point
        new_wpt = gpxpy.gpx.GPXWaypoint()
        pnode = data['features'][i]['geometry']['coordinates'][0]
        bucket1=[]
        bucket2=[]
        for j in range(len(pnode)-1):
            bucket1.append( pnode[j][1] )
            bucket2.append( pnode[j][0] )
        try:
            myname = data['features'][i]['properties']['name']
        except:
            try:
                myname = data['features'][i]['properties']['Name']
            except:
                myname = 'noname'
        new_wpt.name = myname
        new_wpt.latitude = mean(bucket1)
        new_wpt.longitude = mean(bucket2)
        new.waypoints.append(new_wpt)

print( new.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
