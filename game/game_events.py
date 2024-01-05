from typing import Dict, List
from enum import Enum

class GameEvents(Enum):
    START_OF_GAME = 0
    START_OF_QUEUE_PHASE = 1
    PROCESS_MOVEMENT = 2
    PROCESS_PRE_COMBAT = 3
    PROCESS_COMBAT = 4
    ANIMATE = 5
    POST_DEATH_ACTIONS = 7
    END_OF_TURN = 8


class GameEventHandler:
    def __init__(self) -> None:
        self.subscribers: Dict[GameEvents, List] = {}

    def subscribe(self, event: GameEvents, fn):
        if event in self.subscribers:
            self.subscribers[event].append(fn)
        else:
            self.subscribers[event] = [fn]

    def unsubscribe(self, event: GameEvents, fn):
        if event in self.subscribers:
            self.subscribers[event].remove(fn)

    def post(self, event: GameEvents, data):
        if event in self.subscribers:
            for fn in self.subscribers[event]:
                fn(**data)