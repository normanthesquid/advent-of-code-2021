import os
from typing import List
import statistics
from display import display


def check_displays():

    displays = read_input()

    digit_segment_counts = [
        2,  # one
        4,  # four
        3,  # seven
        7,  # eight
    ]

    interesting_digit_count = sum(
        [
            len(
                list(
                    filter(
                        lambda output_value: len(output_value) in digit_segment_counts,
                        disp.output_values,
                    )
                )
            )
            for disp in displays
        ]
    )

    print(f"interesting_digit_count: {interesting_digit_count}")


def read_input() -> List[display]:
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        displays = [display(line.rstrip()) for line in lines]

    return displays


if __name__ == "__main__":
    check_displays()
