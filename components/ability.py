from __future__ import annotations
from .status_effects import StatusEffectComponent
from .buffs import BuffComponent
from .health import HealthComponent
from .movement import MovementComponent
from .aura import AuraComponent
from .leveling import LevelingComponent
from components.resources import ResourceComponent
from abilities.buffs_debuffs import DamageBuff, DamageTakenBuff, HealingBuff
from abilities.status_effects import Stun, Statis, Disabled
from abilities.ability import Ability
from abilities.slots import AbilitySlot
from utils import PlayerError
from typing import Dict
from .component import Component

class AbilityComponent(Component):
    def __init__(self):
        self.abilities: Dict[AbilitySlot, Ability] = {}

        self.health_component: HealthComponent = None
        self.resource_component: ResourceComponent = None
        self.level_component: LevelingComponent = None
        self.buff_component: BuffComponent = None
        self.status_effects_component: StatusEffectComponent = None
        self.aura_component: AuraComponent = None
        self.movement_componenet: MovementComponent = None

    def set_health_component(self, health_component: HealthComponent):
        self.health_component = health_component

    def set_resource_component(self, resource_component: ResourceComponent):
        self.resource_component = resource_component

    def set_level_component(self, level_component: ResourceComponent):
        self.level_component = level_component

    def set_buff_component(self, buff_component: BuffComponent):
        self.buff_component = buff_component

    def set_status_effect_component(self, status_effect_comp: StatusEffectComponent):
        self.status_effects_component = status_effect_comp

    def set_aura_component(self, aura_component: AuraComponent):
        self.aura_component = aura_component

    def set_movement_component(self, movement_component: MovementComponent):
        self.movement_componenet = movement_component

    def set_all_components(self,
        health_component: HealthComponent,
        resource_component: ResourceComponent,
        level_component: LevelingComponent,
        buff_component: BuffComponent,
        status_effect_component: StatusEffectComponent,
        aura_component: AuraComponent,
        movement_component: MovementComponent,
    ):
        self.set_health_component(health_component)
        self.set_resource_component(resource_component)
        self.set_level_component(level_component)
        self.set_buff_component(buff_component)
        self.set_status_effect_component(status_effect_component)
        self.set_aura_component(aura_component)
        self.set_movement_component(movement_component)

    def add_ability(self, ability_slot: AbilitySlot, ability):
        self.abilities[ability_slot] = ability

    def check_cannot_use_ability(self):
        return not any[(
            self.status_effects_component.is_affected_by(Disabled),
            self.status_effects_component.is_affected_by(Stun),
            self.status_effects_component.is_affected_by(Statis),
        )]

    def use_ability(self, ability_slot, game_tile:'GameTile'):
        if self.check_cannot_use_ability():
            raise PlayerError("You cannot use any abilities because you're either stunned, disabled, or in stasis.")
        
        ability = self.abilities[ability_slot]

        if ability:
            required_components = {}
            for req_comp in ability.required_components:
                comp_instance = self.get_component(req_comp)
                required_components[req_comp] = comp_instance

            ability.inject_components(required_components)
            ability.activate()


    def get_component(self, component_type: type(Component)) -> Component:
        component_map = {
            HealthComponent: self.health_component,
            ResourceComponent: self.resource_component,
            LevelingComponent: self.level_component,
            BuffComponent: self.buff_component,
            StatusEffectComponent: self.status_effects_component,
            AuraComponent: self.aura_component,
            MovementComponent: self.movement_componenet
        }
        return component_map[component_type]



