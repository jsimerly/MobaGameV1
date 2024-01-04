from typing import Dict, Type
from abilities.status_effects import StatusEffect, Slow
from component import Component

class StatusEffectComponent(Component):
    def __init__(self):
        self.active_effects: Dict[Type[StatusEffect], int] = {}

    def apply_effect(self, effect: StatusEffect):
        self.active_effects[type(effect)] = effect.duration

    def update(self):
        expired_effects = []
        for effect_type, duration in self.active_effects.items():
            if duration > 0:
                self.active_effects[effect_type] -= 1
            if self.active_effects[effect_type] == 0:
                expired_effects.append(effect_type)

        for effect in expired_effects:
            self.remove_effect(effect)

    def remove_effect(self, effect_type: Type[StatusEffect]):
        if effect_type in self.active_effects:
            del self.active_effects[effect_type]

    def is_affected_by(self, effect_type: Type[StatusEffect]) -> bool:
        return effect_type in self.active_effects
            

#Example
if __name__ == '__main__':
    status_comp = StatusEffectComponent()
    status_comp.apply_effect(Slow(duration=3))
