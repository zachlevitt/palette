import subprocess
import requests
import pyperclip
from google.cloud import storage

year = "2021"
month = "07"
day = "21"
date = year + month + day

subprocess.check_call(['mkdir', date])

filenames = []
dates = []

download_string = ""

for i in range(0,23):

	if (i < 10):
		timeString = "0" + str(i)
	else:
		timeString = str(i)

	indiv_download_string = '\"gs://high-resolution-rapid-refresh/hrrr.' + date + '/conus/hrrr.t' + timeString + 'z.wrfsfcf00.grib2\" \\\n'
	download_string = download_string + indiv_download_string

download_string = "mkdir " + date + "/" + "grib2" + "&& cd " + date + "/" + "grib2" + "&& gsutil -m cp \\\n" + download_string + "."
pyperclip.copy(download_string)


#######################################################################

#print("generating date strings")

# for i in range(1,31):
# 	if (i < 10):
# 		dates.append(date + "0" + str(i))
# 	else:
# 		dates.append(date + str(i))
