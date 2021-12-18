import os
from typing import Dict
import time


def fire_ze_missiles():

    [x_bounds, y_bounds] = read_input(False)

    min_x_velocity = 1
    max_x_velocity = x_bounds[1] + 2
    min_y_velocity = y_bounds[0] - 2
    max_y_velocity = 1000   

    print(f"min_x_velocity: {min_x_velocity}")
    print(f"max_x_velocity: {max_x_velocity}")
    print(f"min_y_velocity: {min_y_velocity}")
    print(f"max_y_velocity: {max_y_velocity}")
    
    x_velocities = [x for x in range(min_x_velocity, max_x_velocity)]
    y_velocities = [y for y in range(min_y_velocity, max_y_velocity)]
    max_ys = []
    
    shots = [[x, y]for x in x_velocities for y in y_velocities]

    launch_probe(6, 0, x_bounds, y_bounds)

    print(f"shooting {len(shots)} missiles")
    for [x_velocity, y_velocity] in shots:
        max_y = launch_probe(x_velocity, y_velocity, x_bounds, y_bounds)
        if max_y != None:
            max_ys.append(max_y)

    max_y = max(max_ys)
    print(f"hits: {len(max_ys)}")


def launch_probe(x_velocity, y_velocity, x_bounds, y_bounds):
    x_position = 0
    y_position = 0
    max_y = 0
    while y_position >= y_bounds[0]:
        x_position = x_position + x_velocity
        y_position = y_position + y_velocity
        if y_position > max_y:
            max_y = y_position

        if (
            x_bounds[0] <= x_position
            and x_position <= x_bounds[1]
            and y_bounds[0] <= y_position
            and y_position <= y_bounds[1]
        ):
            return max_y
        if x_velocity > 0:
            x_velocity = x_velocity - 1
        y_velocity = y_velocity - 1

    return None


def read_input(test=False) -> Dict:
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
        line = file.readlines()[0].rstrip()

    x_start = line.find("x") + 2
    x_end = line.find(",")
    y_start = line.find("y") + 2

    x_bounds = [int(coord) for coord in line[x_start:x_end].split("..")]
    y_bounds = [int(coord) for coord in line[y_start:].split("..")]

    print(f"x_bounds: {x_bounds}")
    print(f"y_bounds: {y_bounds}")
    
    return [x_bounds, y_bounds]


if __name__ == "__main__":
    start_time = time.time()
    fire_ze_missiles()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
