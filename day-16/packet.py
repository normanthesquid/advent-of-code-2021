from typing import List


class Packet:
    literal_packet_type = 4

    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.length_type: int = None
        self.literal_value: int = None
        self.subpacket_length: int = None
        self.subpacket_count: int = None
        self.subpackets: List["Packet"] = []
