from map.base import GameMap, GameTile
from status_effects import StatusEffectComponent
from abilities.status_effects import Slow, Root, Stun, Statis
from utils import PlayerError
from component import Component

class MovementComponent(Component):
    def __init__(self, movement_cost:int):
        self.movement_cost = movement_cost
        self.status_effects_component: StatusEffectComponent = None

    def set_status_effect_component(self, status_effect_component: StatusEffectComponent):
        self.status_effect_component = status_effect_component
    
    def check_cannot_move(self) -> bool:
        return not any[(
            self.status_effects_component.is_affected_by(Root),
            self.status_effects_component.is_affected_by(Stun),
            self.status_effects_component.is_affected_by(Statis),
        )]

    def move(self, entity, target_tile:GameTile, game_map:GameMap):
        if self.check_cannot_move():
            raise PlayerError("You cannot move because you're either rooted, stunned, or in stasis.")
        
        #implement breadth first search to include slows and edges and one way edges
        