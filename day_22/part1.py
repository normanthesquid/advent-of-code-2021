import time
import os
from typing import List

from instruction import Instruction


def reboot_reactor():
    instructions = read_input(0)

    cubes = dict()

    for instruction in instructions:
        for cube in instruction.affected_cubes():
            cubes[cube] = instruction.on

    on_cubes = list(filter(lambda value: value == True, cubes.values()))

    print("on_cubes", len(on_cubes))


    
def read_input(test=0) -> List[Instruction]:
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
        return [Instruction(line.rstrip(), 50) for line in lines]

if __name__ == "__main__":
    start_time = time.time()
    reboot_reactor()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
