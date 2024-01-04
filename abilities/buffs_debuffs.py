from __future__ import annotations
from abc import ABC
from typing import Callable

class Buff(ABC):
    def __init__(self, name: str, is_debuff: bool = False, is_stacking: bool = False, max_stacks: int = None, max_stack_effect: Callable = None, affected_abilities=None, duration: int = 1):
        self.name = name
        self.is_debuff = is_debuff
        self.affected_abilities = affected_abilities

        self.is_stacking = is_stacking
        self.stacks = 1
        self.max_stacks = max_stacks
        self.max_stack_effect = max_stack_effect
        self.start_duration = duration
        self.duration = duration

    def does_applies_to(self, ability):
        if self.affected_abilities:
            return ability in self.affected_abilities
        return True
    
    def add_stack(self, count:int=1) -> int:
        if not self.is_stacking:
            return self.stacks
        
        new_stacks = self.stacks + count
        if new_stacks > self.max_stacks:
            new_stacks = self.max_stacks
            self.max_stacks_effect()

        self.stacks = new_stacks
        return self.stacks
    
    def remove_stack(self, count:int=1) -> int:
        new_stacks = self.stacks - count
        self.stacks = new_stacks
        return self.stacks
    
    
class DamageBuff(Buff):
    def __init__(self, modifier, name, is_debuff=False, is_stacking=False, max_stacks=None, max_stack_effect=None, affected_abilities=None, duration=1):
        super().__init__(name, is_debuff, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration)
        self.modifier = modifier


class DamageTakenBuff(Buff):
    def __init__(self, modifier, name, is_debuff=False, is_stacking=False, max_stacks=None, max_stack_effect=None, affected_abilities=None, duration=1):
        super().__init__(name, is_debuff, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration)
        self.modifier = modifier

class HealingBuff(Buff):
    def __init__(self, modifier, name, is_debuff=False, is_stacking=False, max_stacks=None, max_stack_effect=None, affected_abilities=None, duration=1):
        super().__init__(name, is_debuff, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration)
        self.modifier = modifier

class ShieldBuff(Buff):
    def __init__(self, shield_size, name, is_debuff=False, is_stacking=False, max_stacks=None, max_stack_effect=None, affected_abilities=None, duration=1):
        super().__init__(name, is_debuff, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration)
        self.shield_size = shield_size

class HealingOverTime(Buff):
    def __init__(self, name: str, is_stacking: bool = False, max_stacks: int = None, max_stack_effect = None, affected_abilities=None, duration: int = 1):
        super().__init__(name, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration,  is_debuff=False)

class DamageOverTime(Buff):
    def __init__(self, name: str, damage:int, is_stacking: bool = False, max_stacks: int = None, max_stack_effect = None, affected_abilities=None, duration: int = 1):
        super().__init__(name, is_stacking, max_stacks, max_stack_effect, affected_abilities, duration, is_debuff=True)

        self.damage = damage

    def apply_damage(self, entity: Entity):
        entity.health_component.take_damage(self.damage)

if __name__ == '__main__':
    empowered_flame = DamageBuff(
        modifier=1.2,
        name='Empowered Flame',
        duration=1
    )
    lunar_guidance = DamageBuff(
        modifier=2,
        name='Empower',
        is_stacking=False
    )
    vulnerability_debuff = DamageTakenBuff(
        modifier=1.3, 
        name="Vulnerability",
        is_debuff=True,
        is_stacking=False,
        affected_abilities=None  # Affects all abilities
    )
    healing_aura = HealingBuff(
        modifier=1.25,
        name="Healing Aura",
        is_debuff=False,
        is_stacking=False,
        affected_abilities=["Heal", "Regeneration"]
    )



