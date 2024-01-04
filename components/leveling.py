from typing import List
from component import Component

class LevelingComponent(Component):
    def __init__(self, pp_increments:List[int]=None):
        self.level = 1
        self.pp = 0
        self.pp_increments = pp_increments or [999, 2999]

    def check_for_level_up(self):
        if self.pp > self.pp_increments[self.level-1]:
            self.level_up()

    def level_up(self):
        self.level += 1

    def gain_pp(self, amount:int):
        self.pp += amount
        self.check_for_level_up()

    
