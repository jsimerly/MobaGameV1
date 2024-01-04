from typing import Callable, List
from abc import ABC
from map.base import GameTile, TileObserver, GameMap
from modifiers import EntityModifer
import random

class TileEffect(ABC):
    def __init__(self, 
        duration:int, 
        shape:Callable,
        shape_params:dict,
        
        effects_structures:bool=False, 
        is_immediate:bool=False,
    ):
        self.duration = duration
        self.remaining_duration = duration

        self.shape = shape
        self.shape_params = shape_params
        self.effects_structures = effects_structures
        self.is_immediate = is_immediate

    def apply(self):
        pass

class DamageEffect(TileEffect):
    def __init__(self, damage:int, duration:int=1, effects_structures:bool=False, exact:bool=False):
        super().__init__(duration, effects_structures)
        self.damage = damage
        self.exact = exact
        self.duration = duration

    def calculate_damage(self) -> int:
        damage = self.damage
        if self.exact:
            return damage
        
        # May skew this based on player psych findings
        mu = (damage[1] + damage[0])//4
        sigma = (damage[1] - damage[0])//4
        damage = int(random.gauss(mu, sigma)//1)

        return damage
    
    def apply(self, observer: TileObserver):
        observer.health_component.take_damage(self.damage)
    

class HealEffect(TileEffect):
    def __init__(self, healing:int, duration:int, effects_structures:bool=False):
        super().__init__(duration, effects_structures)
        self.healing = healing

    def apply(self, observer: TileObserver):
        observer.health_component.heal(self.healing)
    
        
class ModifierEffect(TileEffect):
    def __init__(self, modifier: EntityModifer, duration:int, effects_structures: bool = False):
        super().__init__(duration, effects_structures)
        self.modifier = modifier

    def apply(self, observer: TileObserver):
        observer.modifiers.append(self)


class GameAbility(ABC):
    def __init__(self, 
        name:str,
        resource_cost:int=0,

        effects: List[TileEffect] = [],

        is_piercing:bool=True,
        is_colliding:bool=True,
    ):
        self.name = name
        self.resource_cost = resource_cost

        self.effects = effects

        self.is_piercing = is_piercing
        self.is_colliding = is_colliding


    def cast(self, hex:GameTile, game_map:GameMap):
        #Calculate the shapes needed to work with
        #this is where you should actually handle collision and piercing
        targeted_tiles: List[GameTile] = []

        for effect in self.effects:
            #need to handle modifiers
            for tile in targeted_tiles:
                if effect.is_immediate:
                    tile.register_pre_combat_effect(effect)
                else:
                    tile.register_combat_effect(effect)
            

    def __str__(self) -> str:
        return self.name


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