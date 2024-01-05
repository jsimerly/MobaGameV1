from map.tiles.game_tile import GameTile
from .map_loadout.map_loadout import MapLoadout
from hex import Point

class GameMap:
    def __init__(self, map_loadout:MapLoadout, screen):
        self.draw_coords = True

        self.tiles = map_loadout.generate_map(screen, self.draw_coords)
        self.screen = screen
        self.layout = map_loadout.layout
        

    def draw(self):
        for tile in self.tiles.values():
            tile.draw()


    



        


