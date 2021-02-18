## geoJSON-gpx-convert
A collection of geoJSON to gpx converters (bidirectional).

- `Overpass-turbo` [queries](https://overpass-turbo.eu/)

- `Java OpenStreetMap editor` [JOSM](https://josm.openstreetmap.de)

- `BRouter` [Route Planner](https://brouter.de/brouter-web)
 
- `Municipality` Open Data

This repository is a collection of converters between geoJSON and gpx.

The output of these converters is directed to stdout to allow felxibility of using os pipes.

### Examples
```
$python geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python geo2gpx.py myhouse > myhouse.gpx (save to a gpx file: Point, Polygon centroid -> gpx waypoint; LineString -> gpx track)
$python geo2trk.py mytrail   (only extract LineString elements in GeoJSON and map them to a gpx track)
$python geo2wpt.py mytrail   (only extract Point and Polygon elements and map them to gpx waypoint; Polygon's centroid is used as waypoint)
$python gpx2geo.py mygpx     (waypoint is mapped to Point; route and track are mapped to LineString)
```
#### Notes
- transforming GeoJSON Polygon to a single gpx waypoint is not an ideal strategy, but is good enough for casual use.
- there is no strictly defined placeholder for elevation in RFC 7946: "elevation MAY be included as an option". For example, BRouter adds elevation to ['geometry']['coordinates'][2], but gdal-ogr2ogr adds elevation to ['properties']['ele']. My design choice is to discard elevations for now to avoid inconsistencies and conflicts. It may be added in a later date.
- to add elevation to gpx, use [gpx-add-SRTM-elevation](https://github.com/nicholas-fong/gpx-add-SRTM-elevation)

### An ultra simple use case
Download a city's Open Data database of drinking fountains as a GeoJSON file.
```
$python geo2gpx.py fountains > my-city-fountains.gpx
transfer my-city-fountains.gpx to a mobile phone or portable navigation device .
```
