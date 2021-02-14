## geoJSON-gpx-converters
geoJSON to gpx (and vice versa) converters.

Queries from https://overpass-turbo.eu/  and JOSM can be exported to geoJSON.

Queries from municipal Open Data can be exported as geoJSON (most of the times).

This library is a collection of converters between geoJSON and gpx formats.

The output of these converters is always to STDOUT to allow felxibility of using shell pipes.

The main advantage of geoJSON is that it can be edited by Java OpenStreetMap Editor.

## Examples
```
$python geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python geo2gpx.py myhouse > myhouse.gpx (save to a gpx file: Point, Polygon centroid -> gpx waypoint; LineString -> gpx track)
$python geo2trk.py mytrail   (only extract LineString elements in GeoJSON and map them to a gpx track)
$python geo2wpt.py mytrail   (only extract Point and Polygon and map to gpx waypoint, Polygon centroid is used for waypoint)
$python gpx2geo.py mygpx     (waypoint is mapped to Point; route and track are mapped to LineString)
```
### An ultra simple use case
Download my city's Open Data database of drinking fountains as a GeoJSON file.
```
$python geo2gpx.py fountains > my-city-fountains.gpx
import my-city-fountains.gpx to a mobile phone or portable navigation device .
```
