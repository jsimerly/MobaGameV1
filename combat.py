import random
from hex import Layout, orientation_pointy, Point
from typing import Callable

hex_size = (30, 30)
origin = Point(800//2, 800//2)
layout = Layout(orientation=orientation_pointy, size=hex_size, origin=origin)

class AttackComponent:
    def __init__(
        self,
        damage:int,
    ):
        self.damage = damage
    
    def get_damage_done(self, damage:int=None):
        if damage is None:
            damage = self.damage
        

        # May skew this based on player psych findings
        mu = (damage[1] + damage[0])//4
        sigma = (damage[1] - damage[0])//4
        damage = int(random.gauss(mu, sigma)//1)
        return damage

    def attack(self, damage:int, target):
        if target.health_component:
            damage_done = self.get_damage_done(damage)
            target.take_damage(damage_done)
        else:
            raise ValueError(f'{target} does not haev a health component.')

class HealthComponent:
    def __init__(self, health):
        self.health = health
        self.alive = True

    def take_damage(self, damage):
        if self.alive:
            self.health -= damage
            if self.health <= 0:
                self.die()

    def die(self, death_handler:Callable=None):
        if death_handler is not None:
            death_handler()

        self.alive = False



        
        
