import pygame as pg
import math
from map.map import *
from settings import *
pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BGCOLOR)

map_1 = {
    IndestructableTree: [
        {'axial_cord': (0,0)},
    ],
    DestructableTree: [],
    Water: [],
    Brush: [],

    MainBase: [{'axial_cord': (4,4)},],
    Turret: [],
}

game_map = HexMap(screen=screen, map_structures=map_1)

is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False


    pg.display.flip()


pg.quit()