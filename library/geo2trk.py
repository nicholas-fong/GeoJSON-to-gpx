# GeoJSON
# convert LineStrings to tracks
# Polygons and points are discarded

import sys
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
new = gpxpy.gpx.GPX()    #create a new gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']   
    
    if ( geom['type'] == 'LineString' ):
        banana = data['features'][i]['properties']
        if ( banana.setdefault('name','AAA') != 'AAA' ):    # if properties has name
            new_track = gpxpy.gpx.GPXTrack(banana['name'])  #create a new track object with name
        else:
            new_track = gpxpy.gpx.GPXTrack()  #create a new track object without name
        
        new.tracks.append(new_track)
        new_segment = gpxpy.gpx.GPXTrackSegment()   #create a new track segment
        new_track.segments.append(new_segment)      #append the new segment

        for j in range(len(node)):
            if (len(node[j])) == 2:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0] ))
            else:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0], node[j][2] ))
            
print( new.to_xml() )

