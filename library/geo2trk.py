# geojson export file e.g. Overpass query
# convert LineStrings to tracks. Polygons and points are ignored

import sys
import geojson
import gpxpy
import gpxpy.gpx

data = geojson.load(open( sys.argv[1] + '.geojson'))
gpx = gpxpy.gpx.GPX()   #create a gpx object

for i in range(len(data['features'])):
    if ( data['features'][i]['geometry']['type'] == 'LineString' ):
        banana = data['features'][i]['properties']
        if ( banana.setdefault('name','noname') != 'noname' ): 
            varname = banana['name']
        elif ( banana.setdefault('tourism','notour') != 'notour' ):
            varname = banana['tourism']
        else:
            varname = 'noname'
 
        if (varname == 'noname'):
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

