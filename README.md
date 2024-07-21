## GeoJSON-to-gpx
A collection of GeoJSON to GPX converters (bidirectional).
Also includes geo2geo.py which reformats geojson to JSON style (pretty-print or beautify) and makes it human readable. To reverse the process, geo2geo-compact.py reformats GeoJSON to a compact, machine readable, one line.

- `Overpass-turbo` [queries](https://overpass-turbo.eu/)

- `Java OpenStreetMap editor` [JOSM](https://josm.openstreetmap.de)

- `BRouter` [Route Planner](https://brouter.de/brouter-web)
 
- `Municipality` Open Data


### Examples
```
$python3 geo2gpx.py myhouse   (myhouse is a GeoJSON file with file extension .geojson)
$python3 geo2wpt.py myhouse > myhouse.gpx (save Points to a gpx file)
$python3 geo2trk.py mytrail   (extract LineString elements in GeoJSON and save them to a gpx track)
$python3 geo2rte.py mytrail   (extract LineString elements in GeoJSON and save them to a gpx route)
$python3 gpx2geo.py mygpx     (waypoint becomes Point; route and track are saved as LineString)
$python3 geo2geo.py myhouse (pretty print)
$python3 geo2geo-compact.py myhouse (compact GeoJSON to one line)
```
#### Notes

- To add elevation to GPX or GeoJSON or KML, use codes from [SRTM-GeoTIFF](https://github.com/nicholas-fong/SRTM-GeoTIFF)

### Usage
Download a city's Open Data database of drinking fountains (e.g. fountains.geojson in library)
```
$python3 geo2gpx.py fountains
```
