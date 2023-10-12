import sys
import re
import geojson
from geojson import FeatureCollection, Feature, dumps

# GeoJSON clean up and pretty print.

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )
infile.close()   

basket = []       
for feature in data['features']:
    basket.append(Feature(geometry=feature['geometry'], properties=feature['properties']))

geojson_string = dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)
# clean up some programs that use different spellings for name
output_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

print(output_string)
with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( output_string )
    
