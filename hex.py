from math import sqrt, radians, cos, sin
import pygame
from typing import List

class Hex:
    def __init__(self, q:int, r:int, s:int = None) -> None:        
        #(q, r, s) 
        #Can be optimized by switching the a list function to run multithreaded once we move to C#
        if s is None:
            s = -q - r
        if q + r + s != 0:
            raise ValueError("Error: q + r + s must equal 0.")
        
        self.q = q
        self.r = r
        self.s = s

    def __eq__(self, other) -> bool:
        if isinstance(other, Hex):
            return all([
                self.q == other.q,
                self.r == other.r,
                self.s == other.s
            ])
        raise ValueError("You can only add a Hex class with another Hex class.")
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r, self.s + other.s)
    
    def __sub__(self, other):
        return Hex(self.q - other.q, self.r - other.r, self.s - other.s)
    
    def __mul__(self, other):
        if isinstance(other, Hex):
            return Hex(self.q * other.q, self.r * other.r, self.s * other.s)

        if isinstance(other, (int, float)):
            #Other = k when it's a scalar value
            return Hex(self.q * other, self.r * other, self.s * other)
        
        return NotImplemented
    
    def magnitude(self, other=None) -> int:
        ''' We divide by two because we're using a 3D grid system with a plane through it at x + y + z = 0.
        Typically, in a 3D system, we would calculate the length of this vector using the distance from 0, 0, 0.
        But, because we're only using diagnols, as opposed to every block in a discrete 3D grid, that means we're
        double counting using Manhattan distances. '''
        hex = self if other is None else other

        return int((abs(hex.q) + abs(hex.r) + abs(hex.s))/2)
    
    def distance_to(self, other) -> int:
        return self.magnitude(self-other)
    
    cube_direction_vectors = [
        (-1, 0, 1), (0, -1, 1), (1, -1, 0),
        (1, 0, -1), (0, 1, -1), (-1, 1, 0)
    ]

    @classmethod
    def direction(cls, direction):
        if -6 <= direction <= 5:
            return cls(**cls.cube_direction_vectors[direction])
        raise ValueError("direction must be between -5 to 5")
    
    def neighbor(self, direction):
        return self + self.direction(direction)
    
    def lerp(a: float, b:float, t:float):
        return a * (1-t) + (b * t)
        # a + (b - a) * t is more recognizable but worse on floating point arithmetic
    
    def hex_lerp(self, target_hex, t):
        if isinstance(target_hex, Hex):
            return fractional_to_int_hex(
                    self.lerp(self.q, target_hex.q, t),
                    self.lerp(self.r, target_hex.r, t),
                    self.lerp(self.s, target_hex.s, t)
                )
        raise ValueError("target_hex must be a Hex object.")
    
    #if this isn't working as intended, it may be due to exact values and we need a nudge
    def hex_line_to(self, target_hex):
        N = self.distance_to(target_hex)
        hexes = []
        for i in range(N):
            hex = self.hex_lerp(target_hex, 1.0/N * i)
            hexes.append(hex)


class Orientation:
    def __init__(self, f0, f1, f2, f3, b0, b1, b2, b3, start_angle) -> None:
        '''
        f values- are used to convert the 3D cordinates to 2D (forward)
        b values- are used to convert the 2D cordinates to 3D (backwards)
        '''

        self.f0 = f0
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.start_angle = start_angle

layout_pointy = Orientation(
        sqrt(3), sqrt(3)/2, 0, 3/2,
        sqrt(3)/3, -1/3, 0, 2/3,
        30
    )

layout_flat = Orientation(
    3/2, 0, sqrt(3)/2, sqrt(3),
    2/3, 0, -1/3, sqrt(3)/3,
    0.0
)

#Could use (x, y) to reduce memory over head if needed. The added methods may not be that useful.
Point = pygame.math.Vector2

def fractional_to_int_hex(q1: float, r1: float, s1: float) -> Hex:
    q = int(round(q1))
    r = int(round(r1))
    s = int(round(s1))

    dq = abs(q1-q)
    dr = abs(r1-r)
    ds = abs(s1-s)

    if (dq > dr and dq > ds):
        q = -r -s        
    elif (dr > ds):
        r = -q -s
    else:
        s = -q -r

    return Hex(q, r, s)


class Layout:
    def __init__(self, orientation: Orientation, size: Point, origin: Point, skew: int=0) -> None:
        self.orientation = orientation
        self.size = Point(size)
        self.origin = Point(origin)
        self.skew = skew

    #returns the center of the hex
    def hex_to_pixel(self, hex: Hex) -> Point: 
        M = self.orientation # M is the matrix for the orientation
        x = (M.f0 * hex.q + M.f1 * hex.r) * self.size.x
        y = (M.f2 * hex.q + M.f3 * hex.r) * self.size.y
        return Point(x + self.origin.x, y + self.origin.y)
    


    #returns a floating hex location that needs to be converted to target an real hex
    def pixel_to_hex(self, p: Point) -> Hex:
        M = self.orientation
        pt = Point(
            (p.x - self.origin.x) / self.size.x,
            (p.y - self.origin.y) / self.size.y,
        )
        q1 = M.b0 * pt.x + M.b1 * pt.y
        r1 = M.b2 * pt.x + M.b3 * pt.y
        s1 = -q1 - r1

        return fractional_to_int_hex(q1, r1, s1)

    
    def get_corner_offset(self, corner: int) -> Point:
        angle_deg = 60 * corner + self.orientation.start_angle
        angle_rad = radians(angle_deg)
        x = self.size.x * cos(angle_rad)
        y = self.size.y * sin(angle_rad)

        x += self.skew * y
        return Point(x, y)
    
    def get_hex_verticies(self, p: Point) -> List[Point]:
        verticies = []
        for corner in range(6):
            offset = self.get_corner_offset(corner)
            vertex = Point(p.x + offset.x, p.y + offset.y)
            verticies.append(vertex)
        return verticies



    
    




    

