import sys
import re
import json
from geojson import FeatureCollection, Feature

# GeoJSON into one line

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )
infile.close()   

basket = []       
for feature in data['features']:
    basket.append(Feature(geometry=feature['geometry'], properties=feature['properties']))

geojson_string = json.dumps(FeatureCollection(basket), ensure_ascii=False)
# clean up some programs that use different spellings for name
output_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

print(output_string)
with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( output_string )
    
