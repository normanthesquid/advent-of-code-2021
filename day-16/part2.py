import os
import time
from typing import List
from packet import Packet
from packet_types import Packet_Types


def parse_transmission():
    transmissions = read_input(0)

    for bit_string in transmissions:
        print(f"bit_string: {bit_string}")

        cursor = 0
        [packet, cursor] = parse_packet(cursor, bit_string)

        value = calculate_value(packet)

        print(f"value: {value}")

def calculate_value(packet: Packet):
    if packet.type == Packet_Types.SUM.value:
        return calculate_sum(packet)
    elif packet.type == Packet_Types.PRODUCT.value:
        return calculate_product(packet)
    elif packet.type == Packet_Types.MINIMUM.value:
        return min([calculate_value(subpacket) for subpacket in packet.subpackets])
    elif packet.type == Packet_Types.MAXIMUM.value:
        return max([calculate_value(subpacket) for subpacket in packet.subpackets])
    elif packet.type == Packet_Types.LITERAL.value:
        return packet.literal_value
    elif packet.type == Packet_Types.GREATER_THAN.value:
        return int(calculate_value(packet.subpackets[0]) > calculate_value(packet.subpackets[1]))
    elif packet.type == Packet_Types.LESS_THAN.value:
        return int(calculate_value(packet.subpackets[0]) < calculate_value(packet.subpackets[1]))
    elif packet.type == Packet_Types.EQUAL_TO.value:
        return int(calculate_value(packet.subpackets[0]) == calculate_value(packet.subpackets[1]))
    else:
         print(f"unknown packet type: {packet.type}")


def calculate_sum(packet: Packet):
    sum = 0
    for subpacket in packet.subpackets:
        subpacket_value = calculate_value(subpacket)
        sum += subpacket_value
    return sum 

def calculate_product(packet: Packet):
    product = 1
    for subpacket in packet.subpackets:
        subpacket_value = calculate_value(subpacket)
        product *= subpacket_value
    return product 
            
def parse_packet(cursor, bit_string):
    version_start = cursor
    version_end = cursor + 3    
    cursor += 3
    version = int(bit_string[version_start:version_end], 2)

    type_start = cursor
    type_end = cursor + 3    
    cursor += 3
    type = int(bit_string[type_start:type_end], 2)

    packet = Packet(version, type)

    if type == Packet_Types.LITERAL.value:
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

    transmissions = []
    for line in lines:
        num_of_bits = len(line.rstrip()) * 4
        transmissions.append(bin(int(line.rstrip(), 16))[2:].zfill(num_of_bits))

    return transmissions


if __name__ == "__main__":
    start_time = time.time()
    parse_transmission()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
