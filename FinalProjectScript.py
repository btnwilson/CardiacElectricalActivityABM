# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:40:55 2024

@author: bentn
"""
#%% Import packages
import numpy as np
from matplotlib import pyplot as plt
from CardiacCell import heart_cell
from CardiacTissue import CardiacTissue as t
#%% Set up tissue
#row_size = 10
#column_size = 10
#object_array = np.full((row_size, column_size), np.nan, dtype= heart_cell)

#v_max = 10
#v_min = 2
#v_threshold = 7
#r_h = 2
#r_v = 2


#for i in range(row_size):
#    for j in range(column_size):
 #       object_array[i,j] = heart_cell(v_threshold, v_min, v_max, r_h, r_v, i, j, time_step = .01)

#ap_array = np.full((200), 10, dtype=float)
#ap_array[0:75] = np.linspace(v_threshold, v_max, 75)
#ap_array[-75:] = np.linspace(v_max, v_threshold, 75)

#for step in range(10):
 ##   for row in range(row_size):
   #     for column in range(column_size):
    #        object_array[row, column].simulate_step(object_array, ap_array)
            
    #for row in range(row_size):
     #   for column in range(column_size):
      #      object_array[row, column].update_v_m()
#%% With tissue class
v_max = 10
v_min = 2
v_threshold = 7
r_h = 2
r_v = 2
tissue = t(10,10)
t.initialize_cardiac_cells(tissue, v_threshold, v_min, v_max, r_h, r_v)
t.simulate_tissue(tissue, 10)