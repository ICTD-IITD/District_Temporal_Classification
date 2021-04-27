import json
import pandas as pd 
import sys
import pathlib

jsonFileName="/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Visualisation/2011_Dist.geojson"
path_predictor = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Predictions_2019.csv"

a_file = open("2011_Dist.geojson", "r")
countryData = json.load(a_file)
a_file.close()

#countryData = json.loads(open(jsonFileName,).write())

df = pd.read_csv(path_predictor)

for currDistrictFeature in countryData["features"]:
	dic = {}
	censuscode=currDistrictFeature["properties"]['censuscode']
	print(df.loc[df['census_code'] == censuscode, 'ASSET'],'\n')
	if len(df.loc[df['census_code'] == censuscode, 'ASSET']) != 0 :
		dic["ASSET"] = str(df.loc[df['census_code'] == censuscode, 'ASSET'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'BF']) != 0 :
		dic["BF"] = str(df.loc[df['census_code'] == censuscode, 'BF'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'CHH']) != 0 :
		dic["CHH"] = str(df.loc[df['census_code'] == censuscode, 'CHH'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'FC']) != 0 :
		dic["FC"] = str(df.loc[df['census_code'] == censuscode, 'FC'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'MSW']) != 0 :
		dic["MSW"] = str(df.loc[df['census_code'] == censuscode, 'MSW'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'MSL']) != 0 :
		dic["MSL"] = str(df.loc[df['census_code'] == censuscode, 'MSL'].iloc[0])
	if len(df.loc[df['census_code'] == censuscode, 'AQI']) != 0 :
		y = df.loc[df['census_code'] == censuscode, 'AQI'].iloc[0]
	else :
		y = 0
	if (y>=15) :
		dic["fill"] = "#00ff00"
	elif(y<=10):
		dic["fill"] = "#f40606"
	else :
		dic["fill"] = "#f8d112"
	currDistrictFeature["properties"].update(dic)

a_file = open("2011_Dist.geojson", "w")
json.dump(countryData, a_file)
a_file.close()