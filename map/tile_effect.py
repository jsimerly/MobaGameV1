from __future__ import annotations
from game_tile import GameTile

class TileEffect:
    def __init__(self, name:str, override_priority:int):
        self.name = name
        self.override_priority = override_priority

    def apply_effect(self, game_tile: GameTile):
        pass

    def undo_effect(self, game_tile: GameTile):
        pass

    #if they're the same number the effect added later will win out. this will happen by being looped over the tile effects later.
    def can_override(self, other_effect: TileEffect):
        return self.override_priority > other_effect.override_priority

class OnEnterTileEffect(TileEffect):
    def __init__(self, name: str, override_priority: int):
        super().__init__(name, override_priority)

class OnExitTileEffect(TileEffect):
    def __init__(self, name: str, override_priority: int):
        super().__init__(name, override_priority)

class OnEndOfTurnTileEffect(TileEffect):
    def __init__(self, name: str, override_priority: int):
        super().__init__(name, override_priority)