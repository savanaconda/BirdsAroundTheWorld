
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator
from datetime import datetime, timedelta


file = 'model_birddata.csv'
# file = 'Test_tensorflow_input.csv'

st=time.time()
data = pd.read_csv(file)
data = data.drop("Unnamed: 0",axis=1)
print('Read File:', time.time()-st)

# Need a good way to break up dataset into
# test and train data
###################################


# Plots coordinates on a globe
def plot_3D_coords(coords_data, col_names):

	# Include blue circle as background
	img = plt.imread(".\\Images\\bluecircle.png")
	fig, ax = plt.subplots()
	ax.imshow(img, extent=[-100000, 100000, -100000, 100000])

	# Add actual data to plot
	ax.scatter(coords_data['Y_coordinates'], coords_data['X_coordinates'],c='m', marker = 'x')

	# Add label showing where north pole is
	ax.plot([0], [0], 'o', c='k')
	ax.annotate('North Pole', xy=(0, 0), xytext=(-20000, 5000))

	# Add graph features
	ax.set_title('Bird Sightings Across The Globe')
	plt.axis('off')


# Plots coordinates on a world map
def plot_gps_coords(gps_data, col_names):

	# Include world map as background
	img = plt.imread(".\\Images\\worldmap.png")
	fig, ax = plt.subplots()
	ax.imshow(img, extent=[-180, 180, -90, 90])

	# Add actual data to plot
	ax.scatter(gps_data['Longitude'], gps_data['Latitude'], c='m', marker = 'x')

	# Add graph features
	ax.set_title('Bird Sightings Across The World')
	ax.set_xlabel('Longitude')
	ax.set_ylabel('Latitude')


# Gets a date from a correctly formatted string
def getdateformat(string):
	date = datetime.strptime(string, '%Y-%m-%d')
	return date


# Plots the number of sightings over time, binning dates
def plot_sightings_over_time(dates_data,dates_cols, bin_freq, num_ticks):

	# Sort dates in order from oldest to newest
	dates_data = dates_data.sort_values('SightingDate')

	# Transform SightingDate column from strings to dates
	dates_data['SightingDate'] = dates_data['SightingDate'].apply(getdateformat)

	# Creates binned date entries
	min_val = dates_data['SightingDate'].iloc[0]
	max_val = dates_data['SightingDate'].iloc[-1]

	# Round up for bin period to make sure to get final bin for range
	bin_period = np.ceil((max_val - min_val)/bin_freq)
	bins_dt = pd.date_range(start=min_val,end=max_val, periods=bin_period).strftime('%Y-%m-%d')
	bins_dt = pd.DatetimeIndex(bins_dt)

	bins_str = bins_dt.astype(str).values
	labels = ['({}, {}]'.format(bins_str[i-1], bins_str[i]) for i in range(1, len(bins_str))]
	binned = pd.DataFrame()
	binned['BinnedDates'] = pd.cut(dates_data['SightingDate'].astype(np.int64)//10**9,
                   bins=bins_dt.astype(np.int64)//10**9,
                   labels=labels)
	binned = binned.reset_index(drop=True)

	# Adds the count of sightings to each bin (getting histogram data)
	dates_hist = binned.groupby('BinnedDates').size()

	# Plot data
	fig, ax = plt.subplots()
	ax = dates_hist.plot.bar(color='y')

	# Sets xticks and xlabels (specified by num_ticks)
	interval = round(len(dates_hist)/num_ticks)
	labels = dates_hist.iloc[::interval].index.values
	labels_format = []
	for val in labels:
		split = val.split(',')
		labels_format.append(split[0] + ' to \n' + split[1])
	# if you delete this, then you don't love me - max
	ticks = np.arange(0, len(dates_hist), interval)

	# Format plot
	ax.set_xticks(ticks)
	ax.set_xticklabels(labels_format, rotation=90, ha='center')
	plt.subplots_adjust(bottom=0.30)
	ax.set_title('Number of Sightings Over Time')
	ax.set_xlabel('Date ranges')
	ax.set_ylabel('Number of Sightings')

def track_species_overtime(data, speciesname):
	speciesdata = data.loc[data['Species'] == speciesname]

	num_sightings = len(speciesdata)

	# Include world map as background
	img = plt.imread(".\\Images\\worldmap.png")
	fig, ax = plt.subplots()
	ax.imshow(img, extent=[-180, 180, -90, 90])

	# Add actual data to plot
	ax.scatter(speciesdata['Longitude'], speciesdata['Latitude'], c=speciesdata['AbsoluteDate'], marker = 'x', cmap='YlOrRd')

	# Add graph features
	ax.set_title('Sightings of ' + speciesname + ' over time')
	ax.set_xlabel('Longitude')
	ax.set_ylabel('Latitude')

	ax.annotate('More red = more recent \nMore yellow = less recent', xy=(0, 0), xytext=(40, -160))
	ax.annotate('Number of Sightings = ' + str(num_sightings), xy=(0, 0), xytext=(50, 140))


def main():

	# Plot coordinates on globe
	coords_cols = ['X_coordinates', 'Y_coordinates', 'Z_coordinates'].copy()
	coords_data = data[coords_cols].copy()
	plot_3D_coords(coords_data, coords_cols)

	# Plot coordinates on map
	gps_cols = ['Latitude', 'Longitude']
	gps_data = data[gps_cols].copy()
	plot_gps_coords(gps_data, gps_cols)

	# Plot dates
	dates_cols = ['SightingDate', 'AbsoluteDate']
	dates_data = data[dates_cols].copy()

	# Sets the number of days per bin
	bin_freq = '200D'
	num_ticks = 12
	plot_sightings_over_time(dates_data,dates_cols, bin_freq, num_ticks)


	print(data.columns.values)
	print(data.index.values)

	# Where is birb going?
	speciesname = 'Setophaga magnolia'
	track_species_overtime(data, speciesname)

	plt.show()




# Boilerplate telling python to begin execution
# at function called "main()"
if __name__ == '__main__':
   main()