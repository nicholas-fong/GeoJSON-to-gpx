## geoJSON-gpx-converters
A collection of geoJSON to gpx converters (and vice versa).

- Overpass Queries https://overpass-turbo.eu/ can be exported as geoJSON.

- Java OpenStreetMap editor [JOSM](https://josm.openstreetmap.de/) can exported as geoJSON.

- Municipality Open Data can be exported as geoJSON.

- BRouter Route Planner https://brouter.de/brouter-web can be exported as geoJSON.

This repository is a collection of bidirectional converters between geoJSON and gpx formats.

The output of these converters is directed to stdout to allow felxibility of pipes.

### Examples
```
$python geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python geo2gpx.py myhouse > myhouse.gpx (save to a gpx file: Point, Polygon centroid -> gpx waypoint; LineString -> gpx track)
$python geo2trk.py mytrail   (only extract LineString elements in GeoJSON and map them to a gpx track)
$python geo2wpt.py mytrail   (only extract Point and Polygon elements and map them to gpx waypoint; Polygon's centroid is used as waypoint)
$python gpx2geo.py mygpx     (waypoint is mapped to Point; route and track are mapped to LineString)
```
- transforming GeoJSON Polygon to a single gpx waypoint is not an ideal strategy, but is good enough for general tourism use.
- there is no explicitly defined placeholder for elevation in RFC 7946 geoJSON (elevation MAY be included as an optional geometry: coordinates[2]); my design decision is to discard elevations for now. It may be added in a later date.
- to add elevation back to gpx, use [gpx-add-SRTM-elevation](https://github.com/nicholas-fong/gpx-add-SRTM-elevation)

### An ultra simple use case
Download a city's Open Data database of drinking fountains as a GeoJSON file.
```
$python geo2gpx.py fountains > my-city-fountains.gpx
transfer my-city-fountains.gpx to a mobile phone or portable navigation device .
```
