from abc import ABC
from entity_components import AbilityComponent, LevelingComponent, HealthComponent, MovementComponent, GameAbility, VisionComponent
from map.base import GameTile

class Entity(ABC):
    def __init__(self,
        name:str,
        health:int,
        vision_range:int,
        basic_ability: GameAbility,
        sprite,
        movement_cost:int=None,
    ):
        self.name = name
        self.sprite = sprite
        self.game_tile = None

        self.vision_range = VisionComponent(vision_range)
        self.leveling_component = LevelingComponent()
        self.ability_component = AbilityComponent(basic_ability)
        self.health_component = HealthComponent(health)
        self.movement_component = MovementComponent(movement_cost)

        self.modifiers = []

        self.queued_movements = []
        self.queued_abilities = []

    def queue_movement(self, game_tile: GameTile):
        movement_cost, movements = self.movement_component.find_path(game_tile)
        self.queued_movement = movements
        self.movement_spend += movement_cost

    def dequeue_movement(self):
        self.movement_spend = 0
        self.queued_movement = []

    def queue_ability(self, ability: GameAbility):
        self.queued_abilities.append(ability)

    def dequeue_ability(self, ability: GameAbility):
        self.queued_abilities.remove(ability)

    def set_game_tile(self, game_tile:GameTile):
        self.game_tile = game_tile

    def move(self, to_tile: GameTile) -> int:
        self.game_tile.unregister_observer(self)
        self.game_tile = to_tile
        to_tile.register_observer(self)
        #run animation

    def add_modifier(self, modifier):
        self.modifiers.append(modifier)

    def remove_modifier(self, modifier):
        self.modifiers.remove(modifier)

    def __str__(self) -> str:
        return self.name