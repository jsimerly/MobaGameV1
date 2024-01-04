from entity.character import Character
from typing import List
from components.resources import RageResourceComponent, ResourceComponent
from .abilities import *

rage_resource = RageResourceComponent(max_resource=10)

class Crud(Character):
    def __init__(self, 
        #Comp dependancies
        health: int=1000, 
        movement_cost: int=1, 
        level_increments: List[int]=None, 
        vision_range: int=3, 
        resource_comp: ResourceComponent=rage_resource,

        #Abilities
        basic_ability: Ability=BasicAttack,
        ability_1: Ability=Slash,
        ability_2: Ability=SecondWind,
        ability_super: Ability=RecklessRage

      
    ):
        super().__init__(health, movement_cost, level_increments, vision_range, resource_comp, basic_ability, ability_1, ability_2, ability_super)

        self.took_damage_last_turn:bool = False  

    def activate_passive(self):
        if not self.took_damage_last_turn:
            self.health_component.heal(25)
        return super().activate_passive()
    







