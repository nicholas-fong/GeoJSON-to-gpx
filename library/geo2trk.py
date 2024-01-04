# convert GeoJSON LineStrings to gpx tracks  # Points and Polygons are discarded
import sys
import json
import gpxpy

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )

gpx = gpxpy.gpx.GPX()    #create a new gpx object

answer = input("Do you want to include waypoints also ? Y or N ")

if 'features' in data:
    features = data['features']
    for feature in features:
        geometry_type = feature['geometry'].get('type', None)
        coordinates = feature['geometry'].get('coordinates', None)
        properties = feature.get('properties', None)

        if answer == 'Y' or answer == 'y':
            if geometry_type == 'Point':
                new_wpt = gpxpy.gpx.GPXWaypoint()    # create new point object
                new_wpt.name = properties.get('name') or properties.get('Name') or properties.get('NAME')
                new_wpt.latitude = coordinates[1]
                new_wpt.longitude = coordinates[0]
                if (len(coordinates)) > 2:
                    new_wpt.elevation = coordinates[2]    
                gpx.waypoints.append(new_wpt)

        if geometry_type == 'LineString':
            track_name =  properties.get('name') or properties.get('Name') or properties.get('NAME')
            new_track =  gpxpy.gpx.GPXTrack( track_name )        
            gpx.tracks.append( new_track )
            new_segment = gpxpy.gpx.GPXTrackSegment()
            new_track.segments.append(new_segment)
            for item in coordinates:
                if len(item)==2:
                    new_segment.points.append(gpxpy.gpx.GPXTrackPoint(item[1],item[0]))
                else:    
                    new_segment.points.append(gpxpy.gpx.GPXTrackPoint(item[1],item[0],item[2]))

#print( gpx.to_xml() )

with open(sys.argv[1]+'.gpx', 'w') as file:
    file.write( gpx.to_xml() )
    