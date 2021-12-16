import os
import time
from packet import Packet


def parse_transmission():
    bit_string = read_input(0)

    print(f"bit_string: {bit_string}")

    cursor = 0
    [packet, cursor] = parse_packet(cursor, bit_string)

    version_sum = 0
    [version_sum, packet_count] = calculate_version_sum(packet)

    print(f"version_sum: {version_sum}")
    print(f"packet_count: {packet_count}")


def calculate_version_sum(packet: Packet):
    sum = packet.version
    packet_count = 1
    for subpacket in packet.subpackets:
        [subpacket_version_sum, subpacket_count] = calculate_version_sum(subpacket)
        packet_count += subpacket_count
        sum += subpacket_version_sum

    return [sum, packet_count]
            
def parse_packet(cursor, bit_string):
    version_start = cursor
    version_end = cursor + 3    
    cursor += 3
    version = int(bit_string[version_start:version_end], 2)

    type_start = cursor
    type_end = cursor + 3    
    cursor += 3
    type = int(bit_string[type_start:type_end], 2)
    
    print(f"version: {version} type: {type}")

    packet = Packet(version, type)

    if type == Packet.literal_packet_type:
        literal_string = ""
        parsing_literal_value = True
        while parsing_literal_value:
            if bit_string[cursor] == "0":
                parsing_literal_value = False
            cursor += 1
            byte_start = cursor
            byte_end = cursor + 4
            cursor = cursor + 4
            
            literal_string += bit_string[byte_start:byte_end]

        packet.literal_value = int(literal_string, 2)

        print(f"packet.literal_value: {packet.literal_value}")
    else:
        packet.length_type = int(bit_string[cursor])
        cursor += 1

        if packet.length_type == 0:
            subpacket_start = cursor
            subpacket_end = cursor + 15
            cursor += 15
            packet.subpacket_length = int(bit_string[subpacket_start:subpacket_end], 2)

            subpackets_end = cursor + packet.subpacket_length

            parsing_subpackets = True
            while parsing_subpackets:
                [subpacket, cursor] = parse_packet(cursor, bit_string)
                packet.subpackets.append(subpacket)
                if cursor >= subpackets_end:
                    parsing_subpackets = False

            
        if packet.length_type == 1:
            subpacket_start = cursor
            subpacket_end = cursor + 11
            cursor += 11
            packet.subpacket_count = int(bit_string[subpacket_start:subpacket_end], 2)  

            for i in range(packet.subpacket_count):
                [subpacket, cursor] = parse_packet(cursor, bit_string)
                packet.subpackets.append(subpacket)

    return [packet, cursor]

def read_input(test=0) -> str:
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

    num_of_bits = len(lines[0].rstrip()) * 4
    return bin(int(lines[0].rstrip(), 16))[2:].zfill(num_of_bits)


if __name__ == "__main__":
    start_time = time.time()
    parse_transmission()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
