import os
from typing import DefaultDict, Tuple
import time


def fold_paper():

    [template, rules] = read_input(False)

    print(f"folds: {rules}")
    
    for step in range(10):
        output = [template[0]]
        for i in range(len(template)):
            if i < len(template) - 1:
                pair = f"{template[i]}{template[i + 1]}"
                output.append(rules[pair])
                output.append(template[i + 1])
        template = output
        s = ""

        if step < 4:
            print(f"After step {step + 1}: {s.join(template)}")        
        else:
            print(f"After step {step + 1}: len {len(template)}")

    groups = DefaultDict(lambda: 0)    
    for i in range(len(template)):
        groups[template[i]] += 1
    
    print(f"groups: {groups}")  

    result = max(groups.values()) - min(groups.values())

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
    
    template = list(lines[0])
    rules = {}
    
    for line in lines[2:]:
        if len(line) == 0:
            continue
        [pair, insertion] = [part.rstrip() for part in line.split(" -> ")]
        rules[pair] = insertion        

    return [template, rules]


if __name__ == "__main__":
    start_time = time.time()
    fold_paper()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
