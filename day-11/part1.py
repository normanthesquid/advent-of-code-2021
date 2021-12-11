import os
from typing import List
import time
from octopus import octopus


def watch_octopi():
    
    octopi = read_input(False)

    for step in range(100):
        for oct in octopi:
            oct.increase_energy(step)

        for oct in octopi:
            oct.end_step()

    score = sum([oct.flash_count for oct in octopi])

    print(f"score: {score}")


def read_input(test = False) -> List[octopus]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if(test):
        file_name = "test-input.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()
        cells = [[octopus(int(cell)) for cell in list(line.rstrip()) ] for line in lines]

    octopi = []

    for x in range(10):
        for y in range(10):
            oct = cells[x][y]
            
            if x > 0 and y > 0:
                oct.neighbors.append(cells[x-1][y-1])
            if x > 0:
                oct.neighbors.append(cells[x-1][y])
            if x > 0 and y < 9:
                oct.neighbors.append(cells[x-1][y+1])            
            if y > 0:
                oct.neighbors.append(cells[x][y-1])
            if x < 9 and y > 0:
                oct.neighbors.append(cells[x+1][y-1])
            if x < 9:
                oct.neighbors.append(cells[x+1][y])
            if x < 9 and y < 9:
                oct.neighbors.append(cells[x+1][y+1])            
            if y < 9:
                oct.neighbors.append(cells[x][y+1])

            octopi.append(oct)

    return octopi


if __name__ == "__main__":
    start_time = time.time()
    watch_octopi()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
