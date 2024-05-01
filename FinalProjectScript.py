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


#%% With tissue class
v_max = 10
v_min = 0
v_threshold = 3
r_h = 1
r_v = 1
tissue = t(50,50)
#scar = t(50,50)
t.initialize_cardiac_cells(tissue, v_threshold, v_min, v_max, r_h, r_v)
# t.initialize_scar(tissue)
# t.initialize_scar(scar)

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
tissue.tissue[26, 16] = heart_cell(4, v_min, v_max, r_h, r_v, 26, 17, .01)

tissue.initialize_scar()

# tissue.insert_pacer_cell(12,12,120,300)
# tissue.insert_pacer_cell(20,12,100,200)
# tissue.insert_pacer_cell(15,20,90,50)
#tissue.insert_pacer_cell(38,41,150,80)
t.simulate_tissue(tissue, 1000000)