from hex import Hex, Layout
from typing import Callable, Optional
from entity.entity import Entity
from map.tiles.tile_effect import *
from settings import LIGHT_GREY
import pygame as pg

class GameTile(Hex):
    def __init__(self, 
        q:int, r:int,
        layout: Layout,
        screen,

        surface_color: (int, int, int),
        is_passable:bool, 
        can_end_on:bool, 
        can_pierce: bool,
        blocks_vision:bool, 
        hides_occupants: bool,
        is_slowing:bool,
        walkthrough_effects: Optional[None] = [],

    ):
        super().__init__(q, r)
        self.layout = layout

        self.color = surface_color
        visual_effects = []

        self.occupants:Entity = []
        self.tile_effects = {
            OnEnterTileEffect: [],
            OnExitTileEffect: [],
            OnEndOfTurnTileEffect: [],
        }
        
        #Map Component Aggregate of occupiers.
        self.default_is_passable = is_passable
        self.default_can_pierce = can_pierce
        self.default_can_end_on = can_end_on
        self.default_blocks_vision = blocks_vision
        self.default_hides_occupants = hides_occupants
        self.default_is_slowing = is_slowing
        self.default_walkthrough_effects = walkthrough_effects
        
        self.is_passable = is_passable
        self.can_pierce = can_pierce
        self.can_end_on = can_end_on
        self.blocks_vision = blocks_vision
        self.hides_occupants = hides_occupants
        self.is_slowing = is_slowing
        self.walkthrough_effects = walkthrough_effects


    def reset_default_map_interaction(self, property):
        property_map = {
            self.is_passable : self.default_is_passable,
            self.can_pierce : self.default_can_pierce,
            self.can_end_on : self.default_can_end_on,
            self.blocks_vision : self.default_blocks_vision,
            self.hides_occupants : self.default_hides_occupants,
            self.is_slowing : self.default_is_slowing,
            self.walkthrough_effect : self.default_walkthrough_effects,
        }

        default_prop = property_map[property]
        property = default_prop
        return default_prop
            
    def reset_default_map_interactions_all(self):
        self.is_passable = self.default_is_passable
        self.can_pierce = self.can_pierce
        self.can_end_on = self.default_can_end_on
        self.blocks_vision = self.default_blocks_vision
        self.hides_occupants = self.default_hides_occupants
        self.is_slowing = self.default_is_slowing
        self.walkthrough_effect = self.default_walkthrough_effects

    def add_effect(self, effect:TileEffect):
        self.resolve_effects(effect)
        effect_type = type(effect)
        if effect_type in self.tile_effects:
            self.tile_effects[type(effect)].append(effect)
            return effect

        print('Unrecognized effect type.')        

    def resolve_effects(self, new_effect: TileEffect):
        for effect in self.tile_effects:
            if not new_effect.can_override(effect):
                effect.apply_effect(self)
    
    def remove_effect(self, effect:TileEffect):
        effect_type = type(effect)
        if effect_type in self.tile_effects:
            if effect in self.tile_effects[effect_type]:
                self.tile_effects[effect_type].remove(effect)
            else:
                print(f"Effect not found in {effect_type}")
        else:
            print(f"Unrecognized effect type: {effect_type}")

        # Reapply remaining effects
        self._reapplay_effects()

    def _reapplay_effects(self):
        temp_effects = {effect_type: effects.copy() for effect_type, effects in self.tile_effects.items()}
        for effect_list in self.tile_effects.values():
            effect_list.clear()

        for effect_type, effects in temp_effects.items():
            for effect in effects:
                self.add_effect(effect)  

    
    def draw(self, screen):
        point = self.layout.hex_to_pixel(self)
        verticies = self.layout.get_hex_verticies(point)
        pg.draw.polygon(screen, self.color, verticies)
        pg.draw.polygon(screen, LIGHT_GREY, verticies, 2)

