from components.health import HealthComponent
from components.buffs import BuffComponent
from components.vision import VisionComponent
from components.sprite import  SpriteComponent
from components.map_interaction import MapInteractionComponent

class Entity:
    def __init__(self) -> None:
        self.axial_cord: (int, int)= None
        self.health_component: HealthComponent = None
        self.buff_component: BuffComponent = None
        self.vision_component: VisionComponent = None
        self.sprite_component: SpriteComponent = None
        self.map_interaction_component: MapInteractionComponent = None

    def set_axial_cord(self, axial_cord: (int, int)):
        self.axial_cord = axial_cord

    def set_health_component(self, health_component: HealthComponent):
        self.health_component = health_component
    
    def set_buff_component(self, buff_component: BuffComponent):
        self.buff_component = buff_component

    def set_vision_component(self, vision_component: VisionComponent):
        self.vision_component = vision_component

    def set_sprite_component(self, sprite_component: SpriteComponent):
        self.sprite_component = sprite_component

    def set_map_interaction_component(self, interaction_component: MapInteractionComponent):
        self.map_interaction_component = interaction_component
