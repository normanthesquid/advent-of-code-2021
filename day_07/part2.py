import os
from typing import List
import math


def move_crabs():

    crab_positions = read_input()

    mean_position = math.floor(sum(crab_positions) / len(crab_positions))

    print(f"mean_position: {mean_position}")

    fuel_spent = sum(
        [
            calculate_fuel_cost(abs(position - mean_position))
            for position in crab_positions
        ]
    )

    print(f"fuel_spent: {fuel_spent}")


def calculate_fuel_cost(distance):
    cost = 0
    for i in range(distance + 1):
        cost += i

    return cost


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
