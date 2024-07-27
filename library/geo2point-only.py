import sys
import re
import json
from geojson import FeatureCollection, Feature, Point

# GeoJSON extract Point

# remove newlines and blanks in the coordinates array, for better readibility of the GeoJSON pretty print
def pretty_dumps(obj, **kwargs):
    def compact_coordinates(match):
        # Remove newlines and extra spaces within the coordinates array
        return match.group(0).replace('\n', '').replace(' ', '')
    json_str = json.dumps(obj, **kwargs)
    # Use a more robust regex to match coordinate arrays
    json_str = re.sub(r'\[\s*([^\[\]]+?)\s*\]', compact_coordinates, json_str)
    return json_str

with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )

basket = []  

for feature in data['features']:
    if feature['geometry'].get('type') == 'Point':
        coords = feature['geometry']['coordinates']
        basket.append(Feature(geometry=Point(coords), properties=feature['properties']))

    if feature['geometry'].get('type') == 'MultiPoint':
        multiline_bucket = []
        for coords in feature['geometry']['coordinates']:
            basket.append(Feature(geometry=Point(coords), properties=feature['properties']))

    if feature['geometry'].get('type') == 'GeometryCollection':
        for geometry in feature["geometry"]["geometries"]:
            if geometry["type"] == "Point":
                coords = geometry["coordinates"]
                basket.append(Feature(geometry=Point(coords), properties=feature['properties']))  


geojson_string = pretty_dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)
improved_geojson_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

#print(improved_geojson_string)
with open( sys.argv[1]+'-point.geojson', 'w') as outfile:
    outfile.write( improved_geojson_string )
print ( f"File saved as {sys.argv[1]+'-point.geojson'}")