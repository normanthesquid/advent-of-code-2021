import os
from typing import List
from lanternFish import lantern_fish
import time


def simulate_fishes():

    fishes = read_input()

    simulation_days = 80

    for i in range(simulation_days):

        print(f"day {i:>2} fishes: {len(fishes)}")
        spawned_fishes = []
        for j in range(len(fishes)):
            spawn = fishes[j].age_up_and_check_spawn()
            if spawn == True:
                spawned_fishes.append(lantern_fish())
        fishes.extend(spawned_fishes)

    print(f"fishes: {len(fishes)}")


def write_to_file(grid: dict):
    cur_path = os.path.dirname(__file__)
    file_name = f"input\\output.csv"
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
        line = file.readline()
        fishes = [lantern_fish(int(fish.rstrip())) for fish in line.rstrip().split(",")]

    return fishes


if __name__ == "__main__":
    start_time = time.time()
    simulate_fishes()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
