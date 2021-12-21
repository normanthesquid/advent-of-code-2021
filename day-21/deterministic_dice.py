from typing import List


class DeterministicDice:
    def __init__(self):
        self.last_roll = 0

    def roll(self):
        result = self.last_roll + 1
        self.last_roll = result
        if result == 100:
            self.last_roll = 0

        return result
