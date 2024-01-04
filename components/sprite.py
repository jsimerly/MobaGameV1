import pygame as pg
from .component import Component

class SpriteComponent(Component):
    def __init__(self, image):
        image_surface = pg.image.load(image)
        resized_image = pg.transform.scale(image_surface, (60,60))
        self.image = resized_image
        self.rect = self.image.get_rect()

    def draw(self, screen_pos:(int,int), screen: pg.display):
        top_left_pos = self.get_top_left_pos(screen_pos)
        screen.blit(self.image, top_left_pos)

    def get_top_left_pos(self, center_pos:(int,int)):
        top_left_pos = (
            (center_pos[0] - self.rect.width) // 2, 
            (center_pos[1] - self.rect.height) // 2)
        return top_left_pos

    def move_to_pixel(self, x, y):
        self.rect.x = x
        self.rect.y = y