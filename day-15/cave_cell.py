from typing import List


class CaveCell:
    def __init__(self, cost):
        self.risk = cost
        self.end = False
        self.neighbors: List["CaveCell"] = []
        self.distance_to_end = None
        self.shortest_neighbor: "CaveCell" = None
