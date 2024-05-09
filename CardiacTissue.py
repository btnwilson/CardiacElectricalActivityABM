# Import packages
import numpy as np
from matplotlib import pyplot as plt
import CardiacCell as c
from Cell import Cell
from PacerCell import PacerCell as pc

class CardiacTissue:

    def __init__(self, row, col):
        # Size of tissue - # rows
        self.row = row
        # Size of tissue - # columns
        self.col = col
        # Tissue array - size (row,col) dtype = Cell
        self.tissue = np.full((row, col), np.nan, dtype=Cell)
        # Voltage array for graphing - corresponds to tissue array
        self.voltage = np.full((row, col), np.nan)
        # Scar array for graphing - corresponds to tissue array
        self.scar = np.full((row, col), np.nan)

    # Getter - tissue array
    def get_tissue(self):
        return self.tissue

    # Initialize scar array with value 4 (for correct visual color) at coordinates where tissue array has a dead cell
    def initialize_scar(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.tissue[i, j].is_dead == True :
                    self.scar[i,j] = 4
                    

     # Initialize cardiac cells in tissue array
    def initialize_cardiac_cells(self, v_threshold, v_min, v_max, r_h, r_v):
        for i in range(self.row):
            for j in range(self.col):
                self.tissue[i, j] = c.heart_cell(v_threshold, v_min, v_max, r_h, r_v, i, j, time_step =.01)

    # Simulate tissue for a given number of iterations
    # Plot voltage value of each cell
    def simulate_tissue(self,  num_iterations, fig_number, title):
        plt.figure(fig_number)
        plt.title(title)
        tissue_plot = plt.imshow(self.voltage, cmap='magma', interpolation='nearest', vmin=0, vmax=10)
        scar_plot = plt.imshow(self.scar, cmap='binary', interpolation='nearest', vmin=0, vmax=10)
        tbar = plt.colorbar(tissue_plot, label = 'Voltage')
        plt.show()
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
                        if curr_cell.get_voltage() >= 0:
                            self.voltage[row, column] = curr_cell.get_voltage()
                        else:
                            self.voltage[row, column] = 0
                    else:
                        if curr_cell.get_voltage() >= 0:
                            self.voltage[row, column] = curr_cell.get_voltage()
                        else:
                            self.voltage[row, column] = 0

            tissue_plot.set_array(self.voltage)
            scar_plot.set_array(self.scar)
            plt.pause(0.001)
        plt.show()

    # Insert a pacer cell at a specific (row, column) coordinate
    def insert_pacer_cell(self, row, column, heartrate, offset):
        self.tissue[row, column] = pc(heartrate, offset)

    # kill_cell calls apatosis() function from cell classes to set voltage of specified cell to zero
    def kill_cell(self, row, column):
        self.tissue[row,column].apatosis()
