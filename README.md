## GeoJSON-to-gpx
A collection of GeoJSON to GPX converters (bidirectional).
Also includes geo2geo.py which reformats geojson to JSON style (pretty-print or beautify) and makes it human readable. To reverse the process, geo2geo-compact.py reformats GeoJSON to a compact, machine readable one line.

- `Overpass-turbo` [queries](https://overpass-turbo.eu/)

- `Java OpenStreetMap editor` [JOSM](https://josm.openstreetmap.de)

- `BRouter` [Route Planner](https://brouter.de/brouter-web)
 
- `Municipality` Open Data


### Examples
```
$python3 geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python3 geo2gpx.py myhouse > myhouse.gpx (save to a gpx file: Point, Polygon centroid -> gpx waypoint; LineString -> gpx track)
$python3 geo2trk.py mytrail   (only extract LineString elements in GeoJSON and transform them to a gpx track)
$python3 geo2rte.py mytrail   (only extract LineString elements in GeoJSON and transform them to a gpx route)
$python3 geo2wpt.py mytrail   (only extract Point and Polygon elements and transform them to gpx waypoint; Polygon's centroid is used as waypoint)
$python3 gpx2geo.py mygpx     (waypoint is transformed to Point; route and track are transformed to LineString)
$python3 geo2geo.py myhouse
$python3 geo2geo-lean.py myhouse

```
#### Notes
- Transforming GeoJSON Polygon to a single gpx waypoint is not an ideal strategy, but is good enough for casual hobby use.
- There is no strictly defined placeholder for elevation in RFC 7946: it says "Altitude or elevation MAY be included as an optional third element". This xyz approach has been widely adopted. The elevation is the ['geometry']['coordinates'][2] 
- To add elevation to gpx or GeoJSON, use codes from [SRTM-GeoTIFF](https://github.com/nicholas-fong/SRTM-GeoTIFF)

### Usage
Download a city's Open Data database of drinking fountains (e.g. fountains.geojson)
```
$python3 geo2gpx.py fountains > fountains.gpx
$python3 geo2geo.py myhouse
```
