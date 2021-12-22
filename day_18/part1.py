import os
import time
from typing import List
import re
import math


def do_snail_homework():
    number_list = read_input(0)

    print(f"number_list: {number_list}")

    snail_number = number_list[0]
    for i in range(len(number_list) - 1):
        snail_number = f"[{snail_number},{number_list[i+1]}]"


        print(f"after addition: {snail_number}")

        exploded = True
        split = True
        while exploded or split:
            exploded = False
            split = False
            nested_depth = 0
            big_number_index = -1
            number_parts = []
            for j in range(len(snail_number)):
                if snail_number[j] == "[":
                    nested_depth += 1   
                elif snail_number[j] == "]":
                    nested_depth -= 1
                    if big_number_index == -1:
                        if len(number_parts) > 1:
                            big_number_index = j - (len(number_parts))
                        else:
                            number_parts = []
                elif snail_number[j] == ",":
                    if big_number_index == -1:
                        if len(number_parts) > 1:
                            big_number_index = j - (len(number_parts))
                        else:
                            number_parts = []   
                else:                    
                    if nested_depth == 5:
                        snail_number = explode(snail_number, j-1)
                        exploded = True
                        break  
                    elif big_number_index == -1:
                        number_parts.append(snail_number[j])
            if(big_number_index > -1):                                
                snail_number = split_snail_number(snail_number, big_number_index, int(str().join(number_parts)))
                split = True
        
        print(f"after reduction: {snail_number}")

    print(f"magnitude: {calculate_magnitude(eval(snail_number))}")

def explode(snail_number: str, start_index: int):
    pair_end = start_index + snail_number[start_index:].find("]") + 1
    pair = eval(snail_number[start_index:pair_end])

    previous_numbers = list(re.finditer(r'\d+', snail_number[:start_index]))
    if len(previous_numbers) > 0:
        new_snail_number = snail_number[0:previous_numbers[-1].start()]         
        new_snail_number += str(pair[0] + int(previous_numbers[-1].group()))
        new_snail_number += snail_number[previous_numbers[-1].start()+len(previous_numbers[-1].group()):start_index]
    else:
        new_snail_number = snail_number[0:start_index] 
    new_snail_number += "0"

    next_numbers = list(re.finditer(r'\d+', snail_number[pair_end:]))    
    if len(next_numbers) > 0:
        next_number_index = next_numbers[0].start() + pair_end
        
        new_snail_number += snail_number[pair_end:next_number_index]
        new_snail_number += str(pair[1] + int(next_numbers[0].group()))
        new_snail_number += snail_number[next_number_index+len(next_numbers[0].group()):]
    else:
        new_snail_number += snail_number[pair_end:] 
    
    print(f"after explode:  {new_snail_number}")
    return new_snail_number

def split_snail_number(snail_number: str, start_index: int, number: int):
    
    new_snail_number = snail_number[0:start_index]

    new_snail_number += f"[{math.floor(number/2)},{math.ceil(number/2)}]"

    new_snail_number += snail_number[start_index + len(str(number)):]

    print(f"after split:    {new_snail_number}")
    return new_snail_number

def calculate_magnitude(snail_number: list):

    if isinstance(snail_number[0], list):
        left_magnitude = calculate_magnitude(snail_number[0])
    else:
        left_magnitude = snail_number[0]

    if isinstance(snail_number[1], list):
        right_magnitude = calculate_magnitude(snail_number[1])
    else:
        right_magnitude = snail_number[1]


    return 3 * left_magnitude + 2 * right_magnitude




def read_input(test=0) -> List[str]:
    cur_path = os.path.dirname(__file__)

    file_name = "input.txt"
    if test > 0:
        file_name = f"test-input-{test}.txt"

    input_path = os.path.join(
        cur_path,
        "input",
        file_name,
    )

    with open(input_path) as file:
        lines = file.readlines()

    return [line.rstrip() for line in lines]


if __name__ == "__main__":
    start_time = time.time()
    do_snail_homework()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
