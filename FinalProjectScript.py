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
from Cell import Cell

#%% Initialize variables
v_max = 10
v_min = 0
v_threshold = 3
r_h = 1
r_v = 1
#%% Tissue with no blockage

tissue = t(50,50)
t.initialize_cardiac_cells(tissue, v_threshold, v_min, v_max, r_h, r_v)
for i in range(50):
    tissue.insert_pacer_cell(0,i,20,0)
t.simulate_tissue(tissue, 1000000,1,'Normal Electrical Activity of the Heart')

#%% Aberrant tissue 

tissue = t(50,50)

t.initialize_cardiac_cells(tissue, v_threshold, v_min, v_max, r_h, r_v)

for i in range(50):
    tissue.insert_pacer_cell(0,i,20,0)

for i in range(30):
    if i not in [15,16, 17]:
        tissue.kill_cell(25, i)
for i in range(30):
    if i not in [16, 17]:
        tissue.kill_cell(26, i)
for i in range(30):
    if i not in [17]:
        tissue.kill_cell(27, i)
    
tissue.tissue[27, 17] = heart_cell(2.1, v_min, v_max, r_h, r_v, 27, 17, .01)
tissue.tissue[26, 17] = heart_cell(2.1, v_min, v_max, r_h, r_v, 26, 17, .01)
tissue.tissue[28, 17] = heart_cell(4, v_min, v_max, r_h, r_v, 28, 17, .01)
tissue.tissue[26, 16] = heart_cell(2.1, v_min, v_max, r_h, r_v, 26, 17, .01)

tissue.initialize_scar()
t.simulate_tissue(tissue, 1000000,2,'Atrial Fibrillation')

#%% Ablated tissue 

ablated_tissue = t(50,50)

t.initialize_cardiac_cells(ablated_tissue, v_threshold, v_min, v_max, r_h, r_v)

for i in range(50):
    ablated_tissue.insert_pacer_cell(0,i,20,0)

for i in range(30):
        ablated_tissue.kill_cell(25, i)
for i in range(30):
        ablated_tissue.kill_cell(26, i)
for i in range(30):
        ablated_tissue.kill_cell(27, i)
        
ablated_tissue.initialize_scar()
t.simulate_tissue(ablated_tissue, 1000000,3 ,'Ablated Tissue')