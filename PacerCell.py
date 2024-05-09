# Import packages
import numpy as np
from Cell import Cell

# PacerCell 'is-a' Cell
class PacerCell(Cell):
    def __init__(self, heart_rate, offset):
        # Voltage of cell
        self.voltage = 0
        # Signal generated from specified heart rate
        self.signal = self.generate_signal(heart_rate)
        # index_location is the starting index of the signal array - can be used to manipulate aberrant beats
        self.index_location = offset
        # Representing cell state
        self.is_dead = False

    # Creates array of voltage values for a pacer cell to reflect input heartrate.
    def generate_signal(self, heart_rate):
        base_array = np.full((200), 10, dtype=float)
        base_array[0:75] = np.linspace(0, 10, 75)
        base_array[-75:] = np.linspace(10, 0, 75)
        rest_array = np.zeros((int((60000/heart_rate)-200)))
        final_array = np.append(base_array, rest_array)
        return final_array

    # Iterate through signal array to update voltage
    def simulate_step(self, array_of_cells):
        
        self.voltage = self.signal[self.index_location]
        if self.index_location == len(self.signal)-1:
            self.index_location = 0
        else:
            self.index_location += 1

    # Returns voltage
    def get_voltage(self):
        return self.voltage

    # Sets cell state to dead
    def apatosis(self):
        self.is_dead = True