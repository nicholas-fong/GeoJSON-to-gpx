# GeoJSON
# convert LineStrings to tracks
# Points and Polygons are discarded

# code reviewed September 2023

import sys
import geojson
import gpxpy
import gpxpy.gpx

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )
infile.close()   

new = gpxpy.gpx.GPX()    #create a new gpx object

for i in range(len(data['features'])):
    geom = data['features'][i]['geometry']
    node = geom['coordinates']   
    
    if ( geom['type'] == 'LineString' ):
        try:
            myname = data['features'][i]['properties']['name']
        except:
            try:
                myname = data['features'][i]['properties']['Name']
            except:
                try:
                    myname = data['features'][i]['properties']['NAME']
                except:    
                    myname = 'noname'

        new_track = gpxpy.gpx.GPXTrack(myname)  #create a new track object
        new.tracks.append(new_track)
        new_segment = gpxpy.gpx.GPXTrackSegment()   #create a new track segment
        new_track.segments.append(new_segment)      #append the new segment

        for j in range(len(node)):
            if (len(node[j])) == 2:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0] ))
            else:
                new_segment.points.append(gpxpy.gpx.GPXTrackPoint(node[j][1], node[j][0], node[j][2] ))
            
print( new.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( new.to_xml() )
    