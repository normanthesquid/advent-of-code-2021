import os
import array


def process_readings():
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

    total_lines = len(lines)
    half_lines = total_lines / 2

    bits = array.array("i", (0 for i in range(0, 12)))

    for i in range(total_lines):
        for j in range(0, 12):
            bits[j] += int(lines[i][j])

    gamma_bits = ""
    epsilon_bits = ""

    for i in range(0, 12):
        if bits[i] > half_lines:
            gamma_bits += "1"
            epsilon_bits += "0"
        else:
            gamma_bits += "0"
            epsilon_bits += "1"

    print(f"gamma_bits: {gamma_bits}")

    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")

    print(f"power consumption: {epsilon * gamma}")


if __name__ == "__main__":
    process_readings()
