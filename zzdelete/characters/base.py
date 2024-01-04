from typing import Callable, List
from game_component.entity_components import AbilityComponent, HealthComponent, MovementComponent, LevelingComponent, GameAbility
from map.base import GameTile
from abc import ABC
from utils import PlayerError
from game_component.entity import Entity


class Character(Entity):
    def __init__(self, 
        name: str, 
        health: int, 
        movement_cost: int, 
        basic_ability: GameAbility, 
        sprite,

        resource_pool:int,
        resource_name:str,
        ability_1: GameAbility,
        ability_2: GameAbility,
        super_ability: GameAbility,
    ):
        super().__init__(name, health, basic_ability, sprite, movement_cost)
        self.resource_pool = resource_pool
        self.resource_name = resource_name
        self.ability_1 = ability_1
        self.ability_2 = ability_2
        self.super_ability = super_ability
        

    def move(self, to_tile: GameTile):
        self.movement_component.find_path()
