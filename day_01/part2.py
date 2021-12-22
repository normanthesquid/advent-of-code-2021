import os
from typing import List


def window_sum(lines: List[int], window_start: int):
    return lines[window_start] + lines[window_start + 1] + lines[window_start + 2]


def find_depth_increases():

    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    depth_increases = 0

    for i in range(len(lines) - 3):

        this_window_sum = window_sum(lines, i)
        next_window_sum = window_sum(lines, i + 1)
        if this_window_sum < next_window_sum:
            depth_increases += 1

    print(f"increases: {depth_increases}")


if __name__ == "__main__":
    find_depth_increases()
