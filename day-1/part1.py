import os


def find_depth_increases():

    cur_path = os.path.dirname(__file__)

    print(f"Cur Path: {cur_path}")

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    print(f"Path: {input_path}")

    with open(input_path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    # loop through items

    depth_increases = 0

    for i in range(len(lines)):
        if i == 0:
            continue

        if lines[i] > lines[i - 1]:
            depth_increases += 1

    print(f"increases: {depth_increases}")
    # if i > i-1, j++


if __name__ == "__main__":
    find_depth_increases()
