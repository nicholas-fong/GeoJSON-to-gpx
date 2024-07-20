import sys
import re
import json
from geojson import FeatureCollection, Feature, LineString, MultiLineString, GeometryCollection

# remove newlines and blanks in the coordinates array, for better readibility of the GeoJSON pretty print
def pretty_dumps(obj, **kwargs):
    def compact_coordinates(match):
        # Remove newlines and extra spaces within the coordinates array
        return match.group(0).replace('\n', '').replace(' ', '')
    json_str = json.dumps(obj, **kwargs)
    # Use a more robust regex to match coordinate arrays
    json_str = re.sub(r'\[\s*([^\[\]]+?)\s*\]', compact_coordinates, json_str)
    return json_str

# GeoJSON only extracts LineString features
with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )

basket = []  

def reverse(coordinates):
    return (list(reversed(coordinates)))

for feature in data['features']:
    if feature['geometry'].get('type') == 'LineString':
        coords = feature['geometry']['coordinates']
        new_linestring = LineString(reverse(coords))
        basket.append(Feature(geometry=new_linestring, properties=feature['properties']))

    if feature['geometry'].get('type') == 'MultiLineString':
        multiline_bucket = []
        for coords in feature['geometry']['coordinates']:
            multiline_bucket.append ( reverse(coords))
        basket.append(Feature(geometry=MultiLineString(multiline_bucket), properties=feature['properties']))

    if feature['geometry'].get('type') == 'GeometryCollection':
        new_collection = []
        for geometry in feature["geometry"]["geometries"]:
            if geometry["type"] == "LineString":
                coordinates = geometry["coordinates"]
                new_collection.append(LineString(reverse(coordinates)))
        basket.append(Feature(geometry=GeometryCollection(new_collection), properties=feature['properties']))  

geojson_string = pretty_dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)
improved_geojson_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

with open( sys.argv[1]+'-reverse.geojson', 'w') as outfile:
    outfile.write( improved_geojson_string )
print ( f"File saved as {sys.argv[1]+'-reverse.geojson'}")