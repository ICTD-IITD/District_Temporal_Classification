import json
import sys
import pathlib
import rasterio
from rasterio.mask import mask

tiffFileName="/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Creating_features/landsat7_india_500_2011-01-01_2011-12-31.tif"
jsonFileName="/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Creating_features/2011_Dist.geojson"
output_folder_path = 'districtTiffFiles500_2011/'

countryData = json.loads(open(jsonFileName).read())

for currDistrictFeature in countryData["features"]:
	distName=currDistrictFeature["properties"]['DISTRICT']
	st_cen_cd=currDistrictFeature["properties"]['ST_CEN_CD']
	st_name=currDistrictFeature["properties"]['ST_NM']
	censuscode=currDistrictFeature["properties"]['censuscode']
	geoms=currDistrictFeature["geometry"]
	listGeom=[]
	listGeom.append(geoms)
	geoms=listGeom
	with rasterio.open(tiffFileName) as src:
		out_image, out_transform = mask(src, geoms, crop=True)

	out_meta = src.meta.copy()

	# save the resulting raster  
	out_meta.update({"driver": "GTiff",
		"height": out_image.shape[1],
		"width": out_image.shape[2],
		"transform": out_transform})

	# path_to_district_tiffs=output_folder_path + '\\' + str(st_name)
	path_to_district_tiffs=output_folder_path
	pathlib.Path(path_to_district_tiffs).mkdir(parents=True, exist_ok=True)

	with rasterio.open(path_to_district_tiffs + distName + '@' + str(st_cen_cd) + '@' + str(censuscode) + ".tiff", "w", **out_meta) as dest:
		dest.write(out_image)
	#file will be saved as {district_name}@{ST_CEN_CD}@{CensusCode}.tiff