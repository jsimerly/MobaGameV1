from typing import Callable
from abc import ABC
from map.base import GameTile

class GameAbility(ABC):
    def __init__(self, 
        shape:Callable,
        shape_params:dict,
        resource_cost:int=0,

        damage:int=None, 
        friendly_fire:bool=True,
        healing:int=None,
        enemy_healing:bool=True,
        effect=None,

        is_piercing:bool=True,
        is_colliding:bool=True,
        effects_structures:bool=True,
    ):
        self.shape = shape
        self.shape_params = shape_params
        self.resource_cost = resource_cost

        self.damage = damage
        self.friendly_fire=friendly_fire
        self.healing = healing
        self.enemy_healing = enemy_healing
        self.effect = effect

        self.is_piercing = is_piercing
        self.is_colliding = is_colliding
        self.effects_structures = effects_structures

    def use(self, hex:GameTile):
        pass


#Automatically hits in a radius 
class AutoAbility(GameAbility):
    def __init__(self, 
        shape: Callable, 
        shape_params: dict,
        resource_cost: int = 0, 
        damage: int = None, 
        healing: int = None, 
        enemy_healing: bool = True, 
        effect=None
    ):
        super().__init__(shape, shape_params, resource_cost, damage, healing, enemy_healing, effect,
            friendly_fire=False,
            is_piercing=False,
        )

#Automatically hits but no collision
class AreaAffectAbility(GameAbility):
    def __init__(self, 
        shape: Callable, 
        shape_params: dict,
        resource_cost: int = 0, 
        damage: int = None, 
        healing: int = None, 
        enemy_healing: bool = True, 
        friendly_fire: bool = True,
        effect=None
    ):
        super().__init__(shape, shape_params, resource_cost, damage, healing, enemy_healing, effect, friendly_fire,
            is_piercing=True,
            is_colliding=False,
        )

#Is aimed but fixed to the character
class DirectionalAbility(GameAbility):
    def __init__(self, 
        shape: Callable, 
        shape_params: dict,
        resource_cost: int = 0, 
        damage: int = None, 
        healing: int = None, 
        enemy_healing: bool = True, 
        friendly_fire: bool = True,
        effect=None
    ):
        super().__init__(shape, shape_params, resource_cost, damage, healing, enemy_healing, effect, friendly_fire,
            is_piercing=True,
            is_colliding=False,
        )

#Is aimed, but can target an hex as the center point
class TargetedAbility(GameAbility):
    def __init__(self, 
        shape: Callable, 
        shape_params: dict,
        resource_cost: int = 0, 
        damage: int = None, 
        healing: int = None, 
        enemy_healing: bool = True, 
        friendly_fire: bool = True,
        effect=None
    ):
        super().__init__(shape, shape_params, resource_cost, damage, healing, enemy_healing, effect, friendly_fire,
            is_piercing=True,
            is_colliding=False,
        )

    def rotate(self):
        pass