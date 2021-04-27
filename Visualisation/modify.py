# remove the phrase "var india_districts = " before executing this scripts ad then add it back in the output

import json
import pandas as pd

a_file = open("main.geojson", "r")
countryData = json.load(a_file)
a_file.close()

msw_2019 = {}
msl_2019 = {}
bf_2019 = {}
chh_2019 = {}
fc_2019 = {}
assets_2019 = {}
adi_2019 = {}

#print(countryData["features"][2]["properties"])
df = pd.read_csv("../Predictions_2019.csv")


for rows in df.iterrows():
	censuscode = rows[1]["census_code"]
	assets_2019[censuscode] = rows[1]["ASSET"]
	msw_2019[censuscode] = rows[1]["MSW"]
	msl_2019[censuscode] = rows[1]["MSL"]
	bf_2019[censuscode] = rows[1]["BF"]
	chh_2019[censuscode] = rows[1]["CHH"]
	fc_2019[censuscode] = rows[1]["FC"]
	adi_2019[censuscode] = rows[1]["AQI"]

for i in range(len(countryData["features"])):
	print(countryData["features"][i]["properties"]["DISTRICT"])
	census = countryData["features"][i]["properties"]["censuscode"]
	if census not in adi_2019:
		print(census)
		countryData["features"][i]["properties"]["Available"] = '0'
		continue
	countryData["features"][i]["properties"]["Available"] = '1'
	countryData["features"][i]["properties"]["msl_2019"] = str(msl_2019[census])
	countryData["features"][i]["properties"]["msw_2019"] = str(msw_2019[census])
	countryData["features"][i]["properties"]["bf_2019"] = str(bf_2019[census])
	countryData["features"][i]["properties"]["chh_2019"] = str(chh_2019[census])
	countryData["features"][i]["properties"]["fc_2019"] = str(fc_2019[census])
	countryData["features"][i]["properties"]["asset_2019"] = str(assets_2019[census])
	countryData["features"][i]["properties"]["adi_2019"] = str(adi_2019[census])

	countryData["features"][i]["properties"]["adi_2001"] = str(int(countryData["features"][i]["properties"]["msw_2001"])+int(countryData["features"][i]["properties"]["msl_2001"])+int(countryData["features"][i]["properties"]["fc_2001"])+int(countryData["features"][i]["properties"]["bf_2001"])+int(countryData["features"][i]["properties"]["chh_2001"])+int(countryData["features"][i]["properties"]["asset_2001"]))
	countryData["features"][i]["properties"]["adi_2011"] = str(int(countryData["features"][i]["properties"]["msw_2011"])+int(countryData["features"][i]["properties"]["msl_2011"])+int(countryData["features"][i]["properties"]["fc_2011"])+int(countryData["features"][i]["properties"]["bf_2011"])+int(countryData["features"][i]["properties"]["chh_2011"])+int(countryData["features"][i]["properties"]["asset_2011"]))

a_file = open("main_aman.geojson", "w")
json.dump(countryData, a_file)
a_file.close()