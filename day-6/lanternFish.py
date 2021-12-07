from posixpath import split
from typing import List


class lantern_fish:
    def __init__(self, days_till_spawn: int = None):
        if days_till_spawn == None:
            self.days_till_spawn = 8
        else:
            self.days_till_spawn = days_till_spawn

    def age_up_and_check_spawn(self):
        self.days_till_spawn -= 1
        if self.days_till_spawn < 0:
            self.days_till_spawn = 6
            return True
        return False
