# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:43:51 2020

@author: schmole04

Format:
    [[[Straße_Auto1, Lat_Auto1, Lon_Auto1, Zeitstempel], [Straße_Auto1, Lat_Auto1, Lon_Auto1, Zeitstempel2], [...]],
    [[Straße_Auto2, Lat_Auto2, Lon_Auto2, Zeitstempel], [Straße_Auto2, Lat_Auto2, Lon_Auto2, Zeitstempel2]], [[..], [...]]]
"""

 
import pickle
import random
import numpy as np


cars = []
for i in range(0, 10):
    cars.append([])

for i in range(100):
    for j in cars:
        street = random.randint(0, 10)
        lat = random.randint(45000, 48000)/1000
        lon = random.randint(7000, 8000)/1000
        j.append([street, lat, lon, i])
print(cars[0])

data = np.array(cars)

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)