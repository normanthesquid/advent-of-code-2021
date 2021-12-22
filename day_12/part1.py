import os
from typing import Dict, List
import time
from cave import cave
import itertools


def map_caves():

    caves = read_input(False)

    start = caves[cave.start_name]

    paths: List[List[cave]] = []
    visited = []
    walk_graph(caves, start, visited, paths)

    path_count = sum([1 + sum([c.abstracted_paths for c in path])   for path in paths])

    print(f"paths: {path_count}")
    
def walk_graph(caves:dict, current_cave: cave, visited_caves: List[cave], paths:list):
    visited_caves.append(current_cave)
    for neighbor in current_cave.neighbors:        
        if neighbor.big or neighbor not in visited_caves:
            walk_graph(caves, neighbor, visited_caves.copy(), paths)
    if(visited_caves[-1].name == cave.end_name):
        paths.append(visited_caves)
    


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

    leaves_pruned = prune_small_leaves(caves)
    while leaves_pruned:
        leaves_pruned = prune_small_leaves(caves)

    return caves


def prune_small_leaves(caves: Dict[str, cave]):
    pruned = False
    
    cave_to_inspect: cave
    for cave_to_inspect in caves.copy().values():
        if (
            cave_to_inspect.name == cave.start_name
            or cave_to_inspect.name == cave.end_name
        ):
            continue
        if len(cave_to_inspect.neighbors) == 1:
            if (
                cave_to_inspect.neighbors[0].name == cave.start_name
                or cave_to_inspect.neighbors[0].name == cave.end_name
            ):
                continue

            if cave_to_inspect.neighbors[0].big == True:
                cave_to_inspect.neighbors[0].abstracted_paths += cave_to_inspect.abstracted_paths + 1
            
            cave_to_inspect.neighbors[0].neighbors.remove(cave_to_inspect)
            caves.pop(cave_to_inspect.name)
            pruned = True
            print(f"pruned: {cave_to_inspect.name}")

    return pruned


if __name__ == "__main__":
    start_time = time.time()
    map_caves()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
