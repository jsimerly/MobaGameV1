from hex import Hex, Layout, Orientation, Point, layout_pointy

class GameMap:
    def __init__(self, map_loadout):
        self.size = map_loadout['size']
        self.shape = map_loadout['shape']
        self.hexes = []
