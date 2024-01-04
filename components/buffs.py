from abilities.buffs_debuffs import Buff, DamageBuff, DamageTakenBuff, HealingBuff, ShieldBuff
from typing import List
from component import Component

class BuffComponent(Component):
    def __init__(self):
        self.active_buffs: List[Buff] = []

    def add_buff(self, buff: Buff):
        for existing_buff in self.active_buffs:
            if isinstance(buff, existing_buff):
                if existing_buff.is_stacking:
                    existing_buff.add_stack()
                else:
                    existing_buff.duration = buff.start_duration
                return
            
        self.active_buffs.append(buff)

    def handle_end_of_turn(self):
        expired_buffs = []

        for buff in self.active_buffs:
            buff.duration -= 1
            if buff.duration <= 0:
                expired_buffs.append(buff)

        for buff in expired_buffs:
            self.remove_buff(buff)

    def remove_buff_stack(self, buff: Buff, count:int):
        for existing_buff in self.active_buffs:
            if isinstance(buff, existing_buff):
                new_count = existing_buff.remove_stack(count)

                if new_count <= 0:
                    self.remove_buff(buff)
    
    def remove_buff(self, buff: Buff):
        self.active_buffs = [existing_buff for existing_buff in self.active_buffs if existing_buff is not buff]

    def get_damage_modifier(self, ability) -> float:
        modifier = 1.0
        for buff in self.active_buffs:
            if isinstance(buff, DamageBuff) and buff.does_applies_to(ability):
                modifier *= buff.modifier
        return modifier
    
    def get_damage_taken_modifier(self, ability) -> float:
        modifier = 1.0
        for buff in self.active_buffs:
            if isinstance(buff, DamageTakenBuff) and buff.does_applies_to(ability):
                modifier *= buff.modifier
        return modifier
    
    def get_healing_modifier(self, ability) -> float:
        modifier = 1.0
        for buff in self.active_buffs:
            if isinstance(buff, HealingBuff) and buff.does_applies_to(ability):
                modifier *= buff.modifier
        return modifier
    
    def get_total_shield(self) -> int:
        total_shield = 0
        for buff in self.active_buffs:
            if isinstance(buff, ShieldBuff):
                total_shield += buff.shield_size
        return total_shield


if __name__ == '__main__':
    buff_component = BuffComponent()
    empowered_flame = DamageBuff(
        modifier=1.2,
        name='Empowered Flame',
        duration=1
    )

    buff_component.add_buff(empowered_flame)
    buff_component.add_buff(empowered_flame)
    buff_component.add_buff(empowered_flame)
    buff_component.remove_buff_stack(empowered_flame)
    buff_component.remove_buff(empowered_flame)
