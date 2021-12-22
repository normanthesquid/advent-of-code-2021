import os
from typing import List
import statistics


def move_crabs():

    crab_positions = read_input()

    median_position = statistics.median(crab_positions)

    print(f"median_position: {median_position}")

    fuel_spent = sum([abs(position - median_position) for position in crab_positions])

    print(f"fuel_spent: {fuel_spent}")


def read_input():
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        line = file.readline()
        crabs = [int(crab.rstrip()) for crab in line.rstrip().split(",")]

    return crabs


if __name__ == "__main__":
    move_crabs()
