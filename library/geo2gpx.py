# https://overpass-turbo.eu/ exports GeoJSON
# josm can also export to GeoJSON
# convert GeoJSON Points to gpx waypoints
# convert GeoJSON Polygons to a single gpx waypoint based on centroid of the polygon vertices
# convert GeoJSON LineStrings to a gpx track

import sys
from statistics import mean
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
gpx = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    if ( geom['type'] == 'Point' ):
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','noname') != 'noname' ): 
            varname = apple['name']
        elif ( apple.setdefault('tourism','notour') != 'notour' ):
            varname = apple['tourism']
        elif ( apple.setdefault('amenity','noamen') != 'noamen' ):
            varname = apple['amenity']
        else:
            varname = 'noname'
        gpx_wps.latitude = geom['coordinates'][1]
        gpx_wps.longitude = geom['coordinates'][0]
        if ( varname != 'noname'):
            gpx_wps.name = varname
        gpx.waypoints.append(gpx_wps)
            
    if ( geom['type'] == 'Polygon' ):
        gpx_wps = gpxpy.gpx.GPXWaypoint()
        node = data['features'][i]['geometry']['coordinates'][0]
        bucket1=[]  # use to calculate centroid
        bucket2=[]
        for j in range(len(node)):
            bucket1.append( node[j][1] )
            bucket2.append( node[j][0] )
        lat = mean(bucket1)
        lon = mean(bucket2)
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','noname') != 'noname' ): 
            varname = apple['name']
        elif ( apple.setdefault('tourism','notour') != 'notour' ):
            varname = apple['tourism']
        elif ( apple.setdefault('amenity','noamen') != 'noamen' ):
            varname = apple['amenity']
        else:
            varname = 'noname'
        gpx_wps.latitude = lat
        gpx_wps.longitude = lon
        if ( varname != 'noname'):
            gpx_wps.name = varname
        gpx.waypoints.append(gpx_wps)
            
    if ( data['features'][i]['geometry']['type'] == 'LineString' ):
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','noname') != 'noname' ): 
            varname = apple['name']
        elif ( apple.setdefault('tourism','notour') != 'notour' ):
            varname = apple['tourism']
        else:
            varname = 'noname'
        if ( varname == 'noname' ):
            gpx_track = gpxpy.gpx.GPXTrack()
        else:    
            gpx_track = gpxpy.gpx.GPXTrack(varname)
        gpx.tracks.append(gpx_track)
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)
        node = data['features'][i]['geometry']['coordinates']
        gpx_point=gpxpy.gpx.GPXTrackPoint()
        for j in range(len(node)):
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0] ))

print( gpx.to_xml() )
