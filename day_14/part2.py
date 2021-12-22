from collections import defaultdict
import os
from typing import DefaultDict, Dict, Tuple
import time


def process_polymer():

    [template, rules] = read_input(False)

    print(f"rules: {rules}")
    
    # initial state
    pair_counts: Dict[str, int] = defaultdict(lambda: 0)    
    for key in rules.keys():
        pair_counts[key] = template.count(key)

    print(f"counts: {pair_counts.items()}")

    spawned_count: Dict[str, int] = defaultdict(lambda: 0)
    for char in list(template):
        spawned_count[char] = spawned_count[char] + 1

    for step in range(40):
        new_counts: Dict[str, int] = defaultdict(lambda: 0)
        for key, count in pair_counts.items():
            new_counts[rules[key][0]] = new_counts[rules[key][0]] + count
            new_counts[rules[key][1]] = new_counts[rules[key][1]] + count
            spawned_count[rules[key][2]] = spawned_count[rules[key][2]] + count

        pair_counts = new_counts
        
        print(f"After step {step + 1}: counts: {pair_counts.items()}")
       
    print(f"final_counts: {spawned_count}")  

    result = max(spawned_count.values()) - min(spawned_count.values())

    print(f"result: {result}") 


def read_input(test=False) -> Tuple[list, dict]:
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
    
    template = lines[0]
    rules = {}
    
    for line in lines[2:]:
        if len(line) == 0:
            continue
        [pair, insertion] = [part.rstrip() for part in line.split(" -> ")]
        rules[pair] = [pair[0] + insertion, insertion + pair[1], insertion]

    return [template, rules]


if __name__ == "__main__":
    start_time = time.time()
    process_polymer()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
