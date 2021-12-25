import os
from typing import List
import time
from day_25.floor_cell import FloorCell


def move_herds(test=False):
    cells = read_input(test)

    cucumber_moved = True
    step_count = 0

    while cucumber_moved:
        # print_grid(cells)
        cucumber_moved = False

        east_cucumbers = list(filter(lambda cell: cell.east_cucumber, cells))

        moving_cucumbers: List[FloorCell] = []
        for cucumber in east_cucumbers:
            if (
                cucumber.east_neighbor.east_cucumber == False
                and cucumber.east_neighbor.south_cucumber == False
            ):
                cucumber_moved = True
                moving_cucumbers.append(cucumber)

        for cucumber in moving_cucumbers:
            cucumber.east_neighbor.east_cucumber = True
            cucumber.east_cucumber = False

        south_cucumbers = list(filter(lambda cell: cell.south_cucumber, cells))

        moving_cucumbers: List[FloorCell] = []
        for cucumber in south_cucumbers:
            if (
                cucumber.south_neighbor.east_cucumber == False
                and cucumber.south_neighbor.south_cucumber == False
            ):
                cucumber_moved = True
                moving_cucumbers.append(cucumber)

        for cucumber in moving_cucumbers:
            cucumber.south_neighbor.south_cucumber = True
            cucumber.south_cucumber = False

        step_count = step_count + 1
        print("completed step:", step_count)

    print("Finished after:", step_count)
    return step_count


def print_grid(cells: List[FloorCell]):
    for i in range(len(cells)):
        if i % 10 == 0:
            print("")
            print("row: ", end="")
        cell = "."
        if cells[i].east_cucumber:
            cell = ">"
        if cells[i].south_cucumber:
            cell = "v"
        print(cell, end="")
    print("")


def build_neighbors(grid, x, y, max_x, max_y):
    neighbors = []
    if y == 0:
        neighbors.append(grid[-1][x])
    if y > 0:
        neighbors.append(grid[y - 1][x])
    if x == 0:
        neighbors.append(grid[y][-1])
    if x > 0:
        neighbors.append(grid[y][x - 1])
    if y < max_y:
        south_neighbor = grid[y + 1][x]
    if y == max_y:
        south_neighbor = grid[0][x]
    neighbors.append(south_neighbor)
    if x < max_x:
        east_neighbor = grid[y][x + 1]
    if x == max_x:
        east_neighbor = grid[y][0]
    neighbors.append(east_neighbor)
    return (neighbors, east_neighbor, south_neighbor)


def read_input(test=False) -> List[FloorCell]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test:
        file_name = "test-input.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    grid = []
    with open(input_path) as file:
        lines = file.readlines()

    for line in lines:
        gridline = []
        for cell in list(line.rstrip()):
            gridline.append(FloorCell(cell))
        grid.append(gridline)

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    cells = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            [cell.neighbors, cell.east_neighbor, cell.south_neighbor] = build_neighbors(
                grid, x, y, max_x, max_y
            )

            cells.append(cell)

    return cells


if __name__ == "__main__":
    start_time = time.time()
    move_herds()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
