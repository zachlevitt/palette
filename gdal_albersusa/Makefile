
#project each file to the correct albersusa projection
#merge

reproject:
#gdalinfo gis/mapping_assets/elevation_90m_usa.tif
# gdalinfo gis/mapping_assets/albersusa_elements/AKGMTED2010_base_zero.tif
# gdalinfo gis/mapping_assets/albersusa_elements/hi_alos_2000m_dem_base_zero.tif
	
#mapshaper gis/mapping_assets/conus/conus.shp -dissolve2 -o gis/mapping_assets/conus/conus_dissolved.shp

#rasterize an albersusa output
#export conus dem at extent of albersusa with ak/hi
gdal_rasterize -burn 255 -tr 2000 2000 gis/usa_adm1_polygon/usa_adm1_polygon.shp gis/usa_adm1_polygon_raster.tif
gdalwarp -overwrite -te -2386386.179 -1349086.333 2255613.821 1566913.667 gis/hillshade/conus_cut.tif gis/hillshade/conus_cut_albersusa_bb.tif
mapshaper gis/usa_adm1_polygon/usa_adm1_polygon.shp -rectangle -o gis/usa_adm1_polygon_bb.shp

#output bounds for hawaii and alaska
	mapshaper -rectangle bbox=-172.26,50.89,-127.00,73.21 -o gis/ak_bounds.shp
	mapshaper -rectangle bbox=-160.50,18.72,-154.57,22.58 -o gis/hi_bounds.shp

#reproject base data to albersa projections
	gdalwarp -t_srs '+proj=aea +lat_1=55 +lat_2=70 +lat_0=65 +lon_0=-148 +x_0=0 +y_0=0' -overwrite -tr 5405 5405 -r cubic -co compress=lzw gis/mapping_assets/albersusa_elements/AKGMTED2010_base_zero.tif gis/hillshade/ak_projected.tif
	gdalwarp -t_srs '+proj=aea +lat_1=19 +lat_2=24 +lat_0=20.9 +lon_0=-156.5 +x_0=0 +y_0=0' -overwrite -tr 2000 2000 -r cubic -co compress=lzw gis/mapping_assets/albersusa_elements/hi_alos_2000m_dem_base_zero.tif gis/hillshade/hi_projected.tif
	gdalwarp -t_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84' -overwrite -tr 2000 2000 -r cubic -co compress=lzw gis/mapping_assets/elevation_90m_usa.tif gis/hillshade/conus_projected.tif

	gdal_calc.py -A gis/hillshade/conus_projected.tif --outfile=gis/hillshade/conus_projected_zeros.tif --calc="0*(A<=0) + A*(A>0)" --overwrite 

#hillshade the data! add more styling here tk
	gdaldem hillshade gis/hillshade/ak_projected.tif gis/hillshade/ak_hillshade.tif -igor -z 10
	gdaldem hillshade gis/hillshade/hi_projected.tif gis/hillshade/hi_hillshade.tif -igor -z 10
	gdaldem hillshade gis/hillshade/conus_projected_zeros.tif gis/hillshade/conus_hillshade.tif -igor -z 10

#clip ak and hawaii to bounds in mapshaper
gdalwarp -overwrite -cutline gis/ak_bounds.shp -crop_to_cutline gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_bounds.tif 
gdalwarp -overwrite -cutline gis/hi_bounds.shp -crop_to_cutline gis/hillshade/hi_cut.tif gis/hillshade/hi_cut_bounds.tif 


#old clip
# gdalwarp -overwrite -cutline gis/mapping_assets/albersusa_elements/hi_projected/hi_projected.shp -crop_to_cutline gis/hillshade/hi_hillshade.tif gis/hillshade/hi_cut.tif
# gdalwarp -overwrite -cutline gis/mapping_assets/albersusa_elements/ak_projected/ak_projected.shp -crop_to_cutline gis/hillshade/ak_hillshade.tif gis/hillshade/ak_cut.tif
# gdalwarp -overwrite -cutline gis/mapping_assets/conus/conus_dissolved.shp -crop_to_cutline gis/hillshade/conus_hillshade.tif gis/hillshade/conus_cut.tif

#export as png
gdal_translate gis/hillshade/ak_cut_bounds.tif gis/hillshade/ak_cut_bounds.png 
gdal_translate gis/hillshade/hi_cut_bounds.tif gis/hillshade/hi_cut_bounds.png

#ak width in meters: 3140305
#ak height in meters: -2394415

gdalinfo gis/hillshade/ak_cut_bounds.tif #581, 443 ratio
# Corner Coordinates:
# Upper Left  (-1678118.449, 1059318.827) (166d20'32.15"E, 68d58'28.96"N)
# Lower Left  (-1678118.449,-1335096.173) (171d49'11.29"W, 50d15'48.24"N)
# Upper Right ( 1462186.551, 1059318.827) (106d42' 3.74"W, 70d10'18.95"N)
# Lower Right ( 1462186.551,-1335096.173) (127d 1'27.39"W, 50d55'26.73"N)
# Center      ( -107965.949, -137888.673) (150d12'24.28"W, 63d45'26.12"N)

#hi width in meters: 624000
#hi height in meters: 430000

gdalinfo gis/hillshade/hi_cut_bounds.tif #312, 215
# Corner Coordinates:
# Upper Left  ( -420413.559,  191423.847) (160d35'30.22"W, 22d34'39.48"N)
# Lower Left  ( -420413.559, -238576.153) (160d29' 6.60"W, 18d41'50.97"N)
# Upper Right (  203586.441,  191423.847) (154d31' 5.60"W, 22d36'56.16"N)
# Lower Right (  203586.441, -238576.153) (154d34'11.47"W, 18d44' 4.29"N)
# Center      ( -108413.559,  -23576.153) (157d32'29.20"W, 20d41' 2.34"N)


#georference it back to albers eq in right position
#ALMOST PERFECT, A LITTLE TOO LOW AND RIGHT
#TO DO: CLIP ALASKA AND HAWAII SO THAT THE WINDOW IS JUST WHAT ALBERSUSA WANTS (clips to a window like mapshaper albersusa)
# the center in mapshaper would be the center of the a_ullr here if I clipped the rasters to the exact bounding box that mapshaper uses 
gdal_translate gis/hillshade/ak_cut_bounds.png gis/hillshade/ak_cut_georef.tif -a_ullr -2430807.251 -494927.91000000003 -1268894.4009999998 -1380861.46 -a_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84'
gdal_translate gis/hillshade/hi_cut_bounds.png gis/hillshade/hi_cut_georef.tif -a_ullr -1418381.377 -875027.3160000001 -794381.3770000001 -1305027.316 -a_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84'

#THIS WORKS
gdal_merge.py -o gis/hillshade/merged_georef_all.tif gis/hillshade/ak_cut_georef.tif gis/hillshade/hi_cut_georef.tif gis/hillshade/conus_cut.tif

gdalwarp -overwrite -cutline gis/usa_adm1_polygon/usa_adm1_polygon.shp -crop_to_cutline gis/hillshade/merged_georef_all.tif gis/hillshade/merged_georef_all_cut.tif 
#this is 95% of the way there, it's somehow slightly off from the 
gdal_translate -a_nodata 0 gis/hillshade/merged_georef_all_cut.tif gis/hillshade/merged_georef_all_cut.png 

################################
#TESTING BELOW THIS

3632160 (difference between actual file x1 and x2)
times 0.37
1343899.2 
	gdalwarp -overwrite -te -2505083.449 -1135111.173 1127076.551 729613.827 -te_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84' gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_moved.tif
	gdalwarp -overwrite -te -172.26 50.89 -127.00 73.21 -te_srs 'wgs84' gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_moved.tif

	
	gdaldem color-relief -b 1 -alpha -q gis/hillshade/conus_cut.tif gis/colors.txt gis/hillshade/conus_colors.tif
	gdaldem color-relief -b 1 -alpha -q gis/hillshade/ak_cut.tif gis/colors.txt gis/hillshade/ak_colors.tif
	gdaldem color-relief -b 1 -alpha -q gis/hillshade/hi_cut.tif gis/colors.txt gis/hillshade/hi_colors.tif

	convert gis/hillshade/conus_cut.tif gis/hillshade/conus_colors.tif -gravity center -colorspace sRGB -compose multiply -composite -format tif -quality 100 gis/hillshade/conus_combined.tif
# gdalinfo gis/hillshade/hi_projected.tif
# gdalinfo gis/hillshade/ak_projected.tif
# gdalinfo gis/hillshade/conus_projected.tif


# gdal_merge.py -o gis/hillshade/merged.tif gis/hillshade/conus_cut.tif gis/hillshade/ak_cut.tif gis/hillshade/hi_cut.tif
#bounds  -2385312.266302042,-1337212.7020434465,2258200.1768970774,1565781.66

#output bounds of conus aea
# gdalwarp -overwrite -te -2385312.266302042 -1337212.7020434465 2258200.1768970774 1565781.66 gis/hillshade/conus_cut.tif gis/hillshade/conus_bb.tif
# gdalwarp -overwrite -te -2385312.266302042 -1337212.7020434465 2258200.1768970774 1565781.66 gis/hillshade/hi_cut.tif gis/hillshade/hi_bb.tif
gdalwarp -overwrite -te -2505083.449 -1135111.173 10000000 5000000 gis/hillshade/ak_cut.tif gis/hillshade/ak_bb.tif
gdalwarp -overwrite -te -2354235.429 -1336319.575 2257764.571 1565680.425 gis/hillshade/ak_cut.tif gis/hillshade/ak_bb.tif

#try reprojecting the ak cut into the bounding box in conus aea projection using geo transformed coordinates..
gdalwarp -overwrite -te_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84' -te -5623734.81578938 4013678.85796424 -1178704.63837992 3442339.02946053 gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_inconusprojection.tif

#then try to make a bb:
gdalwarp -overwrite -te -2385312.266302042 -1337212.7020434465 2258200.1768970774 1565781.66 gis/hillshade/ak_cut_inconusprojection.tif gis/hillshade/ak_cut_inconusprojection_bb.tif

gdal_merge.py -o gis/hillshade/merged_attempt.tif gis/hillshade/ak_cut_inconusprojection.tif gis/hillshade/conus_cut.tif 




#gdaltransform from ak to conus 
gdaltransform -s_srs '+proj=aea +lat_1=55 +lat_2=70 +lat_0=65 +lon_0=-148 +x_0=0 +y_0=0' -t_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84'
lower left: -2505083.449 -1135111.173 -> in conus: -5623734.81578938 4013678.85796424
upper right in conus: -1178704.63837992 3442339.02946053

#try gdal translate
gdal_translate -a_ullr -2505083.449 729613.827 1327076.551 -1335111.173 gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_shifttest.tif

# ak cut
# Upper Left  (-2505083.449,  729613.827) (158d18'58.77"E, 61d45' 6.24"N)
# Lower Left  (-2505083.449,-1135111.173) (176d50'57.18"E, 48d36' 7.97"N)
# Upper Right ( 1127076.551,  729613.827) (118d31'24.84"W, 69d11'28.69"N)
# Lower Right ( 1127076.551,-1135111.173) (130d51'18.10"W, 53d31'46.25"N)
# Center      ( -689003.449, -202748.673) (161d36'20.67"W, 62d33'15.42"N)

gdaltransform -s_srs 'wgs84' -t_srs '+proj=aea +lat_1=55 +lat_2=70 +lat_0=65 +lon_0=-148 +x_0=0 +y_0=0'

origin of AK in aea: -200840.054766732 -218686.141837532
placement: [-1882782,-969242]

dx: -1681941.945233268
dy: -750555.858162468

gdal_translate -a_ullr -2505083.449 + (-1681941.945233268) 729613.827 + (-750555.858162468) 1327076.551 + (-1681941.945233268) -1335111.173 +  (-750555.858162468) gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_shifttest.tif
gdal_translate -a_ullr -4187025.394233268 -20942.031162468 -354865.394233268 -2085667.031162468 gis/hillshade/ak_cut.tif gis/hillshade/ak_cut_shifttest.tif

#THIS WORKS
#export conus dem at extent of albersusa with ak/hi
gdalwarp -overwrite -te -2386386.179 -1349086.333 2255613.821 1566913.667 gis/hillshade/conus_cut.tif gis/hillshade/conus_cut_albersusa_bb.tif

#export ak as png
gdal_translate gis/hillshade/ak_cut.tif gis/hillshade/ak_cut.png 
#XPORT HI AND PNG
gdal_translate gis/hillshade/hi_cut.tif gis/hillshade/hi_cut.png

#georference it back to albers eq in right position
#ALMOST PERFECT, A LITTLE TOO LOW AND RIGHT
#TO DO: CLIP ALASKA AND HAWAII SO THAT THE WINDOW IS JUST WHAT ALBERSUSA WANTS (clips to a window like mapshaper albersusa)
# the center in mapshaper would be the center of the a_ullr here if I clipped the rasters to the exact bounding box that mapshaper uses 
gdal_translate gis/hillshade/ak_cut.png gis/hillshade/ak_cut_georef.tif -a_ullr -2732729.504 -620969.712 -1388830.304 -1310917.962 -a_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84'

gdal_translate gis/hillshade/hi_cut.png gis/hillshade/hi_cut_georef.tif -a_ullr -2732729.504 -620969.712 -1388830.304 -1310917.962 -a_srs '+proj=aea +lon_0=-96 +lat_0=37.5 +lat_1=29.5 +lat_2=45.5 +ellps=WGS84'

#THIS WORKS
gdal_merge.py -o gis/hillshade/merged_attempt2.tif gis/hillshade/ak_cut_georef.tif gis/hillshade/conus_cut.tif 

#CLIP TO THE EXTENT OF THE ALBERSUSA RASTER
#https://github.com/mbloch/mapshaper/blob/f85a02d30eefc331e4375dd0d6d75188056dc9f7/src/crs/mapshaper-custom-projections.mjs#LL40C5-L40C35
#and 
ak cut has 672/345 ratio
dx = 3632160*0.37 = 1343899.2
dy = -1864725*0.37 = -689948.25

pick an x1 and y1, and then add dx and dy based on the ratio
-3386386.179 + 1343899.2 = -2042486.979
+ 653656.675 (ADJUSTMENT BASED ON QGIS)
-400000 + -689948.25 = -1089948.25
-400000-220969.712 (ADJUSTMENT BASED ON QGIS) =

