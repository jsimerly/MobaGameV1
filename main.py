import pygame as pg
import math
from map.map import *
from settings import *
pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
screen.fill(BGCOLOR)

team_1 = Team(color=(148, 49, 80))
team_2 = Team(color=(138, 166, 181))

map_1 = {
    IndestructableRock: [
        {'axial_cord': (0, 0)}, {'axial_cord': (-1, 1)}, {'axial_cord': (0, -1)}, {'axial_cord': (1, -2)},{'axial_cord': (-1, 2)},
        {'axial_cord': (-8, 0)}, 
    ],
    DestructableTree: [
        #Right Jungle
        {'axial_cord': (8, 0)},  {'axial_cord': (8, -1)},  {'axial_cord': (7, 1)}, 
        {'axial_cord': (5, 2)},  {'axial_cord': (4, 2)},  {'axial_cord': (4, 1)}, 
        {'axial_cord': (5, -1)},  {'axial_cord': (6, -2)},  {'axial_cord': (7, -2)}, 
        {'axial_cord': (3, 1)},  {'axial_cord': (2, 2)},  {'axial_cord': (2, 1)}, 
        {'axial_cord': (4, -1)},  {'axial_cord': (3, -1)},  {'axial_cord': (4, -2)}, 

        {'axial_cord': (3, 5)}, {'axial_cord': (2, 5)}, {'axial_cord': (1, 6)},
        {'axial_cord': (7, -6)}, {'axial_cord': (7, -5)}, {'axial_cord': (8, -5)},
    

        {'axial_cord': (-1, 4)}, {'axial_cord': (0, 4)}, {'axial_cord': (-1, 5)},
        {'axial_cord': (4, -5)}, {'axial_cord': (3,-4)}, {'axial_cord': (4,-4)},


        {'axial_cord': (-1, 9)}, {'axial_cord': (0, 9)}, {'axial_cord': (1, 8)},
        {'axial_cord': (9, -9)}, {'axial_cord': (8, -9)}, {'axial_cord': (9, -8)},
        #Left Lane
        {'axial_cord': (-8, 2)}, {'axial_cord': (-8, 3)}, {'axial_cord': (-6, -2)}, {'axial_cord': (-5, -3)},
        
    ],
    Brush: [
        {'axial_cord': (9, -1)},{'axial_cord': (9, 0)},{'axial_cord': (8, 1)},
        {'axial_cord': (1, 0)}, {'axial_cord': (2, 0)},
        {'axial_cord': (4, 3)}, {'axial_cord': (7, -3)},

        #left lane
        {'axial_cord': (-2, 2)}, {'axial_cord': (-2, 1)}, {'axial_cord': (-1, 0)}, {'axial_cord': (-1, -1)}, {'axial_cord': (0, -2)},
        {'axial_cord': (-9, 4)}, {'axial_cord': (-9, 3)}, {'axial_cord': (-9, 2)}, {'axial_cord': (-9, 1)}, {'axial_cord': (-8, 1)},
        {'axial_cord': (-8, -1)}, {'axial_cord': (-7, -2)}, {'axial_cord': (-6, -3)}, {'axial_cord': (-5, -4)}, {'axial_cord': (-7, -1)},
        {'axial_cord': (-9, 0)}, {'axial_cord': (-7, 0)}, 
    ],

    MainBase: [
        {'axial_cord': (-6, 8), 'team':team_1}, 
        {'axial_cord': (2, -8), 'team': team_2},
    ],
    Turret: [
        {'axial_cord': (-2, 7), 'damage': (20, 30), 'attack_range':3, 'team':team_1 },
        {'axial_cord': (5, -7), 'damage': (20, 30), 'attack_range':3, 'team': team_2},

        {'axial_cord': (-3, 4), 'damage': (20, 30), 'attack_range':3, 'team':team_1},
        {'axial_cord': (1, -4), 'damage': (20, 30), 'attack_range':3, 'team': team_2},

        {'axial_cord': (-7, 5), 'damage': (20, 30), 'attack_range':3, 'team': team_1},
        {'axial_cord': (-2,-5), 'damage': (20, 30), 'attack_range':3, 'team':team_2},

    ],
}

power_sources = [
    {'axial_cord': (-4,0), 'turn':0, 'radius':3, 'power':4}, 
]

game_map = HexMap(screen=screen, map_structures=map_1, power_sources=power_sources)

is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False


    pg.display.flip()


pg.quit()