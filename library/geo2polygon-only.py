import sys
import re
import json
from geojson import FeatureCollection, Feature, Polygon


# remove newlines and blanks in the coordinates array, for better readibility of the GeoJSON pretty print
def pretty_dumps(obj, **kwargs):
    def compact_coordinates(match):
        # Remove newlines and extra spaces within the coordinates array
        return match.group(0).replace('\n', '').replace(' ', '')
    json_str = json.dumps(obj, **kwargs)
    # Use a more robust regex to match coordinate arrays
    json_str = re.sub(r'\[\s*([^\[\]]+?)\s*\]', compact_coordinates, json_str)
    return json_str

# GeoJSON extract Polygons
with open( sys.argv[1]+'.geojson', 'r') as infile:
   data = json.load ( infile )

basket = []  

for feature in data['features']:
    if feature['geometry'].get('type') == 'Polygon':
        basket.append(Feature(geometry=feature['geometry'], properties=feature['properties']))

    if feature['geometry'].get('type') == 'MultiPolygon':
        polygon_list = feature['geometry']['coordinates']
        for item in polygon_list:
            basket.append(Feature(geometry=Polygon(item), properties=feature['properties']))

    if feature['geometry'].get('type') == 'GeometryCollection':
        for geometry in feature["geometry"]["geometries"]:
            if geometry["type"] == "Polygon":
                coordinates = geometry["coordinates"]  
                basket.append(Feature(geometry=Polygon(coordinates), properties=feature['properties']))  


geojson_string = pretty_dumps(FeatureCollection(basket), indent=2, ensure_ascii=False)

improved_geojson_string = re.sub(r'name', 'name', geojson_string, flags=re.IGNORECASE)

#print(improved_geojson_string)
with open( sys.argv[1]+'-polygon.geojson', 'w') as outfile:
    outfile.write( improved_geojson_string )
print ( f"File saved as {sys.argv[1]+'-polygon.geojson'}")