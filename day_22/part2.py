from collections import defaultdict
import time
import os
from typing import Dict, List, Tuple
import re

from day_22.instruction import Instruction


def reboot_reactor(input_file_number = 0):
    instructions = read_input(input_file_number)

    cubes: Dict[Tuple[int, int, int, int, int, int], int] = defaultdict(int)

    counter = 0
    for instruction in instructions:
        counter += 1
        print(f"processing instruction {counter} of {len(instructions)}")
        
        parameters = instruction.parameters()

        for existing_parameters, existing_value in cubes.copy().items():
            instersection = intersect(*parameters, *existing_parameters)
            if instersection != None:
                cubes[instersection] -= existing_value

        if instruction.on:
            cubes[parameters] += 1

    on_cubes = 0

    for cube, value in cubes.items():
        on_cubes += size(*cube) * value

    print("on_cubes", on_cubes)

    return on_cubes


def size(x, X, y, Y, z, Z):
    return (X - x + 1) * (Y - y + 1) * (Z - z + 1)


def intersect(
    x, X, y, Y, z, Z, u, U, v, V, w, W
) -> Tuple[int, int, int, int, int, int]:
    x = max(x, u)
    y = max(y, v)
    z = max(z, w)
    X = min(X, U)
    Y = min(Y, V)
    Z = min(Z, W)
    if x <= X and y <= Y and z <= Z:
        return x, X, y, Y, z, Z
    return None


def read_input(test=3) -> List[Instruction]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test > 0:
        file_name = f"test-input-{test}.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()
        return [Instruction(line.rstrip()) for line in lines]


if __name__ == "__main__":
    start_time = time.time()
    reboot_reactor(3)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
