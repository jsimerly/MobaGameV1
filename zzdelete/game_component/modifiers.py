from abc import ABC, abstractmethod
from entity import Entity
from game_component.abilities import GameAbility

class EntityModifer(ABC):
    def __init__(self, duration:int=None, specific_ability:GameAbility=None):
        self.duration = duration
        self.specific_ability = specific_ability

    @abstractmethod
    def apply(self, entity:Entity, duration:int=1):
        if self.specific_ability:
            return
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

class Shield(EntityModifer):
    def __init__(self, duration: int = None, specific_ability: GameAbility = None):
        super().__init__(duration, specific_ability)


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


