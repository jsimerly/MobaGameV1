from map.tiles.game_tile import GameTile
from map_loadout.map_loadout import MapLoadout

class GameMap:
    def __init__(self, map_loadout:MapLoadout):
        self.grid = self.generate_map_grid(map_loadout)

    def generate_map_grid(self, map_loadout:MapLoadout):
        pass
        


