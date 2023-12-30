import pygame as pg
import math
from combat import AttackComponent

class Mob:
    def __init__(self, health:int):  
        self.health = health
        self.is_in_combat = False
        self.turns_in_combat = 0

    def spawn(self):
        pass

    def despawn(self):
        pass

    def take_damage(self, damage:int):
        self.health = self.health - damage
        self.check_death()

    def check_death(self):
        if self.health <= 0:
            self.die
    
    def die(self):
        self.despawn()
        #reward

class Boss(Mob):
    def __init__(self, health: int, damage:(int,int), attack_speed):
        super().__init__(health)
        self.damage = damage
        self.attack_speed = attack_speed
        self.attack_component = AttackComponent()
        self.is_enraged = False

    def attack(self):
        self.attack_component.attack(damage=self.damage)

    def check_enrage(self):
        if self.turns_in_combat > 4:
            self.is_enraged = True
            self.damage = (self.damage[0]*2,self.damage[1]*2)

    def take_damage(self, damage: int):
        if self.is_enraged:
            damage = int(damage//1.5)
        return super().take_damage(damage)

class Monsters(Mob):
    def __init__(self, health: int, damage:(int,int)):
        super().__init__(health)
        self.damage = damage
        self.attack_component = AttackComponent()

    def attack(self):
        self.attack_component.attack(damage=self.damage)

    def check_enrage(self):
        if self.turns_in_combat > 4:
            self.is_enraged = True
            self.damage = (self.damage[0]*2,self.damage[1]*2)

        