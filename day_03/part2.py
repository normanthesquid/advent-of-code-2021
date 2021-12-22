import os
import array
from typing import List


def process_readings():
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    possible_o2_matches = lines.copy()
    best_o2_match = great_filter(possible_o2_matches, True)[0]

    possible_co2_matches = lines.copy()
    best_co2_match = great_filter(possible_co2_matches, False)[0]

    print(f"best_o2_match:  {best_o2_match}")
    print(f"best_co2_match: {best_co2_match}")

    o2_reading = int(best_o2_match, 2)
    co2_reading = int(best_co2_match, 2)

    print(f"o2_reading: {o2_reading}")
    print(f"co2_reading: {co2_reading}")

    print(f"life_support: {o2_reading*co2_reading}")


def great_filter(items: List[str], take_majority: bool):
    for j in range(0, 12):

        value_to_take = find_value_to_take(items, j, take_majority)

        filtered_items: List[str] = list(
            filter(lambda item: item[j] == value_to_take, items)
        )
        print(f"filter {j} count {len(items)} => {len(filtered_items)}")

        if len(filtered_items) == 1:
            return filtered_items

        if len(filtered_items) > 0:
            items = filtered_items

    return items


def find_value_to_take(items, index, take_majority: bool):
    total_items = len(items)
    ones = 0
    for i in range(total_items):
        if int(items[i][index]) == 1:
            ones += 1

    value = "0"
    if take_majority:
        if ones >= total_items / 2:
            value = "1"
        else:
            value = "0"
    else:
        if ones >= total_items / 2:
            value = "0"
        else:
            value = "1"

    print(f"taking {value} -- one count: {ones}:{len(items) - ones}")

    return value


if __name__ == "__main__":
    process_readings()
