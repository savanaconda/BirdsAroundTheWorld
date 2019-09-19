# Birds Around the World

Creating a model to predict species movement with data from Cornell's eBird database

Accessed csv file of eBird Observation Dataset from Cornell Lab of Ornithology
on Global Biodiversity Information Facility (GBIF) website:
https://www.gbif.org/dataset/4fa7b334-ce0d-4e88-aaae-2e0c138d049e

Created a csv file **model_birddata.csv** (see Birds-Database repo) with relevant data from original file and some feature
engineered parameters (X,Y,Z coordinates and Absolute Date)

Plotted maps of sighting and further analysis to come in **birds_model.py**

Plot of bird sightings across the globe (based on X,Y,Z coordinates calculated from Latitude and Longitude). View is from the top of
the globe, with North Pole labelled:
![alt text](https://github.com/savanaconda/Birds-Model/blob/master/Plots/BirdSightingsAcrossTheGlobe.png)

Plot of bird sightings across the world:
![alt text](https://github.com/savanaconda/Birds-Model/blob/master/Plots/BirdSightingsAcrossTheWorld.png)

Histogram of sightings over time:
![alt text](https://github.com/savanaconda/Birds-Model/blob/master/Plots/NumberOfSightingsOverTime.png)

Sightings of a particular species of bird over the world. This function can be called to view the sightings of any
specified species. Color of points moves from yellow to the red, with yellow being the least recent and red being the
most recent sighting:
![alt text](https://github.com/savanaconda/Birds-Model/blob/master/Plots/SightingsOfParticularBirdOverTime.png)
