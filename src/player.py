import pygame
from . import Entity


class Player(Entity):
    speed = 4

    def __init__(self, pos):
        super().__init__(pos)

    def update(self):
        self.look()
        self.move()

    def look(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.v[0] = -self.speed
        if keys[pygame.K_d]:
            self.v[0] = self.speed
        if keys[pygame.K_w]:
            self.v[1] = -self.speed
        if keys[pygame.K_s]:
            self.v[1] = self.speed

    def move(self):
        self.v[0] *= 0.8
        self.v[1] *= 0.8

        super().move()

    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (150, 150, 0),
            (self.x, self.y, 40, 40),
            10,
        )
