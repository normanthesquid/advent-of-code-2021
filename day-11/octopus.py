
from typing import List


class octopus:
    def __init__(self, energy_level):
        self.energy_level = energy_level        
        self.neighbors: List['octopus'] = []
        
        self.flashed_on_step = [False for _ in range(100)]
        self.flash_count = 0

    def increase_energy(self, step):
        self.energy_level += 1
        if self.energy_level > 9 and self.flashed_on_step[step] == False:
            self.flashed_on_step[step] = True
            self.flash_count += 1
            for neighbor in self.neighbors:
                neighbor.increase_energy(step)

    def end_step(self):
        if self.energy_level > 9:
            self.energy_level = 0

    
        

    
