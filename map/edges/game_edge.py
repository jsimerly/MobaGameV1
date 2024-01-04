from map.tiles.game_tile import GameTile

class MapEdge:
    def __init__(self, 
        hex1: GameTile, #This is the parent Hex, the hex that will be passable down but not up
        hex2: GameTile, #Child Hex
        is_passable: bool, 
        is_directional: bool, 
        is_los: bool, 
        sprite,
    ):
        self.hex1 = hex1
        self.hex2 = hex2
        self.is_passable = is_passable
        self.is_directional = is_directional
        self.is_los = is_los
        self.sprite = sprite

    def check_passability(self, to_hex):
        if self.is_directional and to_hex == self.hex1:
            return False
        return self.is_passable
    
