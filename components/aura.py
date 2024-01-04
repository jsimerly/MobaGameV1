from component import Component
from typing import List

class AuraComponent(Component):
    def __init__(self, aura_range: int, effects): #this will gventually take AuraEffect which will be an ability type for characters. (each aura could have its own affect.)
        self.effects = effects  # List of effects the aura applies
        self.affected_entities = set()  # Entities currently affected by the aura

    def update(self, owner, game_map):
        # Called each game tick or when necessary to update the state of the aura
        # Find entities within aura_range of the owner and apply effects
        nearby_entities = self.find_nearby_entities(owner, game_map)
        self.apply_aura_effects(nearby_entities)

    def find_nearby_entities(self, owner, game_map):
        # Implement logic to find nearby entities within aura_range
        pass

    def apply_aura_effects(self, entities):
        # Apply or update effects on entities
        for entity in entities:
            if entity not in self.affected_entities:
                self.affected_entities.add(entity)
                for effect in self.effects:
                    effect.apply(entity)
            # Additional logic for continuous effects or updates

    def remove_aura_effects(self):
        # Remove effects from all entities if the aura is deactivated or the owner is destroyed
        for entity in self.affected_entities:
            for effect in self.effects:
                effect.remove(entity)
        self.affected_entities.clear()

