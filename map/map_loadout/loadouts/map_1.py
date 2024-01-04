from map.map_loadout.map_loadout import MapLoadout
from hex import Layout, orientation_pointy, Point
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

orientation=orientation_pointy
size = Point(30, 30)
origin = Point(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

layout = Layout(
    orientation=orientation,
    size=size,
    origin=origin,
)
shape=layout.hexagon
shape_params = {
    'radius' : 9,
}

special_tiles = {}

map_1 = MapLoadout(
    layout=layout,
    shape=shape,
    shape_params=shape_params,
    special_tiles=special_tiles
)