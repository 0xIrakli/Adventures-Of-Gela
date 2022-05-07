import pygame
from . import Entity


class Player(Entity):
    speed = 350

    def __init__(self, pos):
        super().__init__(pos)

    def update(self, delta_time):
        self.look()
        self.move(delta_time)

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
            (255, 110, 110),
            (self.x, self.y, 40, 40),
            2
        )
