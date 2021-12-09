import os
from typing import List
import time


def process_heightmap():

    heightmap = read_input()

    max_x = len(heightmap[0])
    max_y = len(heightmap)

    low_points = []

    for x in range(max_x):        
        for y in range(max_y):
            point = heightmap[x][y]

            if x != 0 and point >= heightmap[x - 1][y]:
                continue
            if y != 0 and point >= heightmap[x][y - 1]:
                continue
            
            if x != max_x - 1 and point >= heightmap[x + 1][y]:
                continue
            if y != max_y - 1 and point >= heightmap[x][y + 1]:
                continue

            low_points.append(point)

    total_risk = sum([low_point + 1 for low_point in low_points])
    print(f"total_risk: {total_risk}")


def read_input() -> List[List[int]]:
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        heightmap = [[int(cell) for cell in list(line.rstrip()) ] for line in lines]

    return heightmap


if __name__ == "__main__":
    start_time = time.time()
    process_heightmap()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
