from map.map_objects.base import MapObject
from typing import Callable
from abilities.status_effects import Slow, Stun, Blind, Root
from components import AbilityComponent, HealthComponent, VisionComponent
from abilities.ability import Ability


class StructureBase(MapObject):
    def __init__(self,
        name:str,
        health:int,
        vision_range:int,
        basic_ability: Ability,

        #Map Obj 
        is_passable: bool, 
        is_los: bool, 
        is_concealing: bool,
        sprite,
    ):
        super().__init__(
            name, 
            is_passable, 
            is_los, 
            is_concealing, 
            sprite
        )

        self.vision_range = VisionComponent(vision_range)
        self.ability_component = AbilityComponent(basic_ability)
        self.health_component = HealthComponent(health)
        self.modifiers = []
        self.queued_abilities = []

    def add_modifier(self, modifier):
        if any([
            isinstance(modifier, Stun),
            isinstance(modifier, Slow),
            isinstance(modifier, Blind),
            isinstance(modifier, Root),
        ]):
            return
        
    def destroy(self):
        pass
        

class MainBase(StructureBase):
    def __init__(self, 
        sprite, 
        color:(int,int,int), #Will be team color eventually
        radius:int=2,
        teleport_radius:int=3,
    ):
        super().__init__(
            'Main Base', 
            is_passable=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )
        self.color = color
        self.radius = radius
        self.teleport_radius = teleport_radius

    def teleport(self):
        pass
    
class Teleporter(StructureBase):
    def __init__(self, 
        sprite, 
        color:(int,int,int), 
        health:int=500,
        teleport_radius:int=2
    ):
        super().__init__(
            'Teleporter', 
            is_passable=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )
        self.color = color
        self.teleport_radius = teleport_radius

class Teleporter(StructureBase):
    def __init__(self, 
        sprite, 
        color:(int,int,int), 
        health:int=500,
        teleport_radius:int=2

    ):
        super().__init__(
            'Teleporter', 
            is_passable=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )
        self.color = color
        self.teleport_radius = teleport_radius

    def teleport(self):
        #teleport
        pass

    def destroy(self):
        super().destroy()
        #increase the spawn timers +1

class Turret(StructureBase):
    def __init__(self, 
        sprite,
    ):
        super().__init__(
            'Turret', 
            is_passable=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )


class PowerCrystal(StructureBase):
    def __init__(self, sprite):
        super().__init__(
            name='Power Crystal', 
            is_passable=False, 
            is_los=True, 
            is_concealing=False, 
            sprite=sprite,
        )

class PowerShards(StructureBase):
    def __init__(self, sprite):
        super().__init__(
            name='Power Shards', 
            is_passable=True, 
            is_los=True, 
            is_concealing=False, 
            sprite=sprite,
        )
    
