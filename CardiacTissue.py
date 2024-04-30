import numpy as np
from matplotlib import pyplot as plt
import CardiacCell as c


class CardiacTissue:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.tissue = np.full((row, col), np.nan, dtype=c.heart_cell)
        self.voltage = np.full((row, col), np.nan)

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
                    curr_cell = self.tissue[row][column]
                    curr_cell.simulate_step(self.tissue)

            for row in range(self.row):
                for column in range(self.col):
                    curr_cell = self.tissue[row][column]
                    curr_cell.update_v_m()
                    self.voltage[row, column] = curr_cell.get_voltage()
                    tissue_plot.set_array(self.voltage)
                    #plt.pause(0.1)
                    plt.show()
