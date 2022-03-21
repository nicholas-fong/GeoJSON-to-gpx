# GeoJSON
# convert Points to waypoints
# convert polygons to waypoints based on polygon's centroid
# LineStrings are discarded

import sys
from statistics import mean
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
new = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']
    
    if ( geom['type'] == 'Point' ):         # Point, simple lat lon output
        new_wpt = gpxpy.gpx.GPXWaypoint()    # create new point object
        orange = data['features'][i]['properties']
        if ( orange.setdefault('name','AAA') != 'AAA' ): 
            new_wpt.name = orange['name']
        elif ( orange.setdefault('tourism','BBB') != 'BBB' ):
            new_wpt.name = orange['tourism']
        elif ( orange.setdefault('amenity','BBB') != 'BBB' ):
            new_wpt.name = orange['amenity']
        else:
            new_wpt.name = 'noname'

        if (len(node)) == 2:
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
        else:    
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
            new_wpt.elevation = node[2]    
        
        new.waypoints.append(new_wpt)
            

    if ( geom['type'] == 'Polygon' ):     # if Polygon, calculate centroid
        new_wpt = gpxpy.gpx.GPXWaypoint()
        pnode = data['features'][i]['geometry']['coordinates'][0]
        bucket1=[]
        bucket2=[]
        
        for j in range(len(pnode)):
            if j > 0:           # skip first set of coordinates, it is duplicated in the last set
            bucket1.append( pnode[j][1] )
            bucket2.append( pnode[j][0] )
        
        orange = data['features'][i]['properties']
        if ( orange.setdefault('name','noname') != 'noname' ): 
            new_wpt.name = orange['name']
        elif ( orange.setdefault('tourism','notour') != 'notour' ):
            new_wpt.name = orange['tourism']
        elif ( orange.setdefault('amenity','noamen') != 'noamen' ):
            new_wpt.name = orange['amenity']
        else:
            new_wpt.name = 'polygon'
        
        new_wpt.latitude = mean(bucket1)
        new_wpt.longitude = mean(bucket2)
        
        new.waypoints.append(new_wpt)

print( new.to_xml() )
