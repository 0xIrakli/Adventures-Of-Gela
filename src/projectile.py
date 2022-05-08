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


class ProjectileEmitter():
    def __init__(self, win):
        self.win = win

        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def get_projectile(self):
        self.a += 1

        self.b += self.a
        self.c += self.a ** 2
        self.d += self.a / 3

        y = self.b * self.c * self.d % (self.win.get_height() - 128) + 64

        return Projectile(self.win.get_width(), y)
