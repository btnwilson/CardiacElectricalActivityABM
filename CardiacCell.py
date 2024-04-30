# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:38:10 2024

@author: bentn
"""
import numpy as np 
import CardiacTissue as t

class heart_cell:
    def __init__(self, v_threshold, v_min, v_max, r_h, r_v, row, column, time_step):
        self.v_m = v_min
        self.v_min = v_min
        self.v_max = v_max
        # self.t_active = t_activ
        self.plateau_time = 0 
        self.r_h = r_h
        self.r_v = r_v
        self.dv_dt = None
        self.row = row
        self.column = column
        self.v_next = None
        self.time_step = time_step
        self.is_diastolic = True
        self.ap_int = 0
        self.v_threshold = v_threshold
        self.ap_array = np.full((200), 10, dtype=float)
        self.ap_array[0:75] = np.linspace(v_threshold, v_max, 75)
        self.ap_array[-75:] = np.linspace(v_max, v_threshold, 75)
        
        
    def get_voltage(self):
        return self.v_m
    
    def compute_dv_dt(self, tissue):
        if self.is_diastolic:
            if self.row == 0:
                neighbor_left = 0
            else:
                neighbor_left = tissue[self.row - 1, self.column].get_voltage()
            # If the cell is at tissue row length -1
            if self.row == (np.size(tissue, 1) - 1):
                # Set voltage of neighbor right to zero (cell does not exist)
                neighbor_right = 0
            else:
                neighbor_right = tissue[self.row + 1, self.column].get_voltage()

            if self.column == 0:
                neighbor_down = 0
            else:
                neighbor_down = tissue[self.row, self.column - 1].get_voltage()
            # If the cell is at tissue column length -1
            if self.column == (np.size(tissue, 0) - 1):
                neighbor_up = 0
            else:
                neighbor_up = tissue[self.row, self.column + 1].get_voltage()

            self.dv_dt = (neighbor_left + neighbor_right - 2 * self.v_m) / self.r_h \
                         + (neighbor_up + neighbor_down - 2 * self.v_m) / self.r_v
        else:
            self.v_next = self.ap_array[self.ap_int]

    def update_voltage(self):
        self.v_next = self.v_m + self.dv_dt * self.time_step
    
    def update_v_m(self):
        self.v_m = self.v_next
    
    def simulate_step(self, array_of_cells):
        if self.v_m > self.v_threshold:
            self.is_diastolic = False
            self.ap_int += 1
        else:
            self.is_diastolic = True
            self.ap_int = 0
        self.compute_dv_dt(array_of_cells)
        self.update_voltage()



            
    
    