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
$python geo2trk.py mytrail   (only extract LineString elements in GeoJSON and transform them to a gpx track)
$python geo2rte.py mytrail   (only extract LineString elements in GeoJSON and transform them to a gpx route)
$python geo2wpt.py mytrail   (only extract Point and Polygon elements and transform them to gpx waypoint; Polygon's centroid is used as waypoint)
$python gpx2geo.py mygpx     (waypoint is transformed to Point; route and track are transformed to LineString)
```
#### Notes
- Transforming GeoJSON Polygon to a single gpx waypoint is not an ideal strategy, but is good enough for casual hobby use.
- There is no strictly defined placeholder for elevation in RFC 7946: it says "Altitude or elevation MAY be included as an optional third
   element". Design decision: elevation, if exists, is added as ['geometry']['coordinates'][2] 
- Note that gdal-ogr2ogr adds elevation to ['properties']['ele']. 
- To add elevation to gpx, use codes from [gpx-add-SRTM-elevation](https://github.com/nicholas-fong/gpx-add-SRTM-elevation)

### A simple use case
Download a city's Open Data database of drinking fountains (e.g. fountains.geojson)
```
$python geo2gpx.py fountains > fountains.gpx
```
## GeoJSON to KML conversion
First, install gdal-bin
```
org2org -f 'KML' -a_srs EPSG:4326 fountains.kml fountains.geojson
```
## GPX to KML conversion
First, install gdal-bin
```
org2org -f 'KML' -a_srs EPSG:4326 -mapFieldType DateTime=String fountains.kml fountains.gpx
```
This way of creating KML (from GPX) will add placemarks (pins) on the track.
