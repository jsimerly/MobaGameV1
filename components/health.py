from typing import List
from buffs import BuffComponent
from abilities.buffs_debuffs import HealingBuff, DamageTakenBuff, ShieldBuff
from component import Component

class HealthComponent(Component):
    def __init__(self, health:int):
        self.max_health = health
        self.health = health
        self.alive = True

        self.buff_component: BuffComponent = None

    def set_buff_component(self, buff_component:BuffComponent):
        self.buff_component = buff_component

    def take_damage(self, amount: int) -> int:
        buffs: List[DamageTakenBuff] = []
        shields: List[ShieldBuff] = []
        for buff in self.buff_component.active_buffs:
            if isinstance(buff, DamageTakenBuff):
                buffs.append(buff)

            if isinstance(buff, ShieldBuff):
                shields.append(buff)

        modifier = 1.0
        for buff in buffs:
            modifier *= buff.modifier

        damage = amount * modifier
        
        for shield in shields:
            damage = damage - shield.shield_size
            if damage < 0:
                shield.shield_size = shield.shield_size + damage
                return 0
            self.buff_component.remove_buff(shield)
        
        self.health -= damage


    def heal(self, amount:int) -> int:
        buffs = [buff for buff in self.buff_component if isinstance(buff, HealingBuff)]

        modifier = 1.0
        for buff in buffs:
            modifier *= buff.modifier
        
        heal = amount * modifier

        self.health += heal
        return heal
    
    def increase_max_health(self, amount:int) -> int:
        self.max_health += amount
        self.health += amount
        return self.max_health



if __name__ == '__main__':
    buff_component = BuffComponent()
    health_component = HealthComponent(health=1000)
    health_component.set_buff_component(buff_component)

    empowered_flame = DamageTakenBuff(
        modifier=1.2,
        name='Empowered Flame',
        duration=1
    )

    buff_component.add_buff(empowered_flame)
    buff_component.add_buff(ShieldBuff(shield_size=20, name='shield'))
    health_component.take_damage(50) # 50 * 1.2 - 20 = 40 
    health_component.heal(20) # 40 + 20 = 60

