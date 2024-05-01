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
v_min = 2
v_threshold = 3
r_h = 1
r_v = 1
tissue = t(10,10, 60)
t.initialize_cardiac_cells(tissue, v_threshold, v_min, v_max, r_h, r_v)
tissue.insert_pacer_cell(0,4)
t.simulate_tissue(tissue, 10000)