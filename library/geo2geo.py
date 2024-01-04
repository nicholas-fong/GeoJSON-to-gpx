import sys
import re
import json
from geojson import FeatureCollection, Feature

# GeoJSON clean up and pretty print.

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )
infile.close()     # explicit close because I will use this file again.

features = []       
for feature in data['features']:
    features.append(Feature(geometry=feature['geometry'], properties=feature['properties']))

geojson_string = json.dumps(FeatureCollection(features), indent=2, ensure_ascii=False)
# clean up some programs that use different spellings for name, make all of them lowercase name
clean_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

print(clean_string)
with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( clean_string )
