import os
from typing import Dict, List
import time
from cave import cave
import itertools


def map_caves():

    caves = read_input(False)

    start = caves[cave.start_name]
    visited = []

    paths: List[List[str]] = []

    walk_graph(caves, start, visited, paths, False)

    path_strings = [str.join(",", path).replace("*", "") for path in paths]
    path_strings.sort()
    

    print(f"paths: {len(set(path_strings))}")


def walk_graph(
    caves: dict,
    current_cave: cave,
    visited_caves: List[str],
    paths: list,
    double_small_used,
):
    if current_cave.name == cave.end_name:        
        visited_caves.append(current_cave.name)
        paths.append(visited_caves)
        return

    if (
        current_cave.big == False
        and current_cave.name != cave.start_name
        and double_small_used == False
    ):
        branched_caves = visited_caves.copy()
        branched_caves.append(current_cave.name + "*")
        walk_neighbors(caves, current_cave, branched_caves, paths, True)

    visited_caves.append(current_cave.name)
    walk_neighbors(caves, current_cave, visited_caves, paths, double_small_used)


def walk_neighbors(
    caves: dict,
    current_cave: cave,
    visited_caves: List[str],
    paths: list,
    double_small_used,
):
    for neighbor in current_cave.neighbors:
        if neighbor.big or neighbor.name not in visited_caves:
            walk_graph(caves, neighbor, visited_caves.copy(), paths, double_small_used)


def read_input(test=False) -> dict:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test:
        file_name = "test-input-3.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    cave_names = list(
        set(itertools.chain.from_iterable([line.split("-") for line in lines]))
    )

    caves = {name: cave(name) for name in cave_names}

    for line in lines:
        [cave_one, cave_two] = line.split("-")
        caves[cave_one].neighbors.append(caves[cave_two])
        caves[cave_two].neighbors.append(caves[cave_one])

    return caves


if __name__ == "__main__":
    start_time = time.time()
    map_caves()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
