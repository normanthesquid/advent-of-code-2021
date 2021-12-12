from typing import List


class cave:
    start_name = "start"
    end_name = "end"

    def __init__(self, name: str):
        self.name = name
        self.neighbors: List["cave"] = []
        self.big = name.isupper()
        self.abstracted_paths = 0
