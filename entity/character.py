from abilities.ability import Ability
from abilities.slots import *
from components.sprite import SpriteComponent
from entity.entity import Entity
from components import *
from typing import List

class Character(Entity):
    def __init__(self,
        name:str,
        #component params
        health:int,
        movement_cost:int,
        level_increments: List[int],
        vision_range:int,
        resource_comp:ResourceComponent,
        #abilities
        basic_ability: Ability,
        ability_1: Ability,
        ability_2: Ability,
        ability_super: Ability,
        #sprite
        sprite_component:SpriteComponent,
    ):
        super().__init__()
        self.name=name
        #Resource
        self.set_resource_component(resource_comp)
        
        #Leveling
        level_comp = LevelingComponent(pp_increments=level_increments)
        self.set_leveling_component(level_comp)

        #Buff
        buff_comp = BuffComponent()
        self.set_buff_component(buff_comp)

        #Status Effect
        status_comp = StatusEffectComponent()
        self.set_status_effect_component(status_comp)

        #Aura
        aura_comp = AuraComponent()
        self.set_aura_component(aura_comp)

        #Health
        health_comp = HealthComponent(health)
        health_comp.set_buff_component(self.buff_component)
        self.set_health_component(health_comp)

        #Movement
        move_comp = MovementComponent(movement_cost=movement_cost)
        move_comp.set_status_effect_component(self.status_effect_component)
        self.set_movement_component(move_comp)

        #Vision
        vision_comp = VisionComponent(vision_range=vision_range)
        vision_comp.set_status_effect_component(self.status_effect_component)
        self.set_vision_component(vision_comp)

        #Ability
        ability_comp = AbilityComponent()
        ability_comp.set_all_components(
            health_component=self.health_component,
            resource_component=self.resource_component,
            level_component=self.leveling_component,
            buff_component=self.buff_component,
            status_effect_component=self.status_effect_component,
            aura_component=self.aura_component,
            movement_component=self.movement_component
        )
        ability_comp.add_ability(AbilitySlot_Basic, basic_ability)
        ability_comp.add_ability(AbilitySlot_1, ability_1)
        ability_comp.add_ability(AbilitySlot_2, ability_2)
        ability_comp.add_ability(AbilitySlot_Super, ability_super)
        self.set_ability_component(ability_comp)

        #Map Interaction
        map_interaction_comp = MapInteractionComponent(
            is_passable=True, can_end_on=False, blocks_vision=False, hides_occupants=False, is_hidden=False, walkthrough_effects=False, is_slowing=False
        )
        self.set_map_interaction_component(map_interaction_comp)

        #Sprite
        self.set_sprite_component(sprite_component)

        self.queued_movement_to = None
        self.queued_abilities = []

    def set_aura_component(self, aura_component: AuraComponent):
        self.aura_component = aura_component

    def set_buff_component(self, buff_component: BuffComponent):
        self.buff_component = buff_component

    def set_status_effect_component(self, status_effect_component: StatusEffectComponent):
        self.status_effect_component = status_effect_component

    def set_ability_component(self, ability_component: AbilityComponent):
        self.ability_component = ability_component

    def set_leveling_component(self, leveling_component: LevelingComponent):
        self.leveling_component = leveling_component

    def set_movement_component(self, movement_component: MovementComponent):
        self.movement_component = movement_component

    def set_resource_component(self, resource_component: ResourceComponent):
        self.resource_component = resource_component

    def set_sprite_component(self, sprite_component: SpriteComponent):
        self.sprite_component = sprite_component

    def process_queue(self):
        pass
        #this will probably entail stacking up different abilities and their effects into the proper phase. As the user will only be queueing the ability then once we hit processing then we need to split it out into movement, precombat,
    
    def turn_processing(self):
        self.process_queue()
        

    def start_of_queue_phase(self):
        pass

    def movement_processing(self):
        pass
    
    def pre_combat_processing(self):
        pass
    
    def combat_processing(self):
        pass
        
    def animate_turn(self):
        pass

    def end_of_turn(self):
        pass

