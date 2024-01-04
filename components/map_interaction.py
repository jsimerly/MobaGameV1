from typing import Callable, Optional, List

class MapInteractionComponent:
    def __init__(self, 
        is_passable:bool, 
        can_end_on:bool, 
        blocks_vision:bool, 
        is_hidden:bool,
        hides_occupants: bool,
        is_slowing:bool,
        walkthrough_effects: Optional[List[Callable]] = None,
    ):
        self.is_passable = is_passable
        self.can_end_on = can_end_on
        self.blocks_vision = blocks_vision
        self.is_hidden = is_hidden
        self.hides_occupants = hides_occupants
        self.is_slowing = is_slowing
        self.walkthrough_effects = walkthrough_effects or []

    def trigger_walkthrough_effects(self, entity):
        # Call each walkthrough effect when an entity walks through/over the component
        for effect in self.walkthrough_effects:
            effect(entity)