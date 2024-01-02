from hex import Hex, Orientation, Layout, orientation_pointy, orientation_flat
from events import OnEnterEvent, OnExitEvent, OnSotEvent, OnEotEvent, MovementEventBase
from typing import List, Dict, Type, Callable
from map.map_objects.base import MapEdge

EventHandler = Callable[[MovementEventBase], None]

class TileObserver:
    def on_ability(self, ability):
        pass


class GameTile(Hex):
    def __init__(self, q: int, r: int, 
            surface_color: (int, int, int), #RGB
            visual_effects = [],

            is_passable:bool = True,
            is_los:bool = True,
            is_hidden:bool= False,

            event_handlers: Dict[Type[MovementEventBase], List[EventHandler]] = {
                OnEnterEvent: [],
                OnExitEvent : [],
                OnSotEvent: [],
                OnEotEvent : []
            }
        ):
            super().__init__(q, r)
            self.surface_color = surface_color
            self.visual_effects = visual_effects

            self.is_passable = is_passable
            self.is_los = is_los
            self.is_hidden = is_hidden
            self.event_handlers = event_handlers
            self.observers = []

    def register_event_handler(self, event_name, handler):
        if event_name in self.event_handlers:
            self.event_handlers[event_name].append(handler)
        else:
            raise ValueError(f"No event named {event_name}")
        
    def trigger_event(self, event_name, *args, **kwargs):
        for handler in self.event_handlers.get(event_name, []):
             handler(**args, **kwargs)


    def register_observer(self, observer: TileObserver):
        self.observers.append(observer)

    def unregister_observer(self, observer: TileObserver):
        self.observers.remove(observer)

class GameMap:
    def __init__(self, 
            map_loadout: dict,
            default_color: (int, int, int), #RGB
        ):
        self.size = map_loadout['size']
        self.hex_layout = map_loadout['layout']
        self.grid = self.generate_map_grid(map_loadout['map_layout'])
        self.edges = map_loadout['edges']

        self.default_color = default_color

    def generate_map_grid(map_layout) -> Dict[(int, int), GameTile]:
        pass

    def generate_map_edges(map_layout) -> Dict[(Hex, Hex), MapEdge]:
        pass


