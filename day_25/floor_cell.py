from typing import List


class FloorCell:
    def __init__(self, definition: str):
        self.east_cucumber = False
        self.south_cucumber = False
        if definition == ">":
            self.east_cucumber = True
        if definition == "v":
            self.south_cucumber = True
        self.neighbors: List["FloorCell"] = []
        self.east_neighbor: "FloorCell" = None
        self.south_neighbor: "FloorCell" = None
