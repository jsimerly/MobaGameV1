from __future__ import annotations
from .component import Component
from team.team import Team
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entity.entity import Entity

class TeamComponent(Component):
    def __init__(self, team:Team):
        self.team = team

    def is_target_same_team(self, entity:Entity):
        return entity.team_component == self.team