import urllib.request
import os 
import pathlib

DATASET_DIR = pathlib.Path('./datasets')
weather_station_dataset = DATASET_DIR / 'weather_station_data.parquet'
nc_dataset = DATASET_DIR / 'berkeley_earth.nc'

datasets = [(weather_station_dataset, 'https://s3.amazonaws.com/sea-datasets/weather_station_data.parquet')]#, (nc_dataset)]

for dataset in datasets:
    if not DATASET_DIR.exists():
        os.mkdir(DATASET_DIR)
    if not dataset[0].exists():
        print('Downloading', dataset[0])
        f = urllib.request.urlretrieve(dataset[1], dataset[0])
        print('Finished downloading......')
        