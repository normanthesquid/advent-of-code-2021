import os
from typing import List
from display import display
import time


def check_displays():

    displays = read_input()

    print(f"displays: {len(displays)}")

    result = sum([disp.numeric_output for disp in displays])

    print(f"result: {result}")


def read_input() -> List[display]:
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        displays = [display(line.rstrip()) for line in lines]

    return displays


if __name__ == "__main__":
    start_time = time.time()
    check_displays()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
