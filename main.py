import pygame as pg
import math
from map.map import *
from settings import *
from hex import *
pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
screen.fill(BGCOLOR)

team_1 = Team(color=(148, 49, 80))
team_2 = Team(color=(138, 166, 181))

# game_map = HexMap(screen=screen, map_structures=map_1, power_sources=power_sources)

orientation = layout_pointy
size = Point(30, 30)
origin = Point(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
layout = Layout(orientation=orientation, size=size, origin=origin)

hexes = layout.rectangle(6, 6)

is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False


    for hex in hexes:
        center = layout.hex_to_pixel(hex)
        points = layout.get_hex_verticies(center)
        verticies = [(v.x, v.y) for v in points]
        pygame.draw.polygon(screen, LIGHT_GREY, verticies, 2)

    pg.display.flip()


pg.quit()