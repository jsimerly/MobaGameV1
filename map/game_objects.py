from typing import Dict, List, Type
from base import GameTile, GameEdge
from events import MovementEventBase, OnEnterEvent, OnEotEvent, OnExitEvent, OnSotEvent
from map.base import EventHandler



class GameObject:
    def __init__(self, name:str, is_passible:bool, is_los:bool, is_hidden:bool):
        self.name = name
        self.is_passible = is_passible
        self.is_los = is_los
        self.is_hidden = is_hidden

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class EnviromentObject(GameObject):
    def __init__(self, name: str, is_passible: bool, is_los: bool, is_hidden: bool):
        super().__init__(name, is_passible, is_los, is_hidden)

class Objective(GameObject):
    def __init__(self, 
        name: str, 
        is_passible: bool, 
        is_los: bool, 
        is_hidden: bool,
        health: int,
        is_teleporter: bool,
        teleport_range: int,

    ):
        super().__init__(name, is_passible, is_los, is_hidden)
