from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
if TYPE_CHECKING:
    from entity.character import Character
    from map.tiles.game_tile import GameTile


class Team:
    def __init__(self, team_id:int) -> None:
        self.team_id = team_id
        self.color: (int, int, int) = (0,0,0)
        self.characters: List[Character] = []
        self.vision_of: List[GameTile] = []

    def add_character(self, character_instance:Character):
        self.characters.append(character_instance)

    def remove_character_from_team(self, character):
        self.characters.remove(character)
    
    def set_main_base(self, base):
        self.main_base = base

