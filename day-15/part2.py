import os
from typing import DefaultDict, Dict, List
import time
from cave_cell import CaveCell
import bisect


def find_path():
    cells = read_input(False)

    print(f"cell length: {len(cells)}")    

    start = cells[0]
    end = cells[-1]
    print(f"end cell: {end.risk}")   

    current_square = end
    end.distance_to_end = end.risk

    traversing = True
    
    checks = 0
    
    start_time = time.time()
    maximum_checks = 500 * 500

    unvisited_squares_dict = DefaultDict(lambda: [])
    unvisited_squares_dict[end.distance_to_end].append(end)
    value_queue = []

    while traversing:
        current_square.visited = True
        if current_square == start:
            break

        for neighbor in current_square.neighbors:
            if neighbor.visited == False:
                new_distance = neighbor.risk + current_square.distance_to_end
                if new_distance < neighbor.distance_to_end:
                    old_location = unvisited_squares_dict[neighbor.distance_to_end]
                    if neighbor in old_location:
                        unvisited_squares_dict[neighbor.distance_to_end].remove(neighbor)
                        value_queue.remove(neighbor.distance_to_end)
                    neighbor.distance_to_end = new_distance
                    unvisited_squares_dict[new_distance].append(neighbor)
                    bisect.insort(value_queue, neighbor.distance_to_end)                
        
        unvisited_squares_dict[current_square.distance_to_end].remove(current_square)

        current_square = get_next_square(unvisited_squares_dict, value_queue)
        
        checks += 1
        if checks % 100 == 0:
            estimated_remaining_checks = maximum_checks - checks 
            elapsed_time = time.time() - start_time
            time_per_check = elapsed_time/checks
            remaining_minutes = time_per_check * estimated_remaining_checks / 60
            print(f"current_shortest: {current_square.x},{current_square.y} : {current_square.distance_to_end} check: {checks}, {remaining_minutes} minutes remaining, time per check: {time_per_check}")
  
    print(f"distance: {current_square.distance_to_end - start.risk}")
    return

def get_next_square(unvisited_squares_dict, value_queue: List):    
    current_square = None
    
    while current_square == None:
        next_value = value_queue.pop(0)
        current_group = unvisited_squares_dict[next_value]
        if(len(current_group) > 0):
            current_square = current_group[0]

    return current_square

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
        grid = []
        for tile_row in range(5):
            for line in lines:   
                if len(line) == 0:
                    continue
                gridline = []                
                for tile_column in range(5):    
                    for cell in list(line.rstrip()):
                        risk = ((int(cell) + tile_row + tile_column - 1) % 9) + 1
                        gridline.append(CaveCell(risk))
                        pass
                grid.append(gridline)

    write_to_file(grid)
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1

    cells = []
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cell = grid[x][y]
            cell.x = x
            cell.y = y
            cell.neighbors = build_neighbors(grid, x, y, max_x, max_y)
            cells.append(cell)
    grid[-1][-1].end = True
    return cells


def write_to_file(grid:  List[List[CaveCell]]):
    cur_path = os.path.dirname(__file__)
    file_name = f"input\\output.csv"
    abs_file_path = os.path.join(cur_path, file_name)

    with open(abs_file_path, "w+") as output_file:
        for row in grid:        
            output_file.write(f"{str().join([str(cell.risk) for cell in row])}\n")

if __name__ == "__main__":
    start_time = time.time()
    find_path()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
