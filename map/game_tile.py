from hex import Hex
from components import MapInteractionComponent
from typing import Callable, Optional
from tile_effect import *

class GameTile(Hex):
    def __init__(self, 
        q:int, r:int,
        surface_color: (int, int, int),
        is_passable:bool, 
        can_end_on:bool, 
        blocks_vision:bool, 
        hides_occupants: bool,
        is_slowing:bool,
        walkthrough_effect: Optional[None],
    ):
        self.color = surface_color
        visual_effects = []

        self.occupants = []
        self.tile_effects = {
            OnEnterTileEffect: [],
            OnExitTileEffect: [],
            OnEndOfTurnTileEffect: [],
        }
        
        #Map Component Aggregate of occupiers.
        self.default_is_passable = is_passable
        self.default_can_end_on = can_end_on
        self.default_blocks_vision = blocks_vision
        self.default_hides_occupants = hides_occupants
        self.default_is_slowing = is_slowing
        self.default_walkthrough_effect = walkthrough_effect
        
        self.is_passable = is_passable
        self.can_end_on = can_end_on
        self.blocks_vision = blocks_vision
        self.hides_occupants = hides_occupants
        self.is_slowing = is_slowing
        self.walkthrough_effect = walkthrough_effect


    def reset_default_map_interaction(self, property):
        property_map = {
            self.is_passable : self.default_is_passable,
            self.can_end_on : self.default_can_end_on,
            self.blocks_vision : self.default_blocks_vision,
            self.hides_occupants : self.default_hides_occupants,
            self.is_slowing : self.default_is_slowing,
            self.walkthrough_effect : self.default_walkthrough_effect,
        }

        default_prop = property_map[property]
        property = default_prop
        return default_prop
            
    def reset_default_map_interactions_all(self):
        self.is_passable = self.default_is_passable
        self.can_end_on = self.default_can_end_on
        self.blocks_vision = self.default_blocks_vision
        self.hides_occupants = self.default_hides_occupants
        self.is_slowing = self.default_is_slowing
        self.walkthrough_effect = self.default_walkthrough_effect

    def add_effect(self, effect:TileEffect):
        self.resolve_effects(effect)
        self.tile_effects[type(effect)].append(effect)        

    def resolve_effects(self, new_effect: TileEffect):
        for effect in self.tile_effects:
            if not new_effect.can_override(effect):
                effect.apply_effect(self)
    
    def remove_effect(self, effect:TileEffect):
        pass

