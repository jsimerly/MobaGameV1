from __future__ import annotations
import pygame
from map.base import GameMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from teams import Team


class GameManager:
    def __init__(self):
        self.is_running = False
        self.turn = 0

        self.map:GameMap = None
        self.team_1: Team = None
        self.team_2: Team = None

    def set_team(self, team: Team):
        if not self.team_1:
            self.team_1=team
            return
        self.team_2 = team

    def set_map(self, map: GameMap):
        self.map = map

    def start(self):
        if not self.team_1 or not self.team_2:
            raise ValueError("Need two teams to start the game.")
        
        while self.is_running:
            self.check_ready_for_game_processing()

    def check_ready_for_game_processing(self):
        if self.team_1.is_turn_complete and self.team_2.is_turn_complete:
            self.process_game_queue()   


    def handle_start_of_turn(self):
        self.turn += 1
        self.check_for_respawns()
        pass


    def handle_player_turns(self):
        pass

    def process_game_queue(self):
        self.process_movement()
        self.process_pre_combat()
        self.process_damage()
        self.process_deaths()
        self.process_healing()
        
        pass
    
    def process_movement(self):
        pass

    def process_pre_combat(self):
        pass

    def process_damage(self):
        pass

    def process_deaths(self):
        pass

    def check_for_respawns(self):
        team_1_respawns = self.team_1.get_respawn_ready()
        team_2_respawns = self.team_2.get_respawn_ready()

    def process_healing(self):
        pass

    def process_end_of_turn(self):
        pass


        