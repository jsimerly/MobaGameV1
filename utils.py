import math


def get_hex_verticies(pos: (int,int), radius):
    x, y = pos
    verticies = []
    skew_intensity = 0
    
    for i in range(6):
        angle_deg = 60 * i + 30
        angle_rad = math.radians(angle_deg)
        cos = x + radius * math.cos(angle_rad)
        sin = y + radius * math.sin(angle_rad)

        cos += skew_intensity * sin

        verticies.append((cos, sin))
        
    return verticies

def cube_to_pixel(cube: (int, int, int), radius: int) -> (int, int):
    x, y, z = cube
    hex_width = math.sqrt(3) * radius
    hex_height = 2 * radius
    pixel_x = hex_width * (x + z/2)
    pixel_y = hex_height * (3/4) * z
    return (pixel_x, pixel_y)

def get_hexagons_in_radius(self, center_axial: (int, int), radius:int) -> []:
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

def axial_to_cube(axial_cord):
    q, r = axial_cord
    x = q
    z = r
    y =  -x - z
    return (x, y, z)

def cube_distance(cube1, cube2):
    x1, y1, z1 = cube1
    x2, y2, z2 = cube2
    return max(abs(x1-x2), abs(y1-y2), abs(z1-z2))

def hex_distance(axial1, axial2):
    cube1 = axial_to_cube(axial1)
    cube2 = axial_to_cube(axial2)
    return cube_distance(cube1, cube2)

