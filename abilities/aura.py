from game.game_object import GameObject
class Aura(GameObject):
    def __init__(self, duration:int, radius):
        self.duration = duration