
import tensorflow as tf
# from keras.models import Sequential
# from keras.layers import Dense
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator


file = 'model_birddata.csv'
# file = 'Test_tensorflow_input.csv'

st=time.time()
data = pd.read_csv(file)
data = data.drop("Unnamed: 0",axis=1)
print('Read File:', time.time()-st)

# Need a good way to break up dataset into
# test and train data
###################################

print(data.head(1))


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

	dates_hist = dates_data.groupby(dates_data['SightingDate']).count()
	dates_hist = np.log10(dates_hist)
	dates_hist.plot(kind='bar',color='y')
	majorLocator = MultipleLocator(20)
	plt.xaxis.set_major_locator(majorLocator)
	plt.xticks(rotation=90)
	plt.subplots_adjust(bottom=0.25)


	plt.show()




# Boilerplate telling python to begin execution
# at function called "main()"
if __name__ == '__main__':
   main()