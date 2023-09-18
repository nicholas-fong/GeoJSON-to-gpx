import sys
import geojson
import json
from geojson import FeatureCollection, Feature, Point, LineString, Polygon

if len(sys.argv) < 2:
    print("enter a geojson file to convert to geojson file ")
    sys.exit(1)

basket = []       

data = geojson.load(open( sys.argv[1] + '.geojson'))

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

geojson_string = json.dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)

clean_str = geojson_string.replace("Name","name").replace("NAME","name")
#print(clean_str)

with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( clean_str )