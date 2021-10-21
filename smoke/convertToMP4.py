import subprocess

year = "2021"
month = "07"
day = "01"
date = year + month + day
#month = '202107'

subprocess.check_call(['mkdir', date + "/tif"])
subprocess.check_call(['mkdir', date + "/color"])
subprocess.check_call(['mkdir', date + "/projected"])
subprocess.check_call(['mkdir', date + "/jpeg"])
subprocess.check_call(['mkdir', date + "/combined"])

filenames = []
dates = []

download_string = ""

argsStates = ['gdal_rasterize','-burn','40','-burn','40','-burn','40','-a_nodata','255','-ot','Byte','-te','-2814555.3746216343715787','-1497340.4026472282130271','2586948.8959804810583591','1723358.5133773556444794','-ts','1818','1084','-l','us-states-albers-lines','us/us-states-albers-lines.shp',date + '/us-states.tif']
subprocess.call(argsStates)

argsStatesJPEG = ['gdal_translate','-of','JPEG','-scale','-co','worldfile=yes',date + '/us-states.tif',date + '/us-states.jpeg']
subprocess.call(argsStatesJPEG)

for i in range(0,1):

	if (i < 10):
		timeString = "0" + str(i)
	else:
		timeString = str(i)

	#indiv_download_string = '\"gs://high-resolution-rapid-refresh/hrrr.' + date + '/conus/hrrr.t' + timeString + 'z.wrfsfcf00.grib2\" \\\n'
	#download_string = download_string + indiv_download_string
	grib2_file = date + "/grib2/hrrr.t" + timeString + "z.wrfsfcf00.grib2"
	tif_file = date + "/tif/hrrr_nss8m_" + date + "_" + timeString + ".tif"
	color_file = date + "/color/hrrr_nss8m_" + date + "_" + timeString + "_color.tif"
	color_projected = date + "/projected/hrrr_nss8m_" + date + "_" + timeString + "_color_projected.tif"
	color_jpeg = date + "/jpeg/hrrr_nss8m_" + date + "_" + timeString + "_color_projected.jpeg"
	combined_jpeg = date + "/combined/hrrr_nss8m_" + date + "_" + timeString + "_combined.jpeg"

	args = ['gdal_translate', '-b', '76', grib2_file , tif_file]
	subprocess.call(args)

	print("wrote tif file for " + timeString + " on " + date)


	argsColor = ['gdaldem','color-relief',tif_file, 'smokeColorWapo.txt',color_file]
	subprocess.call(argsColor)

	print("gdal subprocess colorize done for " + timeString + " on " + date)

	#crs = '\"+proj=aea +lat_1=29.5 +lat_2=45.5 +lat_0=37.5 +lon_0=-96 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m no_defs\"'
	#print(crs)
	argsProject = ['gdalwarp','-t_srs','ESRI:102003','-r','bilinear','-of','GTiff',color_file,color_projected]
	subprocess.call(argsProject)

	argsJPEG = ['gdal_translate','-of','JPEG','-scale','-co','worldfile=yes',color_projected,color_jpeg]
	subprocess.call(argsJPEG)
	print("gdal subprocess jpeg output done for " + timeString + " on " + date)

	argsCombine = ['convert',color_jpeg,date + '/us-states.jpeg','-gravity','center','-compose','multiply','-composite','-format','jpg','-quality','100',combined_jpeg]
	subprocess.call(argsCombine)
	print("imagemagick combine done for " + timeString + " on " + date)

	argsFFMPEG = ['ffmpeg','-r','20','-f','image2','-s','1060x880','-pattern_type','-glob','-i',date + "combined/*.jpeg",'-vcodec','libx264','-crf','25','-pix_fmt','yuv420p',date + ".mp4"]
	subprocess.call(argsFFMPEG)
	print("ffmpeg done for " + timeString + " on " + date)



