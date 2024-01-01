import pygame as pg
import math        
from settings import LIGHT_GREY, SCREEN_WIDTH, SCREEN_HEIGHT
from typing import List
from utils import get_hex_verticies, cube_to_pixel, hex_distance
from combat import AttackComponent
from teams import Team

pg.font.init()
font = pg.font.SysFont(None, 24)
class HexTile:     
    def __init__(
            self, 
            screen: pg.display,  
            center_pixel_pos: (int, int),
            axial_cord:(int,int), 
            cube_cord=(int, int, int)
    ):
        self.screen = screen
        self.is_occupied = False
        self.character = None
        self.structure = None
        self.color = (123,182,101)

        self.axial_cord = axial_cord
        self.cube_cord = cube_cord
        self.center_pixel_pos = center_pixel_pos

        self.draw()
        
    radius = 32
    width = radius * math.sqrt(3)
    height = radius * 2
    outline_thickness = 2
    
    def set_structure(self, structure) -> (int, int):
        self.structure = structure
        return self.center_pixel_pos

    def remove_structure(self):
        self.structure = None
        self.is_occupied = False
    
    def draw(self):
        verticies = get_hex_verticies(self.center_pixel_pos, radius=HexTile.radius)
        pg.draw.polygon(self.screen, self.color, verticies)
        pg.draw.polygon(self.screen, LIGHT_GREY, verticies, self.outline_thickness)
            
class HexMap:
    GRID_RADIUS = 9

    def __init__(self, screen: pg.display, map_structures, power_sources:list):
        self.screen = screen
        self.map_structures = map_structures
        self.tiles = {}
        self.generate_grid()
        self.place_structures()
        self.power_sources = self.place_power_sources(power_sources)

    def get_pixel_pos_axial(self, axial_cord, radius):
        q, r = axial_cord
        x = radius * math.sqrt(3) * (q + r/2)
        y = radius * 1.5 * r
        return (x, y)
    
    def get_hexagons_in_radius(self, center_axial: (int, int), radius:int) -> List[HexTile]:
        hexagons = []
        cx, cz = center_axial
        
        for dx in range(-radius, radius + 1):
            for dy in range(max(-radius, -dx - radius), min(radius, -dx + radius) + 1):
                dz = -dx - dy
                x = cx + dx
                z = cz + dz
                axial_coord = (x, z)

                hexagons.append(axial_coord)

        return hexagons
    
    def generate_grid(self):
        radius = self.GRID_RADIUS
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        center_axial = (0, 0)  # Assuming the center of the grid is at axial coordinates (0, 0)

        hexagons = self.get_hexagons_in_radius(center_axial, radius)

        for axial_cord in hexagons:
            q, r = axial_cord
            cube_cord = (q, -q - r, r)

            center_pixel_pos = self.get_pixel_pos_axial(axial_cord, HexTile.radius)
            center_pixel_pos = (center_pixel_pos[0] + center_x, center_pixel_pos[1] + center_y)

            self.tiles[axial_cord] = HexTile(screen=self.screen, center_pixel_pos=center_pixel_pos, cube_cord=cube_cord, axial_cord=axial_cord)
    
    def place_structures(self):
        for structure_obj in self.map_structures:
            for obj_params in self.map_structures[structure_obj]:
                axial_cord = obj_params['axial_cord']

                # Get the center tile for the structure
                center_tile = self.tiles[axial_cord]
                structure_instance = structure_obj(tile=center_tile, game_map=self, **obj_params)
                structure_size = structure_instance.size

                # Get all hexagons within the specified radius
                affected_hexagons = self.get_hexagons_in_radius(axial_cord, structure_size - 1)

                # Set the structure on the center and surrounding tiles
                for hex_axial in affected_hexagons:
                    if hex_axial in self.tiles:
                        tile = self.tiles[hex_axial]
                        tile.set_structure(structure_instance)

    def place_power_sources(self, power_sources):
        all_power_sources = []
        for obj_params in power_sources:
            axial_cord = obj_params['axial_cord']
            center_tile = self.tiles[axial_cord]
            power_sources_instance = PowerSource(tile=center_tile, game_map=self, **obj_params)
            all_power_sources.append(power_sources_instance)

        return all_power_sources

class MapStructure:
    def __init__(
            self, 
            is_pass_through:bool, 
            size: int, 
            tile: HexTile,
            game_map: HexMap,
            destructable: bool,
            axial_cord: (int, int)
        ):
        self.is_pass_through = is_pass_through
        self.size = size 
        self.tile = tile
        self.game_map = game_map
        self.destructable = destructable
        self.axial_cord = axial_cord
        self.color = (194, 43, 75)

    def draw(self):
        if self.size > 1:
            # Find all hexagons within the structure's size radius
            hexagons = self.game_map.get_hexagons_in_radius(self.axial_cord, self.size - 1)
            for hex_axial in hexagons:
                if hex_axial in self.game_map.tiles:
                    hex_tile = self.game_map.tiles[hex_axial]
                    vertices = get_hex_verticies(hex_tile.center_pixel_pos, HexTile.radius)
                    pg.draw.polygon(hex_tile.screen, self.color, vertices)

        vertices = get_hex_verticies(self.tile.center_pixel_pos, HexTile.radius)
        pg.draw.polygon(self.tile.screen, self.color, vertices)

        

#Map Elements
class IndestructableRock(MapStructure):
    def __init__(self, tile: HexTile, game_map: HexMap, axial_cord:(int, int)):
        super().__init__(is_pass_through=False, size=1, tile=tile, destructable=False, game_map=game_map, axial_cord=axial_cord)
        self.color = (58,50,50)
        self.draw()

class DestructableTree(MapStructure):
    def __init__(self, tile: HexTile, game_map: HexMap, axial_cord:(int, int)):
        super().__init__(is_pass_through=False, size=1, tile=tile, destructable=True,  game_map=game_map, axial_cord=axial_cord)
        self.health = 1
        self.color = (20, 51, 6)
        self.draw()
    
class Water(MapStructure):
    def __init__(self, tile: HexTile, game_map: HexMap, axial_cord:(int, int)):
        super().__init__(is_pass_through=True, size=1, tile=tile, destructable=False,  game_map=game_map, axial_cord=axial_cord)
        self.color = (152, 216, 227)
        self.draw()

class Brush(MapStructure):
    def __init__(self, tile: HexTile, game_map: HexMap, axial_cord:(int, int)):
        super().__init__(is_pass_through=True, size=1, tile=tile, destructable=False,  game_map=game_map, axial_cord=axial_cord)
        self.color = (130, 148, 67)
        self.draw()

    def adjust_transparency(self, color, alpha):
        r, g, b = color
        return (r,g,b,alpha)

    def draw(self):      
        hexagons = self.game_map.get_hexagons_in_radius(self.axial_cord, self.size - 1)
        for hex_axial in hexagons:
            print(hexagons)
            if hex_axial in self.game_map.tiles:
                hex_tile = self.game_map.tiles[hex_axial]

                alpha = 185
                adjusted_color = self.adjust_transparency(self.color, alpha)

                temp_surface = pg.Surface((HexTile.width, HexTile.height), pg.SRCALPHA)
                vertices = get_hex_verticies((HexTile.width//2, HexTile.height//2), HexTile.radius)

                pg.draw.polygon(temp_surface, adjusted_color, vertices)

                top_left_x = hex_tile.center_pixel_pos[0] - HexTile.width // 2
                top_left_y = hex_tile.center_pixel_pos[1] - HexTile.height // 2
                top_left_pos = (top_left_x, top_left_y)

                self.tile.screen.blit(temp_surface, top_left_pos)
                    
#Buildings    
class MainBase(MapStructure):
    def __init__(self, tile: HexTile, game_map: HexMap, axial_cord:(int, int), team:Team):
        super().__init__(
            is_pass_through=False, 
            size=2, 
            tile=tile, 
            destructable=True, 
            game_map=game_map, 
            axial_cord=axial_cord
        )
        self.health = 1000
        self.color = (171, 209, 202)
        self.team = team
        self.color = team.color
        self.draw()

class Turret(MapStructure):
    def __init__(self, tile: HexTile, damage: (int, int), attack_range: int, game_map: HexMap, axial_cord:(int, int), team:Team):
        super().__init__(
            is_pass_through=False, 
            size=1, 
            tile=tile, 
            destructable=True, 
            game_map=game_map,
            axial_cord=axial_cord,
        )

        self.health = 200
        self.attack_component = AttackComponent()
        self.attack_charged = True
        self.damage = damage
        self.attack_range = attack_range
        self.color = (207, 208, 209)
        self.team = team
        self.color = team.color
        self.draw()

    def attack(self):
        if self.attack_charged:
            self.attack_component.attack(self.damage)
            self.attack_charged = False
            return
        
        self.charge_attack()

    def charge_attack(self):
        self.attack_charged = True


class PowerSource:
    def __init__(self, tile:HexTile, turn:int, radius:int, power:int, axial_cord: (int, int), game_map: HexMap):
        self.tile = tile
        self.axial_cord = axial_cord
        self.radius = radius
        self.power = power
        self.color = (179, 86, 184)
        self.turn = turn
        self.game_map = game_map
        self.draw()

    def adjust_transparency(self, color, alpha):
        r, g, b = color
        return (r,g,b,alpha)
    
    def draw(self):
        if self.radius > 1:
            hexagons = self.game_map.get_hexagons_in_radius(self.tile.axial_cord, self.radius - 1)
            for hex_axial in hexagons:
                if hex_axial in self.game_map.tiles:
                    hex_tile = self.game_map.tiles[hex_axial]

                    distance = hex_distance(self.axial_cord, hex_axial)
                    alpha = max(10, 185 - distance * 30)
                    adjusted_color = self.adjust_transparency(self.color, alpha)

                    # Create a new surface with per-pixel alpha
                    temp_surface = pg.Surface((HexTile.width, HexTile.height), pg.SRCALPHA)
                    vertices = get_hex_verticies((HexTile.width//2, HexTile.height//2), HexTile.radius)
                    
                    # Draw on the temporary surface
                    pg.draw.polygon(temp_surface, adjusted_color, vertices)

                    top_left_x = hex_tile.center_pixel_pos[0] - HexTile.width // 2
                    top_left_y = hex_tile.center_pixel_pos[1] - HexTile.height // 2
                    top_left_pos = (top_left_x, top_left_y)

                    self.tile.screen.blit(temp_surface, top_left_pos)

        vertices = get_hex_verticies(self.tile.center_pixel_pos, HexTile.radius)
        pg.draw.polygon(self.tile.screen, self.color, vertices)
