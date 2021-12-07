import os
from typing import List
from vent import vent


def navigate_vents():

    vents = read_input()

    print(f"vents: {len(vents)}")

    vent_grid = dict()

    for i in range(len(vents)):
        for j in range(len(vents[i].points)):
            point = vents[i].points[j]
            point_key = f"{point[0]}-{point[1]}"

            if point_key not in vent_grid:
                vent_grid[point_key] = 0
            vent_grid[point_key] += 1

    intersection_count = 0

    for key in vent_grid:
        if vent_grid[key] > 1:
            intersection_count += 1

    write_to_file(vent_grid)
    print(f"intersection_count: {intersection_count}")


def write_to_file(grid: dict):
    cur_path = os.path.dirname(__file__)
    file_name = f"input\\output-2.csv"
    abs_file_path = os.path.join(cur_path, file_name)

    with open(abs_file_path, "w+") as output_file:
        for id in grid:
            output_file.write(f"{id}:{grid[id]}\n")


def read_input():
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        vents = [vent(line.rstrip()) for line in lines]

    return vents


if __name__ == "__main__":
    navigate_vents()
