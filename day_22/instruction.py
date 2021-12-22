from typing import List, Tuple


class Instruction:
    def __init__(self, definition: str, space_limit: int = None):
        [on_definition, ranges] = definition.split()
        self.on = on_definition == "on"

        [x_range, y_range, z_range] = [
            axis_range[2:] for axis_range in ranges.split(",")
        ]
        [self.x_start, self.x_end] = [int(x) for x in x_range.split("..")]
        [self.y_start, self.y_end] = [int(x) for x in y_range.split("..")]
        [self.z_start, self.z_end] = [int(x) for x in z_range.split("..")]

        if space_limit:
            negative_space_limit = space_limit * -1
            if self.x_start < negative_space_limit:
                self.x_start = negative_space_limit
            if self.x_start > space_limit:
                self.x_start = None
            if self.x_end > space_limit:
                self.x_end = space_limit
            if self.x_end < negative_space_limit:
                self.x_end = None

            if self.y_start < negative_space_limit:
                self.y_start = negative_space_limit
            if self.y_start > space_limit:
                self.y_start = None
            if self.y_end > space_limit:
                self.y_end = space_limit
            if self.y_end < negative_space_limit:
                self.y_end = None

            if self.z_start < negative_space_limit:
                self.z_start = negative_space_limit
            if self.z_start > space_limit:
                self.z_start = None
            if self.z_end > space_limit:
                self.z_end = space_limit
            if self.z_end < negative_space_limit:
                self.z_end = None

    def parameters(self) -> Tuple[int, int, int, int, int, int]:
        return (
            self.x_start,
            self.x_end,
            self.y_start,
            self.y_end,
            self.z_start,
            self.z_end
        )

    def affected_cubes(self):
        affected_cubes = []
        if (
            self.x_start == None
            or self.x_end == None
            or self.y_start == None
            or self.y_end == None
            or self.z_start == None
            or self.z_end == None
        ):
            return affected_cubes
        for x in range(self.x_start, self.x_end + 1):
            for y in range(self.y_start, self.y_end + 1):
                for z in range(self.z_start, self.z_end + 1):
                    affected_cubes.append(f"{x}-{y}-{z}")

        return affected_cubes
