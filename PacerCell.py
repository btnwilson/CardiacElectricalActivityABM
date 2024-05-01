
import numpy as np
from Cell import Cell
class PacerCell(Cell):
    def __init__(self, heart_rate, offset):
        self.voltage = 0
        self.signal = self.generate_signal(heart_rate)
        self.index_location = offset
        self.is_dead = False

    def generate_signal(self, heart_rate):
        base_array = np.full((200), 10, dtype=float)
        base_array[0:75] = np.linspace(0, 10, 75)
        base_array[-75:] = np.linspace(10, 0, 75)
        rest_array = np.zeros((int((60000/heart_rate)-200)))
        final_array = np.append(base_array, rest_array)
        return final_array

    def simulate_step(self, array_of_cells):
        
        self.voltage = self.signal[self.index_location]
        if self.index_location == len(self.signal)-1:
            self.index_location = 0
        else:
            self.index_location += 1

    def get_voltage(self):
        return self.voltage
