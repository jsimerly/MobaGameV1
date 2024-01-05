from __future__ import annotations
from team.team import Team
from map.game_map import GameMap
from entity.entity import Entity
from typing import TYPE_CHECKING
from .game_object import GameObject

if TYPE_CHECKING:
    from map.tiles.game_tile import GameTile

class GameManager(GameObject):
    def __init__(self):
        self.player_1 = None
        self.player_2 = None

        self.team_1 = Team(team_id=1)
        self.team_2 = Team(team_id=2)
        self.game_map: GameMap = None

        self.selected_tile: GameTile = None

    def add_player(self, player) -> int:
        if not self.player_1:
            self.player_1 = player
            return 1
        if not self.player_2:
            self.player_2 = player
            return 2
       
        raise ValueError("There are already two players assigned to this game.")
        
    def remove_player(self, player):
        if player == self.player_1:
            self.player_1 = None
        if player == self.player_2:
            self.player_2 = None

    def set_game_map(self, game_map:GameMap):
        self.game_map = game_map

    def get_tile_under_mouse(self, mouse_pos) -> GameTile:
        hex_coord = self.game_map.layout.pixel_to_hex_coord(mouse_pos)
        q, r, s = hex_coord
        try:
            return self.game_map.tiles[(q,r)]
        except KeyError:
            return None
        
    def select_tile(self, selected_tile: GameTile):
        if selected_tile:
            if self.selected_tile:
                #have to redraw neighbors to remove the outline's effect
                self.deselect_tile(self.selected_tile)
            
            self.selected_tile = selected_tile
            selected_tile.set_selected()

    def deselect_tile(self, deselected_tile: GameTile):
        hex_neighbors =  deselected_tile.get_all_neighors()
        self.selected_tile.deselect()

        for hex in hex_neighbors:
            axial_coord = (hex.q, hex.r)
            tile = self.game_map.tiles[axial_coord]
            tile.draw()

    def start_of_game(self):
        self.team_1.start_of_game()
        self.team_2.start_of_game()

    def turn_processing(self):
        self.team_1.turn_processing()
        self.team_2.turn_processing()

    def animate_turn(self):
        self.team_1.animate_turn()
        self.team_2.animate_turn()
        self.game_map.animate_turn()

    def post_death_actions(self):
        self.game_map.animate_turn()

    def end_of_turn(self):
        self.team_1.end_of_turn()
        self.team_2.end_of_turn()
        self.game_map.end_of_turn()


    



        


   



    