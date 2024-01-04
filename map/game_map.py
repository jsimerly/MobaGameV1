from map.tiles.game_tile import GameTile
from .map_loadout.map_loadout import MapLoadout
from hex import Point

class GameMap:
    def __init__(self, map_loadout:MapLoadout, screen):
        self.tiles = map_loadout.generate_map(screen)
        self.screen = screen
        self.layout = map_loadout.layout
        self.draw_coords = True

    def draw(self):
        for coord, tile in self.tiles.items():
            tile.draw(self.screen, self.draw_coords)

    

    def select_hex(self, mouse_pos):
        hex_coord = self.layout.pixel_to_hex(mouse_pos)
        print(hex_coord)
    



        


