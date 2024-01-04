from __future__ import annotations
import random
from hex import Layout, orientation_pointy, Point
from typing import Callable, List
from map.base import GameTile
from utils import PlayerError
from game_component.abilities import GameAbility
from abc import ABC, abstractmethod

hex_size = (30, 30)
origin = Point(800//2, 800//2)
layout = Layout(orientation=orientation_pointy, size=hex_size, origin=origin)

class AttackingComponent:
    def __init__(
        self,
        ability: GameAbility
    ):
        self.ability= ability
        self.damage_modifiers = []  
    
    def calculate_damage_done(self):
        # May skew this based on player psych findings
        mu = (damage[1] + damage[0])//4
        sigma = (damage[1] - damage[0])//4
        damage = int(random.gauss(mu, sigma)//1)
        return damage
    
    def use(self, target_hex:GameTile):
        self.ability.use(target_hex)

class HealingComponent:
    def __init__(
        self,
        ability: GameAbility
    ):
        self.ability= ability
        self.healing_modifiers = []

class HealthComponent:
    def __init__(self, health):
        self.health = health
        self.alive = True

        self.damage_reduction_modifiers = []
        self.healing_taken_modifiers = []
        self.sheild_modifiers = []

    def take_damage(self, damage):
        if self.alive:
            self.health -= damage
            if self.health <= 0:
                self.die()

    def die(self, death_handler:Callable=None):
        if death_handler is not None:
            death_handler()

        self.alive = False

class MovementComponent:
    def __init__(self, movement_cost: int):
        self.movement_cost = movement_cost
        self.is_slowed = False
        self.is_rooted = False
        self.movement_modifiers = []

    #path finding algo that returns an ordered list of game tiles for movement
    #this will need to include slows and rough terrain
    def find_path(self, entity, to_tile) -> (int, List[GameTile]):
        pass


    def prepare_move(self, entity, to_tile: GameTile) -> int:
        if isinstance(entity, Character):
            move_distance = entity.game_tile.distance_to(to_tile)
            slow_modifier = 2 if self.is_slowed else 1
            total_move_cost = slow_modifier * self.movement_cost * move_distance

            if total_move_cost > entity.resources:
                raise PlayerError('You cannot move this far this turn.')
            
            entity.move(to_tile)
            return total_move_cost
        
class LevelingComponent:
    def __init__(self):
        self.lvl = 1
        self.pp = 0

        self.lvl_2_pp_needed = 999
        self.lvl_3_pp_needed = 2999
        self.leveling_modifiers = []

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
            
class VisionComponent:
    def __init__(self, range):
        self.range = range