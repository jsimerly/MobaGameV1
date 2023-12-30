from hex import Hex, Orientation, Layout, orientation_pointy, orientation_flat
from events import OnEnterEvent, OnExitEvent, OnSotEvent, OnEotEvent, MovementEventBase
from game_objects import EnviromentObject, Objective
from typing import List, Dict, Type, Callable

EventHandler = Callable[[MovementEventBase], None]

class GameEdge:
    def __init__(self, 
            hex1: Hex, #This is the parent Hex, the hex that will be passible down but not up
            hex2: Hex, #Child Hex
            is_passable: bool, 
            is_directional: bool, 
            is_los: bool, 
            color: (int, int, int)
        ):
        self.hex1 = hex1
        self.hex2 = hex2
        self.is_passable = is_passable
        self.is_directional = is_directional
        self.is_los = is_los
        self.color = color

    def check_passability(self, to_hex):
        if self.is_directional and to_hex == self.hex1:
            return False
        return self.is_passable
    
class GameTile(Hex):
    def __init__(self, q: int, r: int, 
            surface_color: (int, int, int), #RGB
            visual_effects = [],

            character = None,
            enviroment_obj: List[EnviromentObject] = [],
            objectives: List[Objective] = [],

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

            self.character = character
            self.enviroment_obj = enviroment_obj
            self.objective = objectives

            self.is_passable = is_passable
            self.is_los = is_los
            self.is_hidden = is_hidden
            self.event_handlers = event_handlers

    def add_object(self, game_object:GameObject):
        self.game_objects.append(game_object)
    
    def remove_object(self, game_object: GameObject):
        self.game_objects.remove(game_object)


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
        self.edges = map_loadout['edges']

        self.default_color = default_color

    def generate_map_grid(map_layout) -> Dict[(int, int), GameTile]:
        pass

    def generate_map_edges(map_layout) -> Dict[(Hex, Hex), GameEdge]:
        pass


