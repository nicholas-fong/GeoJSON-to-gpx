import sys
import geojson
from geojson import FeatureCollection, Feature

if len(sys.argv) < 2:
    print("enter a geojson file to convert to geojson file ")
    sys.exit(1)

basket = []       
in_file = open( sys.argv[1] + '.geojson')
data = geojson.load(in_file)
in_file.close()

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

