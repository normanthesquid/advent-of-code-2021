from typing import List


class CaveCell:
    def __init__(self, cost):
        self.risk = cost
        self.end = False
        self.x = 0
        self.y = 0
        self.visited = False
        self.neighbors: List["CaveCell"] = []
        self.distance_to_end = 500*500*10
        self.shortest_neighbor: "CaveCell" = None
