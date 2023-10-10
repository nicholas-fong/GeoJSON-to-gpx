import sys
import re
import geojson
from geojson import FeatureCollection, Feature, dumps

# GeoJSON into one line

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = geojson.load ( infile )
infile.close()   

basket = []       
for i in range(len(data['features'])):
    #type = data['features'][i]['geometry']['type']
    my_geometry = data['features'][i]['geometry']
    my_properties = data['features'][i]['properties']
    basket.append(Feature(geometry=my_geometry, properties=my_properties))

geojson_string = dumps(FeatureCollection(basket), ensure_ascii=False)
# clean up some programs that use different spellings for name
output_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

#print(output_string)
with open( sys.argv[1]+'.geojson', 'w') as outfile:
    outfile.write( output_string )
