# https://overpass-turbo.eu/ exports query result to GeoJSON format.
# JOSM can export to GeoJSON format.
# convert GeoJSON Points to gpx waypoints, add elevation if exists.
# convert GeoJSON LineStrings to a gpx track, add elevation if exists.
# convert GeoJSON Polygons to waypoint (based on centroid of the polygon vertices) no elevation.

# code reviewed September 2023

import sys
from statistics import mean
import geojson
import gpxpy
import gpxpy.gpx

if len(sys.argv) < 2:
    print("Please enter a geojson filename. Points, LineStrings and Polygon (centroid) are converted ") 
    sys.exit(1)

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )

new = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']
    
    if ( geom['type'] == 'Point' ):
        new_wpt = gpxpy.gpx.GPXWaypoint()
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            new_wpt.name = apple['name']
        elif ( apple.setdefault('tourism','BBB') != 'BBB' ):
            new_wpt.name = apple['tourism']
        elif ( apple.setdefault('amenity','CCC') != 'CCC' ):
            new_wpt.name = apple['amenity']
        else:   
            new_wpt.name = 'noname'

        if  (len(node)) == 2:
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
        else:
            new_wpt.latitude = node[1]
            new_wpt.longitude = node[0]
            new_wpt.elevation = node[2]
            
        new.waypoints.append(new_wpt)

    if ( geom['type'] == 'LineString' ):
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            new_track = gpxpy.gpx.GPXTrack(apple['name'])   # if properties has name
        else:
            new_track = gpxpy.gpx.GPXTrack()

        new.tracks.append(new_track)
        new_segment = gpxpy.gpx.GPXTrackSegment()   #create a new track segment
        new_track.segments.append(new_segment)      #append the new segment
        
        for j in range(len(node)):
            if (len(node[j])) == 2:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0] ))
            else:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0], node[j][2] ))
                
    if ( geom['type'] == 'Polygon' ):
        new_wpt = gpxpy.gpx.GPXWaypoint()
        pnode = data['features'][i]['geometry']['coordinates'][0]
        bucket1=[]  # use to calculate centroid
        bucket2=[]
        for j in range(len(pnode)-1):  #skip the last node, which is a duplicate of the first node
            bucket1.append( pnode[j][1] )
            bucket2.append( pnode[j][0] )
        
        apple = data['features'][i]['properties']
        if ( apple.setdefault('name','AAA') != 'AAA' ): 
            new_wpt.name = apple['name']
        elif ( apple.setdefault('tourism','BBB') != 'BBB' ):
            new_wpt.name = apple['tourism']
        elif ( apple.setdefault('amenity','CCC') != 'CCC' ):
            new_wpt.name = apple['amenity']
        else:     
            new_wpt.name = 'noname'
            
        new_wpt.latitude = mean(bucket1)
        new_wpt.longitude = mean(bucket2)
        
        new.waypoints.append(new_wpt)
            
print( new.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
