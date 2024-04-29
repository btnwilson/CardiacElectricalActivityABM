# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:38:10 2024

@author: bentn
"""
import numpy as np 


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
        # self.t_plat = t_plat_sec * time_step
        # self.t_plat_counter = 0
        self.ap_int = 0
        self.v_threshold = v_threshold
        # self.is_prev_syst = False 
        
        
    def get_voltage(self):
        return self.v_m
    
    def compute_dv_dt(self, array_of_cells):
        if self.row == 0:
            neighbor_left = 0
        else:
            neighbor_left = array_of_cells[self.row - 1, self.column].get_voltage()
       
        if self.row == 9:
            neighbor_right = 0
        else:
            neighbor_right = array_of_cells[self.row + 1, self.column].get_voltage()
       
        if self.column == 0:
            neighbor_down = 0
        else:
            neighbor_down =  array_of_cells[self.row, self.column - 1].get_voltage()
      
        if self.column == 9:
            neighbor_up = 0
        else:
            neighbor_up = array_of_cells[self.row, self.column + 1].get_voltage()
            
        self.dv_dt = (neighbor_left + neighbor_right - 2 * self.v_m)/self.r_h \
            + (neighbor_up + neighbor_down - 2 * self.v_m)/self.r_v
    
    def update_voltage(self):
        self.v_next = self.v_m + self.dv_dt * self.time_step
    
    def update_v_m(self):
        self.v_m = self.v_next
    
    def simulate_step(self, array_of_cells, ap_array):
        if self.v_m > self.v_threshold:
            self.is_diastolic = False
            self.ap_int += 1
        else:
            self.is_diastolic = True
            self.ap_int = 0
            
        if self.is_diastolic:
            self.compute_dv_dt(array_of_cells)
            self.update_voltage()
        else:
            self.v_next = ap_array[self.ap_int]
            
            
    
    