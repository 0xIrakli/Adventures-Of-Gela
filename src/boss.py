from . import Entity
import pygame

class Boss(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        
    def update(self):
        pass

    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (0, 240, 20),
            (self.x, self.y, 60, 60),
            4
        )
