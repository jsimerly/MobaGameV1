from typing import Callable

class LevelingComponent:
    def __init__(self, lvl:int, pp:int):
        self.lvl = lvl
        self.pp = pp

        self.lvl_2_pp_needed = 999
        self.lvl_3_pp_needed = 2999

    def gain_xp(self, pp:int):
        self.pp += pp

    def check_for_level_up(self):
        if self.lvl == 3:
            return

        if self.lvl == 1:
            if self.pp > self.lvl_2_pp_needed:
                self.level_up()
    
    def level_up(self, level_up_handler:Callable=None):
        self.lvl += 1
        if level_up_handler is not None:
            level_up_handler()

        #handle units and stuff