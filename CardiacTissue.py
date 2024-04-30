import numpy as np
from matplotlib import pyplot as plt
import CardiacCell as c
from Cell import Cell
from PacerCell import PacerCell as pc

class CardiacTissue:

    def __init__(self, row, col, heartrate):
        self.row = row
        self.col = col
        self.tissue = np.full((row, col), np.nan, dtype=Cell)
        self.voltage = np.full((row, col), np.nan)
        self.heartrate = heartrate

    def get_tissue(self):
        return self.tissue

    def initialize_cardiac_cells(self, v_threshold, v_min, v_max, r_h, r_v):
        for i in range(self.row):
            for j in range(self.col):
                self.tissue[i, j] = c.heart_cell(v_threshold, v_min, v_max, r_h, r_v, i, j, time_step =.01)

    def simulate_tissue(self, num_iterations):
        plt.figure()
        tissue_plot = plt.imshow(self.voltage, cmap='winter', interpolation='nearest', vmin=0, vmax=10)
        for step in range(num_iterations):
            for row in range(self.row):
                for column in range(self.col):
                    curr_cell = self.tissue[row, column]
                    curr_cell.simulate_step(self.tissue)

            for row in range(self.row):
                for column in range(self.col):
                    curr_cell = self.tissue[row, column]
                    if type(curr_cell) == c.heart_cell:
                        curr_cell.update_v_m()
                        self.voltage[row, column] = curr_cell.get_voltage()
                    else:
                        self.voltage[row, column] = curr_cell.get_voltage()

        tissue_plot.set_array(self.voltage)
        # plt.pause(0.1)
        plt.show()

    def insert_pacer_cell(self, row, column):
        self.tissue[row, column] = pc(self.heartrate)
