from game.game_object import GameObject

class StatusEffect(GameObject):
    def __init__(self, duration:int=None):
        self.duration = duration or 1

class Slow(StatusEffect):
    pass

class Stun(StatusEffect):
    pass

class Blind(StatusEffect):
    pass

class Blur(StatusEffect):
    pass

class Root(StatusEffect):
    pass

class Disabled(StatusEffect):
    pass

class Statis(StatusEffect):
    pass