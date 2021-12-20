import os
import time
from typing import List, Tuple
import itertools


def process_image():
    [algorithm, image] = read_input(0)
    
    print(f"initial lit pixels", count_lit_pixels(image))

    number_of_enhances = 50

    infinity_char = "0"

    for i in range(number_of_enhances):  
        infinity_char = toggle_infinity_char(algorithm, infinity_char, i)      
        image = enhance(algorithm, infinity_char, image)
        
        print("enhance ", i + 1)
    

    print("lit pixels after enhance: ", count_lit_pixels(image))

def toggle_infinity_char(algorithm, infinity_char, iteration):
    
    if algorithm[0] == "1":
        infinity_char = str(iteration % 2)        

    return infinity_char

def count_lit_pixels(image: List[List[int]]):
    return len(list(filter(lambda point: point == "1", itertools.chain.from_iterable(image))))

def enhance(algorithm: List[int], infinity_char, image: List[List[int]]) -> List[List[int]]:
    max_x = len(image[0])
    max_y = len(image)
    new_max_x = max_x + 2
    new_max_y = max_y + 2

    new_image = []

    for x in range(new_max_x):
        new_row = []
        for y in range(new_max_y):
            index = calculate_index(image, x, y, max_x, max_y, infinity_char)
            # print(f"index: {index} pixel: {algorithm[index]}")
            new_row.append(algorithm[index])
        new_image.append(new_row)

    return new_image

def calculate_index(image: List[List[int]], image_x: int, image_y: int, max_x: int, max_y: int, infinity_char) -> int:
    index_string = ""    
    image_x = image_x - 1
    image_y = image_y - 1

    coordinates = [
        [image_x-1, image_y-1], [image_x-1, image_y], [image_x-1, image_y+1],
        [image_x, image_y-1], [image_x, image_y], [image_x, image_y+1],
        [image_x+1, image_y-1], [image_x+1, image_y], [image_x+1, image_y+1],
    ]

    for [x, y] in coordinates:
        if x < 0 or y < 0 or x >= max_x or y >= max_y:
            index_string += infinity_char        
        else:
            index_string += image[x][y]
    # print("index_string", index_string)
    return int(index_string, 2)

def read_input(test=0) -> Tuple[List[int], List[List[int]]]:
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

    algorithm = process_line(lines[0])

    image = [process_line(line) for line in lines[2:]]

    return [algorithm, image]

def process_line(line: str) -> List[str]:
    line = line.rstrip()
    result = []
    for char in line:
        if char == "#":
            result.append("1")
        elif char == ".":
            result.append("0")
        else:
            print("invalid input")
    return result

if __name__ == "__main__":
    start_time = time.time()
    process_image()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
