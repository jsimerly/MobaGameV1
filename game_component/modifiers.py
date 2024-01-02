from abc import ABC, abstractmethod
from entity import Entity

class EntityModifer(ABC):
    def __init__(self, duration:int=None):
        self.duration = duration

    @abstractmethod
    def apply(self, entity:Entity, duration:int=1):
        pass

    def reduce_duration(self):
        if self.duration:
            self.duration -= 1

# Combat
class AttackDamageMod(EntityModifer):
    def __init__(self, duration: int, strength:float=1):
        super().__init__(duration)
        self.strength = strength

class DamageTakenMod(EntityModifer):
    def __init__(self, duration: int, strength:float):
        super().__init__(duration)
        self.strength = strength

class HealingGivenMod(EntityModifer):
    def __init__(self, duration: int, strength:float):
        super().__init__(duration)
        self.strength = strength

class HealingTakenMod(EntityModifer):
    def __init__(self, duration: int, strength:float):
        super().__init__(duration)
        self.strength = strength


# CC
class SlowMod(EntityModifer):
    def __init__(self, duration: int=None, strength:int=1):
        super().__init__(duration)
        self.strength = strength

class Stun(EntityModifer):
    def __init__(self, duration: int):
        super().__init__(duration)

class Blind(EntityModifer):
    def __init__(self, duration: int):
        super().__init__(duration)

class Root(EntityModifer):
    def __init__(self, duration: int=None):
        super().__init__(duration)

class Silence(EntityModifer):
    def __init__(self, duration: int=None):
        super().__init__(duration)


