from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from game_manager import GameManager

class Team:
    def __init__(self, player, game_manager: GameManager):
        self.player = ''
        self.game_manager = game_manager
        self.spawn_time = 1
        self.color = ''
        self.is_turn_complete = False
        
        self.character_1 = None
        self.character_2 = None
        self.character_3 = None
        self.characters = [self.character_1, self.character_2, self.character_3]

    def set_character(self, character):
        if not self.character_1:
            self.character_1 = character
        elif not self.character_2:
            self.character_2 = character
        elif not self.character_3:
            self.character_3 = character
        else:
            raise ValueError("This team already has 3 characters selected.")
        
    def is_ready_for_game_start(self):
        return all([
            self.player,
            self.color,
            self.character_1,
            self.character_2,
            self.character_3
        ])

    def handle_start_of_turn(self):
        self.is_turn_complete = False

        # self.character_1.start_of_turn()
        # self.character_2.start_of_turn()
        # self.character_3.start_of_turn()

    def get_respawn_ready(self):
        characters_ready_for_respawn = []
        for character in self.characters:
        #if character.is_ready_for_respawn():
            characters_ready_for_respawn.append(character)
        return character


    def queue_action(self, character):
        pass

    def handle_end_turn(self):
        self.is_turn_complete=True
        self.game_manager.check_ready_for_game_processing()

    


