from . import Entity
import pygame


class Projectile(Entity):
    speed = 500
    v = [-7, 0]

    def __init__(self, x, y):
        super().__init__([x, y])

    def update(self):
        super().move()

    def get_bounding_rect(self):
        return pygame.rect.Rect(self.x - 10, self.y - 10, 20, 20)

    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (240, 240, 240),
            (self.x, self.y, 20, 20),
            2
        )
