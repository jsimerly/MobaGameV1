from typing import Dict, List, Type
from base import GameTile, GameEdge
from abc import ABC
from game_component.entity import Entity

class MapEdge:
    def __init__(self, 
        hex1: GameTile, #This is the parent Hex, the hex that will be passable down but not up
        hex2: GameTile, #Child Hex
        is_passable: bool, 
        is_directional: bool, 
        is_los: bool, 
        sprite,
    ):
        self.hex1 = hex1
        self.hex2 = hex2
        self.is_passable = is_passable
        self.is_directional = is_directional
        self.is_los = is_los
        self.sprite = sprite

    def check_passability(self, to_hex):
        if self.is_directional and to_hex == self.hex1:
            return False
        return self.is_passable
    


class MapObject(ABC):
    def __init__(self, 
        name:str, 
        is_passable:bool, 
        is_los:bool, 
        is_concealing:bool,
        sprite
    ):
        self.name = name
        self.is_passable = is_passable
        self.is_los = is_los
        self.is_concealing = is_concealing
        self.sprite = sprite
        self.observers = []

    def perform_start_of_turn(self):
        pass

    def perform_end_of_turn(self):
        pass

    def perform_on_enter(self):
        pass

    def perform_on_exit(self):
        pass

    def draw(self):
        pass

    def clear(self):
        pass

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class EnviromentBase(MapObject):
    def __init__(self,
        name: str, 
        is_passable: bool, 
        is_los: bool, 
        is_concealing: bool,
        sprite,
    ):
        super().__init__(name, is_passable, is_los, is_concealing, sprite)





