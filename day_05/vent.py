from posixpath import split
from typing import List


class vent:
    def __init__(self, vent_definition: str):
        points = vent_definition.split(" -> ")
        start = [int(point) for point in points[0].split(",")]
        end = [int(point) for point in points[1].split(",")]

        self.points = []
        self.diagonal = False

        if start[0] != end[0] and start[1] != end[1]:
            self.diagonal = True

            run = end[0] - start[0]
            x_move = 1
            if run < 0:
                x_move = -1

            rise = end[1] - start[1]
            y_move = 1
            if rise < 0:
                y_move = -1

            for i in range(abs(rise) + 1):
                x = start[0] + (i * x_move)
                y = start[1] + (i * y_move)
                self.points.append([x, y])
        else:
            if start[0] != end[0]:
                if start[0] > end[0]:
                    start, end = end, start
                for i in range(end[0] - start[0] + 1):
                    self.points.append([start[0] + i, start[1]])
            else:
                if start[1] > end[1]:
                    start, end = end, start
                for i in range(end[1] - start[1] + 1):
                    self.points.append([start[0], start[1] + i])
