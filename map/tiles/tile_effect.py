from __future__ import annotations
from map.tiles.game_tile import GameTile
from entity.entity import Entity

class TileEffect:
    def __init__(self, name:str, duration:int, override_priority:int):
        self.name = name
        self.duration = duration
        self.override_priority = override_priority

    def apply_effect(self, game_tile: GameTile):
        pass

    def undo_effect(self, game_tile: GameTile):
        pass

    def trigger_effect(self, entity:Entity):
        pass

    #if they're the same number the effect added later will win out. this will happen by being looped over the tile effects later.
    def can_override(self, other_effect: TileEffect):
        return self.override_priority > other_effect.override_priority

class OnEnterTileEffect(TileEffect):
    def __init__(self, name: str, duration:int, override_priority: int):
        super().__init__(name, duration, override_priority)

class OnExitTileEffect(TileEffect):
    def __init__(self, name: str, duration:int, override_priority: int):
        super().__init__(name, duration, override_priority)

class OnEndOfTurnTileEffect(TileEffect):
    def __init__(self, name: str, duration:int, override_priority: int):
        super().__init__(name, duration, override_priority)