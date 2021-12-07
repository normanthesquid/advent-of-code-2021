import os
from lanternFish import lantern_fish
from collections import defaultdict


def simulate_fishes():

    fishes = read_input()

    cohorts = build_cohorts(fishes)

    simulation_days = 256

    for i in range(simulation_days):

        fish_count = sum([cohorts[cohort] for cohort in cohorts])
        print(f"day {i:>3}  cohorts: {len(cohorts):>4} fishes: {fish_count}")

        new_cohorts = defaultdict(int)
        for j in reversed(range(8 + 1)):
            if j == 0:
                new_cohorts[8] = cohorts[0]
                new_cohorts[6] += cohorts[0]
            else:
                new_cohorts[j - 1] = cohorts[j]
        cohorts = new_cohorts

    fish_count = sum([cohorts[cohort] for cohort in cohorts])
    print(f"fishes: {fish_count}")


def build_cohorts(fishes: list[lantern_fish]) -> dict:
    groups = defaultdict(int)

    for i in range(len(fishes)):
        groups[fishes[i].days_till_spawn] += 1

    cohorts = defaultdict(int)
    for key in range(8 + 1):
        count = 0
        if key in groups:
            count = groups[key]
        cohorts[key] = count

    return cohorts


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
    simulate_fishes()
