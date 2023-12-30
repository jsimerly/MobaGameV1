

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
