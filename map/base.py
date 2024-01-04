from hex import Hex, Orientation, Layout, orientation_pointy, orientation_flat
from typing import List, Dict,
from map.map_objects.base import MapEdge
from 


class TileObserver:
    def __init__(self):
        self.health_component = None
        self.modifiers = []
        
    def apply_effect(self, effect: TileEffect):
        effect.apply()

class GameTile(Hex):
    def __init__(self, q: int, r: int, 
            surface_color: (int, int, int), #RGB
            visual_effects = [],

            is_passable:bool = True,
            is_los:bool = True,
            is_hidden:bool= False,
        ):
            super().__init__(q, r)
            self.surface_color = surface_color
            self.visual_effects = visual_effects

            self.is_passable = is_passable
            self.is_los = is_los
            self.is_hidden = is_hidden

            self.pre_combat_effects = []
            self.combat_effects = []
            self.observers = []

    def register_pre_combat_effect(self, effect: TileEffect):
        self.pre_combat_effects.append(effect)
    
    def unregister_pre_combat_effect(self, effect: TileEffect):
        self.pre_combat_effects.remove(effect)

    def register_combat_effect(self, effect: TileEffect):
        self.combat_effects.append(effect)

    def register_combat_effect(self, effect: TileEffect):
        self.combat_effects.remove(effect)

    def register_observer(self, observer: TileObserver):
        self.observers.append(observer)

    def unregister_observer(self, observer: TileObserver):
        self.observers.remove(observer)

    def handle_end_of_turn(self):
        for observer in self.observers:
            for effect in self.effects:
                observer.apply_effect(effect)

class GameMap:
    def __init__(self, 
            map_loadout: dict,
            default_color: (int, int, int), #RGB
        ):
        self.size = map_loadout['size']
        self.hex_layout = map_loadout['layout']
        self.grid = self.generate_map_grid(map_loadout['map_layout'])
        self.edges = map_loadout['edges']

        self.default_color = default_color

    def generate_map_grid(map_layout) -> Dict[(int, int), GameTile]:
        pass

    def generate_map_edges(map_layout) -> Dict[(Hex, Hex), MapEdge]:
        pass


