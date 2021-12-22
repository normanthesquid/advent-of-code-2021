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

            low_points.append([x, y])

    print(f"low_points count: {len(low_points)}")
    basin_areas = []
    crawled_points = dict()
    for low_point in low_points:
        key = f"{low_point[0]}-{low_point[1]}"

        if key in crawled_points.keys():
            continue
        basin = dict()
        crawl_basin(heightmap, basin, max_x, max_y, low_point)
        basin_area = len(list(filter(lambda cell: cell != "X",  basin.values())))
        basin_areas.append(basin_area)
        crawled_points.update(basin)

    print(f"basin_areas count: {len(basin_areas)}")

    basin_areas.sort(reverse=True)

    
    print(f"basin_areas zero: {basin_areas[0]}")
    print(f"basin_areas one: {basin_areas[1]}")
    print(f"basin_areas two: {basin_areas[2]}")
    
    print(f"basin_areas score: {basin_areas[0] * basin_areas[1] * basin_areas[2]}")

def crawl_basin(heightmap, basin: dict, max_x, max_y, point):
    key = f"{point[0]}-{point[1]}"

    if key in basin.keys():
        return
    
    if heightmap[point[0]][point[1]] == 9:
        basin[key] = "X"
        return
    else:
        basin[key] = " "
    
    if point[0] != 0:
        crawl_basin(heightmap, basin, max_x, max_y, [point[0] - 1, point[1]])
    if point[0] != max_x - 1:
        crawl_basin(heightmap, basin, max_x, max_y, [point[0] + 1, point[1]])
    if point[1] != 0:
        crawl_basin(heightmap, basin, max_x, max_y, [point[0], point[1] - 1])
    if point[1] != max_y - 1:
        crawl_basin(heightmap, basin, max_x, max_y, [point[0], point[1] + 1])

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
