from components import AbilityComponent, TeleportComponent, AuraComponent, MapInteractionComponent
from entity.entity import Entity

class Structure(Entity):
    def __init__(self, map_interaction_component: MapInteractionComponent):
        super().__init__()
        self.ability_component: AbilityComponent = None
        self.teleport_component: TeleportComponent = None
        self.aura_component: AuraComponent = None
        self.set_map_interaction_component(map_interaction_component)

    def set_ability_component(self, ability_component: AbilityComponent):
        self.ability_component = ability_component

    def set_teleport_component(self, teleport_component: TeleportComponent):
        self.teleport_component = teleport_component

    def set_aura_component(self, aura_component: AuraComponent):
        self.aura_component = aura_component


