from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
from game.game_object import GameObject
from enum import Enum
if TYPE_CHECKING:
    from entity.character import Character
    from map.tiles.game_tile import GameTile


class QUEUE_PHASE(Enum):
    SPAWNING = 0
    MOVEMENT = 1
    ABILITIES = 2

class Team(GameObject):
    def __init__(self, team_id:int) -> None:
        self.team_id = team_id
        self.color: (int, int, int) = (0,0,0)
        self.characters: List[Character] = []
        self.vision_of: List[GameTile] = []

        self.queueing_phase = None

    def add_character(self, character_instance:Character):
        self.characters.append(character_instance)

    def remove_character_from_team(self, character):
        self.characters.remove(character)
    
    def set_main_base(self, base):
        self.main_base = base

    def start_of_game(self):
        pass
        #handle initial spawning

    def start_of_queue_phase(self):
        self.queueing_phase = QUEUE_PHASE.SPAWNING

    def turn_processing(self):
        for character in self.characters:
            character.turn_processing()
        
    def animate_turn(self):
        for character in self.characters:
            character.animate_turn()

    def end_of_turn(self):
        for character in self.characters:
            character.end_of_turn()