## geoJSON-gpx-converters
geoJSON to gpx (and vice versa) converters.

Overpass Queries https://overpass-turbo.eu/ can be exported as geoJSON.

Java OpenStreetMap editor (JOSM) can exported as geoJSON.

Queries from municipal Open Data can be exported as geoJSON (most of the times).

This repository is a collection of converters between geoJSON and gpx formats.

The output of these converters is directed to stdout to allow felxibility of pipes and filters.

The advantage of geoJSON is that it can be easily edited by Java OpenStreetMap Editor (JOSM).

## Examples
```
$python geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python geo2gpx.py myhouse > myhouse.gpx (save to a gpx file: Point, Polygon centroid -> gpx waypoint; LineString -> gpx track)
$python geo2trk.py mytrail   (only extract LineString elements in GeoJSON and map them to a gpx track)
$python geo2wpt.py mytrail   (only extract Point and Polygon and map to gpx waypoint, Polygon centroid is used for waypoint)
$python gpx2geo.py mygpx     (waypoint is mapped to Point; route and track are mapped to LineString)
```
### An ultra simple use case
Download a city's Open Data database of drinking fountains as a GeoJSON file.
```
$python geo2gpx.py fountains > my-city-fountains.gpx
import my-city-fountains.gpx to a mobile phone or portable navigation device .
```
