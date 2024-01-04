import pygame as pg
from settings import *
from hex import *
from map.game_map import GameMap
from map.map_loadout.loadouts.map_1 import map_1
from characters.crud.crud import Crud
from game.brock_purdy import GameManager

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
screen.fill(BGCOLOR)

game_manager = GameManager()
game_map = GameMap(map_loadout=map_1, screen=screen)
game_manager.set_game_map(game_map)

crud = Crud()
crud.sprite_component.move_to_pixel((600,600))
game_manager.team_1.add_character(crud)
game_map.draw()

is_running = True

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    mouse_pos = pg.mouse.get_pos()
    mouse_pressed = pg.mouse.get_pressed()[0]
    hovered_hex = game_manager.get_hex_under_mouse(mouse_pos)
    print(hovered_hex)

    pg.display.flip()

pg.quit()