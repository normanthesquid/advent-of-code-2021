import os
from typing import List
import time


def check_syntax():
    
    lines = read_input()
    
    opener_stack = []

    openers = ["(","[","{","<"]
    closers = [")","]","}",">"]

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    illegal_characters = []

    for line in lines:        
        for glyph in line:
            if glyph in openers:
                opener_stack.append(glyph)                
            elif glyph in closers:
                if pairs[opener_stack[-1]] == glyph:
                    opener_stack.pop()
                else:
                    illegal_characters.append(glyph)
                    print(f"Expected {pairs[opener_stack[-1]]}, but found {glyph} instead.")
                    break
            else:
                raise Exception(f"unexpected input: {glyph}")

    scores = {
        ")": 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }

    score = sum([scores[glyph] for glyph in illegal_characters])
    
    print(f"score {score}")


def read_input(test = False) -> List[str]:
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
        stripped_lines = [line.rstrip() for line in lines]

    return stripped_lines


if __name__ == "__main__":
    start_time = time.time()
    check_syntax()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
