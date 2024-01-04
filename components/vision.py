from map.base import GameMap, GameTile
from status_effects import StatusEffectComponent
from abilities.status_effects import Blind, Blur
from typing import List
from component import Component

class VisionComponent(Component):
    def __init__(self, vision_range:int):
        self.vision_range = vision_range
        self.status_effect_component:StatusEffectComponent = None

    def set_status_effect_component(self, status_effect_component:StatusEffectComponent):
        self.status_effect_component = status_effect_component    

    def check_cannot_see(self) -> bool:
        if self.status_effect_component == None:
            return True
        return self.status_effect_component.is_affected_by(Blind)
    
    def check_for_blur(self) -> bool:
        if self.status_effect_component == None:
            return None
        return self.status_effect_component.is_affected_by(Blur)


    #Need to think about implementing what they previously saw and building before you lost vision
    def is_in_los(self, entity, game_map:GameMap) -> List[GameTile]:
        if self.check_cannot_see():
            return []
        #implement algo using the line function https://www.redblobgames.com/grids/hexagons/
