from map.map_objects.base import StructureBase
from combat import HealthComponent, AttackComponent


class MainBase(StructureBase):
    def __init__(self, 
        sprite, 
        color:(int,int,int), #Will be team color eventually
        radius:int=2,
        health:int=1000,
        teleport_radius:int=3,
    ):
        super().__init__(
            'Main Base', 
            is_passible=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )
        self.color = color
        self.radius = radius
        self.health_component = HealthComponent(1000)
        self.teleport_radius = teleport_radius

    def teleport(self):
        #teleport
        pass

    def destroy(self):
        super().destroy()
        #End the game when this happens

class Teleporter(StructureBase):
    def __init__(self, 
        sprite, 
        color:(int,int,int), 
        health:int=500,
        teleport_radius:int=2

    ):
        super().__init__(
            'Teleporter', 
            is_passible=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )
        self.color = color
        self.health_component = HealthComponent(health)
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
        health:int=500,
        damage:int=100,
    ):
        super().__init__(
            'Turret', 
            is_passible=False, 
            is_los=False, 
            is_concealing=False, 
            sprite=sprite
        )

        self.health_component = HealthComponent(health)
        self.attack_component = AttackComponent(damage)




    

    


