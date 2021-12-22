from typing import List


class Instruction:
    def __init__(self, definition: str):
        [on_definition, ranges] = definition.split()
        self.on = on_definition == "on"

        [x_range, y_range, z_range] = [axis_range[2:] for axis_range in ranges.split(",")]
        [self.x_start, self.x_end] = [int(x) for x in x_range.split("..")]
        [self.y_start, self.y_end] = [int(x) for x in y_range.split("..")]
        [self.z_start, self.z_end] = [int(x) for x in z_range.split("..")]


        #self.affected_cubes = 

