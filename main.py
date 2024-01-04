import pygame as pg
from settings import *
from hex import *
from map.game_map import GameMap
from map.map_loadout.loadouts.map_1 import map_1



pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
screen.fill(BGCOLOR)

# game_map = HexMap(screen=screen, map_structures=map_1, power_sources=power_sources)

game_map = GameMap(map_loadout=map_1, screen=screen)

is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    game_map.draw()

    pg.display.flip()


pg.quit()