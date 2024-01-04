from map.tiles.game_tile import GameTile
from .map_loadout.map_loadout import MapLoadout

class GameMap:
    def __init__(self, map_loadout:MapLoadout, screen):
        self.map = map_loadout.generate_map(screen)
        self.screen = screen
        self.layout = map_loadout.layout
        self.draw_coords = True

    def draw(self):
        for coord, tile in self.map.items():
            tile.draw(self.screen, self.draw_coords)
    



        


