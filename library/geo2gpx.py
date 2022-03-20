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
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            gpx_wps.name = apple['name']
        elif ( apple.setdefault('tourism','BBB') != 'BBB' ):
            gpx_wps.name = apple['tourism']
        elif ( apple.setdefault('amenity','CCC') != 'CCC' ):
            gpx_wps.name = apple['amenity']
        else:   
            gpx_wps.name = 'noname'

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
        if ( apple.setdefault('name','BBB') != 'BBB' ): 
            gpx_track = gpxpy.gpx.GPXTrack(apple['name'])
        elif ( apple.setdefault('tourism','CCC') != 'CCC' ):
            gpx_track = gpxpy.gpx.GPXTrack(apple['tourism'])
        else:
            gpx_track = gpxpy.gpx.GPXTrack('noname')

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
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            gpx_wps.name = apple['name']
        elif ( apple.setdefault('tourism','BBB') != 'BBB' ):
            gpx_wps.name = apple['tourism']
        elif ( apple.setdefault('amenity','CCC') != 'CCC' ):
            gpx_wps.name = apple['amenity']
        else:     
            gpx_wps.name = 'noname'
            
        gpx_wps.latitude = mean(bucket1)
        gpx_wps.longitude = mean(bucket2)
        
        gpx.waypoints.append(gpx_wps)
            
print( gpx.to_xml() )
