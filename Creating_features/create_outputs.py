# this file is used to generate the output csv file.
import tifffile as tf
import json
import sys
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import pickle

np.seterr(divide='ignore', invalid='ignore')

data_resolution = '500'
# Path of folder where district-wise tiff files are stored
input_path = input_path = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Creating_features/districtTiffFiles500_2011/"
total_bands = 13
year_of_sat_image = 2011
total_bins = 10
binning_strategy = 'quantile'
# File path followed by name to store the pickle file for created bins
bins_pickle_path = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Creating_features/bin_pickle_2011/"
bins_pickle_name = 'bins_' + str(total_bins) + '_' + binning_strategy + '_' + str(year_of_sat_image) + '_pickle_' + data_resolution
bins_pickle_file = open(join(bins_pickle_path, bins_pickle_name), 'rb')
bins_pickle = pickle.load(bins_pickle_file)
# File path and name(with extension) to save the feature file created at the end
feature_file_path = "/home/aygupt/Desktop/A.Seth Project/Landset Imagery/Creating_features/Outputs"
feature_file_name = '2011_districts_quant.csv'

dist_tiff_names = [f for f in listdir(input_path) if isfile(join(input_path, f))]
flattened_DataDictionary={}
printing_dictionary={}

for band_id in range(total_bands):
	dist_counter = 0
	for current_dist_file in dist_tiff_names:
		dist_counter += 1
		print(f'band: {band_id} dist#: {dist_counter}\t name: {current_dist_file}', end='\t')
		current_dist_file_path = join(input_path, current_dist_file)
		image = tf.imread(current_dist_file_path, key=0)
		imagenum=np.array(image)
		# break
		if(band_id<10):
			current_dist_data = np.array(image)[:,:, band_id]
		elif(band_id==10): #ndvi
			current_dist_data = np.array((image[:,:,3]-(image)[:,:,2])/((image)[:,:,3]+(image)[:,:,2]))
		elif(band_id==11): #ndbi
			current_dist_data = np.array((image[:,:,4]-(image)[:,:,3])/((image)[:,:,3]+(image)[:,:,4]))	
		elif(band_id==12): #mndwi
			current_dist_data = np.array((image[:,:,1]-(image)[:,:,4])/((image)[:,:,1]+(image)[:,:,4]))

		dist_data_flattened = current_dist_data.flatten()
		# Remove nan and zero values
		dist_data_flattened = dist_data_flattened[~np.isnan(dist_data_flattened)]
		dist_data_flattened = dist_data_flattened[dist_data_flattened != 0]
		
		# Replaces the previous value of the key with new one.
		flattened_DataDictionary[current_dist_file] = dist_data_flattened
		print('---Completed')

	if band_id == 9:
		continue
	bins = bins_pickle[band_id][0]

	print('band_id = ', band_id, ' bins = ', bins)
	for key, val in flattened_DataDictionary.items():
		tempArray = val.copy()
		binning = np.histogram(tempArray, bins=bins)
		str1 = key
		str2 = str1[:-5] # to remove .tif from file name
		distName_st_cen_cd_censuscode = str2.split('@') 
		if distName_st_cen_cd_censuscode == "0" : 
			continue 
		if band_id == 0:
			currArray = np.array([int(distName_st_cen_cd_censuscode[2])])
			currArray = np.append(currArray,binning[0])
			printing_dictionary[distName_st_cen_cd_censuscode[2]] = currArray
		else:
			currArray = np.array(binning[0])
			printing_dictionary[distName_st_cen_cd_censuscode[2]] = np.append(printing_dictionary[distName_st_cen_cd_censuscode[2]],currArray)

output_col_list = ['0']
col_temp = []

output_col_list.extend([str(i) for i in range(1,121)])
district_df = pd.DataFrame.from_dict(printing_dictionary, orient='index', columns=output_col_list)
print(district_df.shape)
district_df = district_df.sort_values(['0'])
district_df = district_df[1:]

district_df.to_csv(join(feature_file_path, feature_file_name), index=False)
