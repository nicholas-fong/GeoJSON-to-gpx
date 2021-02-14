# geojson export file e.g. Overpass query
# convert Points to waypoints. convert polygons to waypoints based on polygon's centroid

import sys
from statistics import mean
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
gpx = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    if ( geom['type'] == 'Point' ):    # if Point, simple lat lon output
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        banana = data['features'][i]['properties']
        if ( banana.setdefault('name','noname') != 'noname' ): 
            varname = banana['name']
        elif ( banana.setdefault('tourism','notour') != 'notour' ):
            varname = banana['tourism']
        elif ( banana.setdefault('amenity','noamen') != 'noamen' ):
            varname = banana['amenity']
        else:
            varname = 'noname'
        gpx_wps.latitude = geom['coordinates'][1]
        gpx_wps.longitude = geom['coordinates'][0]
        if ( varname != 'noname'):
            gpx_wps.name = varname
        gpx.waypoints.append(gpx_wps)
            

    if ( geom['type'] == 'Polygon' ):     # if Polygon, calculate centroid
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        node = data['features'][i]['geometry']['coordinates'][0]
        bucket1=[]
        bucket2=[]
        for j in range(len(node)):
            bucket1.append( node[j][1] )
            bucket2.append( node[j][0] )
        lat = mean(bucket1)
        lon = mean(bucket2)
        banana = data['features'][i]['properties']
        if ( banana.setdefault('name','noname') != 'noname' ): 
            varname = banana['name']
        elif ( banana.setdefault('tourism','notour') != 'notour' ):
            varname = banana['tourism']
        elif ( banana.setdefault('amenity','noamen') != 'noamen' ):
            varname = banana['amenity']
        else:
            varname = 'noname'
        gpx_wps.latitude = lat
        gpx_wps.longitude = lon
        if ( varname != 'noname'):
            gpx_wps.name = varname
        gpx.waypoints.append(gpx_wps)

print( gpx.to_xml() )
