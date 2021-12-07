import os
from submarine import *


def process_commands():
    cur_path = os.path.dirname(__file__)

    print(f"Cur Path: {cur_path}")

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    print(f"Path: {input_path}")

    with open(input_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    sub = Submarine()

    for i in range(len(lines)):
        parse_command(sub, lines[i])

    print(f"output: {sub.x_position * sub.y_position}")


def parse_command(sub: Submarine, command: str):
    command_parts = command.split()

    if command_parts[0] == "forward":
        sub.forward(int(command_parts[1]))
    if command_parts[0] == "up":
        sub.up(int(command_parts[1]))
    if command_parts[0] == "down":
        sub.down(int(command_parts[1]))


if __name__ == "__main__":
    process_commands()
