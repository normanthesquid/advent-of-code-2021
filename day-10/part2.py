import os
from typing import List
import time
import statistics


def check_syntax():
    
    lines = read_input()    

    openers = ["(","[","{","<"]
    closers = [")","]","}",">"]

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    illegal_characters = []

    fixes = []

    for line in lines:        
        opener_stack = []
        fix = []
        bad_line = False  
        for glyph in line:
            if glyph in openers:
                opener_stack.append(glyph)                
            elif glyph in closers:
                if pairs[opener_stack[-1]] == glyph:
                    opener_stack.pop()
                else:
                    illegal_characters.append(glyph)
                    print(f"Expected {pairs[opener_stack[-1]]}, but found {glyph} instead.")
                    bad_line = True
                    break
            else:
                raise Exception(f"unexpected input: {glyph}")
        if(bad_line):
            continue

        fix = [pairs[glyph] for glyph in opener_stack]
        fix.reverse()
        fixes.append(fix)

    scores = {
        ")": 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    
    print(f"fixes count {len(fixes)}")

    print(f"fixes {fixes}")
    fix_scores = []
    for fix in fixes:
        score = 0
        for glyph in fix:
            score = 5*score + scores[glyph]
        fix_scores.append(score)

        
    print(f"fixe scores {fix_scores}")

    median_score = statistics.median(fix_scores)
    
    print(f"median_score {median_score}")


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
