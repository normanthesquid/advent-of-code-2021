import os
from typing import Dict, List
import time
from cave_cell import CaveCell
import numpy


def find_path():
    cells = read_input(False)
    start = cells[0]
    end = cells[-1]
    visited_squares = []

    walk_graph_2(cells)
    # walk_graph(end, visited_squares)

    path_shortened = True
    cells.reverse()
    shortenings = 0
    while path_shortened:
        path_shortened = False
        for cell in cells:
            if cell.end:
                continue
            index = numpy.argmin([neighbor.distance_to_end for neighbor in cell.neighbors])
            current_shortest_neighbor = cell.neighbors[index]
            if current_shortest_neighbor != cell.shortest_neighbor:                
                cell.distance_to_end = cell.risk + current_shortest_neighbor.distance_to_end  
                cell.shortest_neighbor = current_shortest_neighbor
                path_shortened = True
        lowest_risk = min([neighbor.distance_to_end for neighbor in start.neighbors])
        print(f"current_shortest: {lowest_risk - start.risk}")
        shortenings += 1

    print_graph(start)

    lowest_risk = min([neighbor.distance_to_end for neighbor in start.neighbors])
   
    print(f"shortenings: {shortenings}")
    print(f"lowest_risk: {lowest_risk}")

def print_graph(current_square: CaveCell):
    print(f"risk: {current_square.risk} distance: {current_square.distance_to_end}")
    if current_square.end:
        return
    index = numpy.argmin([neighbor.distance_to_end for neighbor in current_square.neighbors])
    print_graph(current_square.neighbors[index])
    
def walk_graph_2(cells: List[CaveCell]):
    cells = cells.copy()
    cells.reverse()

    for current_square in cells:
        visited_neighbors = list(
            filter(
                lambda neighbor: neighbor.distance_to_end != None, current_square.neighbors
            )
        )
        if(current_square.end):
            current_square.distance_to_end = current_square.risk
            current_square.shortest_neighbor = 0
        else:    
            lowest_distance = min([neighbor.distance_to_end for neighbor in visited_neighbors])
            current_square.distance_to_end = current_square.risk + lowest_distance
            current_square.shortest_neighbor = lowest_distance


def walk_graph(current_square: CaveCell, visited_squares: List[CaveCell]):
    visited_neighbors = list(
        filter(
            lambda neighbor: neighbor.distance_to_end != None, current_square.neighbors
        )
    )
    if(current_square.end):
        current_square.distance_to_end = current_square.risk
        current_square.shortest_neighbor = 0
    else:    
        lowest_distance = min([neighbor.distance_to_end for neighbor in visited_neighbors])
        current_square.distance_to_end = current_square.risk + lowest_distance
        current_square.shortest_neighbor = lowest_distance
    visited_squares.append(current_square)

    for neighbor in current_square.neighbors:
        if neighbor not in visited_squares:
            walk_graph(neighbor, visited_squares)


def build_neighbors(grid, x, y, max_x, max_y):
    neighbors = []
    # if x > 0 and y > 0:
    #    neighbors.append(grid[x - 1][y - 1])
    if x > 0:
        neighbors.append(grid[x - 1][y])
    # if x > 0 and y < max_y:
    #    neighbors.append(grid[x - 1][y + 1])
    if y > 0:
        neighbors.append(grid[x][y - 1])
    # if x < max_x and y > 0:
    #    neighbors.append(grid[x + 1][y - 1])
    if x < max_x:
        neighbors.append(grid[x + 1][y])
    # if x < max_x and y < max_y:
    #    neighbors.append(grid[x + 1][y + 1])
    if y < max_y:
        neighbors.append(grid[x][y + 1])
    return neighbors


def read_input(test=False) -> List[CaveCell]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test:
        file_name = "test-input.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()
        grid = [[CaveCell(int(cell)) for cell in list(line.rstrip())] for line in lines]

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    cells = []
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            cell = grid[x][y]
            cell.neighbors = build_neighbors(grid, x, y, max_x, max_y)
            cells.append(cell)
    grid[-1][-1].end = True
    return cells


if __name__ == "__main__":
    start_time = time.time()
    find_path()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
