from hex import Hex, Orientation, Layout, orientation_pointy, orientation_flat
from events import OnEnterEvent, OnExitEvent, OnSotEvent, OnEotEvent, MovementEventBase
from typing import List, Dict, Type, Callable

EventHandler = Callable[[MovementEventBase], None]

class GameTile(Hex):
    def __init__(self, q: int, r: int, 
            surface_color: (int, int, int), #RGB
            terrian_type,
            sprites = None,
            character = None,
            structure = None, 

            passable:bool = True,
            los:bool = False,

            event_handlers: Dict[Type[MovementEventBase], List[EventHandler]] = {
                OnEnterEvent: [],
                OnExitEvent : [],
                OnSotEvent: [],
                OnEotEvent : []
            }
        ):
            super().__init__(q, r)
            self.surface_color = surface_color
            self.terrian_type = terrian_type
            self.sprites = sprites
            self.character = character
            self.structure = structure

            self.passable = passable
            self.los = los
            self.event_handlers = event_handlers


    def register_event_handler(self, event_name, handler):
        if event_name in self.event_handlers:
            self.event_handlers[event_name].append(handler)
        else:
            raise ValueError(f"No event named {event_name}")
        
    def trigger_event(self, event_name, *args, **kwargs):
        for handler in self.event_handlers.get(event_name, []):
             handler(**args, **kwargs)


class GameMap:
    def __init__(self, 
            map_loadout: dict,
            default_color: (int, int, int), #RGB
        ):
        self.size = map_loadout['size']
        self.hex_layout = map_loadout['layout']
        self.grid = self.generate_map_grid(map_loadout['map_layout'])

        self.default_color = default_color

    def generate_map_grid(map_layout) -> List[GameTile]:
        pass
