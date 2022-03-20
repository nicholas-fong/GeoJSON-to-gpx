# https://overpass-turbo.eu/ exports query result to GeoJSON format.
# Note: JOSM can read GeoJSON format.
# convert GeoJSON Points to gpx waypoints, add elevation if exists.
# convert GeoJSON LineStrings to a gpx track, add elevation if exists.
# convert GeoJSON Polygons to waypoint (based on centroid of the polygon vertices) no elevtation.

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
        if ( varname != 'noname'):
            gpx_wps.name = varname

        if  (len(geom['coordinates'])) == 2:
            gpx_wps.latitude = geom['coordinates'][1]
            gpx_wps.longitude = geom['coordinates'][0]
        else:
            gpx_wps.latitude = geom['coordinates'][1]
            gpx_wps.longitude = geom['coordinates'][0]
            gpx_wps.elevation = geom['coordinates'][2]
            
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
            if (len(node[j])) == 2:
                gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0] ))
            else:
                gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0], node[j][2] ))
                
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
        if ( varname != 'noname'):
            gpx_wps.name = varname
        gpx_wps.latitude = lat
        gpx_wps.longitude = lon
        
        gpx.waypoints.append(gpx_wps)
            
print( gpx.to_xml() )
