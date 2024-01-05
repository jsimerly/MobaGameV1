from hex import Hex, Layout
from typing import Callable, Optional, List
from entity.entity import Entity
from abilities.tile_effect import *
from settings import LIGHT_GREY
import pygame as pg
from game.game_object import GameObject

pg.font.init()

class GameTile(Hex, GameObject):
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

        has_coords:bool = False,
    ):
        super().__init__(q, r)
        self.layout = layout
        self.screen = screen
        self.is_selected = False

        self.has_coords = has_coords

        self.color = surface_color
        visual_effects = []

        self.occupants: List[Entity] = []
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

    def set_selected(self):
        self.is_selected = True
        self.draw() 

    def deselect(self):
        self.is_selected = False
        self.draw()
    
    def draw(self):
        point = self.layout.hex_to_pixel(self)
        verticies = self.layout.get_hex_verticies(point)
        pg.draw.polygon(self.screen, self.color, verticies)

        outline_size = 4 if self.is_selected else 1
        outline_color = (220,220,220) if self.is_selected else LIGHT_GREY
        pg.draw.polygon(self.screen, outline_color, verticies, outline_size)

        if self.has_coords:
            pg.font.init()
            font = pg.font.SysFont('Arial', 12)
            coord_text = f'{self.q}, {self.r}'
            text_surface = font.render(coord_text, True, (255, 255, 255))
            text_pos = (point[0] - text_surface.get_width() // 2, point[1] - text_surface.get_height() // 2)

            self.screen.blit(text_surface, text_pos)

