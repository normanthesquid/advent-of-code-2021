import os
from typing import Tuple
import time


def fold_paper():

    [grid, folds] = read_input(False)

    print(f"folds: {folds}")

    fold = folds[0]
    fold_index = int(fold[1])

    folded_grid = {}
    for key in grid.keys():
        [x, y] = [int(coordinate) for coordinate in key.split(",")]
        if fold[0] == "x":
            if x > fold_index:
                x = x - ((x - fold_index) * 2)
            folded_grid[f"{x},{y}"] = "#"

        if fold[0] == "y":
            if y > fold_index:
                y = y - ((y - fold_index) * 2)
            folded_grid[f"{x},{y}"] = "#"

    print(f"dots: {folded_grid}")
    print(f"dots: {len(folded_grid)}")


def read_input(test=False) -> Tuple[dict, list]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test:
        file_name = "test-input.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    grid = {}
    folds = []
    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith("fold"):
            folds.append(line[11:].split("="))
        else:
            grid[line] = "#"

    return [grid, folds]


if __name__ == "__main__":
    start_time = time.time()
    fold_paper()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
