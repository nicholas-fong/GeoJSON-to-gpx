# compact GeoJSON file into one line. Machine readable, more compact, but less human readable

import sys
import geojson
from geojson import FeatureCollection, Feature

if len(sys.argv) < 2:
    print("enter a geojson file to compact ")
    sys.exit(1)

basket = []
      
with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )

for i in range(len(data['features'])):
    my_type = data['features'][i]['geometry']['type']
    my_geometry = data['features'][i]['geometry']
    my_properties = data['features'][i]['properties']

    if my_type == 'Point':
        my_feature = Feature(geometry=my_geometry, properties=my_properties)
        basket.append(my_feature)

    elif my_type == 'LineString':
        my_feature = Feature(geometry=my_geometry, properties=my_properties)
        basket.append(my_feature)   

    elif my_type == 'Polygon':
        my_feature = Feature(geometry=my_geometry, properties=my_properties)
        basket.append(my_feature)   

    elif my_type == 'MultiPolygon':
        my_feature = Feature(geometry=my_geometry, properties=my_properties)
        basket.append(my_feature)          

out_str = str(FeatureCollection(basket)).replace("Name","name").replace("NAME","name")

with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( out_str )

