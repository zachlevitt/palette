# palette

Scripts, color schemes, templates and more for making maps.

Inspired by Dylan Moriarty's [cookbook](https://github.com/DylanMoriarty/cookbook)

## Helpful links

### Climate variables (temp, precip)
  - [Climate Engine](https://app.climateengine.com/climateEngine)
    - Easy access to GEE datasets, weather data, etc

### Fires
  - [NASA FIRMS: Archive download for points](https://firms.modaps.eosdis.nasa.gov/download/)<br>
  - [NASA FIRMS: Active fire data (also change over time)](https://firms.modaps.eosdis.nasa.gov/active_fire/)<br>
  - [NASA/USFS: active fire data](https://firms.modaps.eosdis.nasa.gov/usfs/active_fire/)<br>
  - [GeoMAC: historic fire perimeters thru April 2021](https://rmgsc.cr.usgs.gov/outgoing/GeoMAC/)<br>
  - [GeoMAC: Post April 2021](https://data-nifc.opendata.arcgis.com/)<br>


### Smoke
  - [Google Cloud, Archived NOAA HRRR Smoke data](https://console.cloud.google.com/marketplace/product/noaa-public/hrrr?project=python-232920&pli=1)
  - [S3 bucket, archive](https://noaa-hrrr-bdp-pds.s3.amazonaws.com/index.html)
  - [SILAM: Global concentration in air](http://silam.fmi.fi/thredds/ncss/grid/i4f20-an/IS4FIRES-disp_best.ncd/pointDataset.html)
    -   [Source](http://is4fires.fmi.fi/)
  - [Data for today and yesterday](https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/)
    - For example, /hrrr.t22z.wrfsfcf00.grib2 is for 6 p.m ET (22 UTC). For near surface smoke you are looking for the variable called MASSDEN or mass density (band 76)
  - Inventory of HRRR product: https://www.nco.ncep.noaa.gov/pmb/products/hrrr/hrrr.t00z.wrfsfcf00.grib2.shtml

### Satellite imagery
  - [MODIS regional-level 250m imagery](https://worldview.earthdata.nasa.gov/)
  - [LANDSAT 90m](https://landsat.usgs.gov/)
    - Or: [Sentinel Hub](https://apps.sentinel-hub.com/eo-browser/?zoom=10&lat=41.9&lng=12.5&themeId=DEFAULT-THEME#lat=41.90074384269173&lng=12.499008178710938&zoom=10)
  - [Sentinel 30m](https://apps.sentinel-hub.com/eo-browser/)


### Land cover
  - [WorldCover 10m ESA land cover](https://viewer.esa-worldcover.org/worldcover/?language=en&bbox=-139.3970663187302,15.960599472365558,-54.090944878048674,53.328727928912656&overlay=false&bgLayer=MapBox_Satellite&date=2021-10-20&layer=WORLDCOVER_2020_MAP)
  - USGS NLCD

### DEM
  - 30M: http://dwtkns.com/srtm30m/
  - 90M: http://dwtkns.com/srtm/
  - GEBCO
  - ETOPO_global_1km_relief_and_bathymetry: https://portal.opentopography.org/raster?opentopoID=OTSRTM.042013.4326.1
  - https://www.bodc.ac.uk/data/hosted_data_systems/gebco_gridded_bathymetry_data/

