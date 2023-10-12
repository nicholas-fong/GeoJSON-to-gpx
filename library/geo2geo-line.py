import sys
import re
import geojson
from geojson import FeatureCollection, Feature, dumps

# GeoJSON extract LineString

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )

basket = []  

for feature in data['features']:
        #geometry_type = feature['geometry'].get('type', None)
        #coordinates = feature['geometry'].get('coordinates', None)
        #properties = feature.get('properties', None)

        if feature['geometry']['type'] == 'LineString':
            basket.append(Feature(geometry=feature['geometry'], properties=feature['properties']))

geojson_string = dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)

improved_geojson_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

print(improved_geojson_string)
with open( sys.argv[1]+'-line.geojson', 'w') as outfile:
    outfile.write( improved_geojson_string )
