from map.map_objects.base import EnviromentBase, GameTile, MapEdge
from map.base import GameTile

class Tree(EnviromentBase):
    def __init__(self, sprite):
        super().__init__(
            name='Tree', 
            is_passible=False,
            is_los=False, 
            is_concealing=False,
            sprite=sprite,
        )

class Rock(EnviromentBase):
    def __init__(self, sprite):
        super().__init__(
            name='Rock', 
            is_passible=True,
            is_los=True, 
            is_concealing=False,
            sprite=sprite,
        )

class Water(EnviromentBase):
    def __init__(self, sprite):
        super().__init__(
            name='Water', 
            is_passible=False,
            is_los=True, 
            is_concealing=False,
            sprite=sprite,
        )

class Brush(EnviromentBase):
    def __init__(self, sprite):
        super().__init__(
            name='Brush', 
            is_passible=False,
            is_los=False, 
            is_concealing=False,
            sprite=sprite,
        )

class RoughTerrain(EnviromentBase):
    def __init__(self, sprite, movement_cost):
        super().__init__(
            name='Rough Terrain', 
            is_passible=True,
            is_los=False, 
            is_concealing=False,
            sprite=sprite,
        )
        self.movement_cost = movement_cost


#Edges 
class Wall(MapEdge):
    def __init__(self, 
        hex1: GameTile, 
        hex2: GameTile, 
        sprite
    ):
        super().__init__(
            hex1, 
            hex2, 
            is_passable=False, 
            is_directional=False, 
            is_los=True, 
            sprite=sprite
        )

class Fence(MapEdge):
    def __init__(self, 
        hex1: GameTile, 
        hex2: GameTile, 
        sprite
    ):
        super().__init__(
            hex1, 
            hex2, 
            is_passable=False, 
            is_directional=False, 
            is_los=True, 
            sprite=sprite
        )

class Cliff(MapEdge):
    def __init__(self, 
        hex1: GameTile, 
        hex2: GameTile, 
        sprite
    ):
        super().__init__(
            hex1, 
            hex2, 
            is_passable=True, 
            is_directional=True, 
            is_los=True, 
            sprite=sprite
        )
## Could add more thing directional such as one-way doors or mirrors

