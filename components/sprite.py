import pygame as pg
from .component import Component

class SpriteComponent(Component):
    def __init__(self, image):
        image_surface = pg.image.load(image)
        self.is_selected = False

        self.std_image = pg.transform.scale(image_surface, (60,60))
        self.selected_image = pg.transform.scale(image_surface, (70, 70))
        self.current_image = self.std_image

        self.rect = self.std_image.get_rect()

    def draw(self, screen: pg.display):
        screen.blit(self.current_image, self.rect)

    def get_top_left_pos(self, center_pos:(int,int)) -> (int, int):
        top_left_pos = (
            center_pos[0] - self.rect.width//2, 
            center_pos[1] - self.rect.height//2,
        )
        return top_left_pos
        
    def update(self, mouse_pos, mouse_pressed):
            touching = self.rect.collidepoint(mouse_pos)

            if mouse_pressed:
                if touching:
                    self.is_selected = True
                else:
                    self.is_selected = False

            current_image = self.selected_image if self.is_selected else self.std_image
            self.current_image = current_image
            
    def move_to_pixel(self, center_pos):
        top_left_pos = self.get_top_left_pos(center_pos)

        self.rect.x = top_left_pos[0]
        self.rect.y = top_left_pos[1]
