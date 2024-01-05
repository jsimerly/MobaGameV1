from map.tiles.game_tile import GameTile
from game.game_object import GameObject
from .map_loadout.map_loadout import MapLoadout
from hex import Point

class GameMap(GameObject):
    def __init__(self, map_loadout:MapLoadout, screen):
        self.draw_coords = True

        self.tiles = map_loadout.generate_map(screen, self.draw_coords)
        self.screen = screen
        self.layout = map_loadout.layout

        self.structures = []
        self.objectives = []

    def draw(self):
        for tile in self.tiles.values():
            tile.draw()

    # These event methods are called the Game Manage (brock_purdy.py)
    def animate_turn(self):
        pass

    def end_of_turn(self):
        pass


    



        


