class IGameTurnBehavior:
    def perform_start_of_turn(self):
        pass

    def perform_end_of_turn(self):
        pass

    def perform_on_enter(self):
        pass

    def perform_on_exit(self):
        pass

class MovementEventBase:
    def __init__(self, entity, event):
        self.entity = entity
        self.event = event

    def trigger(self):
        self.event(self.entity)

class OnEnterEvent(MovementEventBase):
    pass

class OnExitEvent(MovementEventBase):
    pass

class OnEotEvent(MovementEventBase):
    pass

class OnSotEvent(MovementEventBase):
    pass
