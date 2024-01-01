from typing import Callable
from combat import AttackComponent, HealthComponent
from map.base import GameTile
from abc import ABC

class LevelingComponent:
    def __init__(self):
        self.lvl = 1
        self.pp = 0

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
                       

class CharacterAbility(ABC):
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



    def use(self, hex:GameTile):
        pass


#Automatically hits in a radius 
class AutoAbility(CharacterAbility):
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
class AreaAffectAbility(CharacterAbility):
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
class DirectionalAbility(CharacterAbility):
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
class TargetedAbility(CharacterAbility):
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


class Character:
    def __init__(self, 
        name:str,
        health:int,  
        resources:int,
        resource_name:str,
        basic_ability: CharacterAbility,
        ability_1: CharacterAbility, 
        ability_2: CharacterAbility, 
        super_ability: CharacterAbility,
        sprite,
    ):
        self.name = name
        self.resources = resources
        self.resource_name = resource_name

        self.basic_ability = basic_ability
        self.ability_1 = ability_1
        self.ability_2 = ability_2
        self.super_ability = super_ability
        self.leveling_component = LevelingComponent()
        self.health_component = HealthComponent(health)

    def use_basic_ability(self):
        self.basic_ability.use()
        self.resources -= self.basic_ability.resource_cost

    def draw(self):
        pass

    def __str__(self) -> str:
        return self.name
