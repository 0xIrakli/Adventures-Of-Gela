from .entity import Entity
from .utils import get_animation_frames
import pygame
from PIL import Image


class Player(Entity):
    speed = 5

    def __init__(self, pos):
        super().__init__(pos)
        self.animation = get_animation_frames(
            Image.open('assets/animations/player.png'), 16)
        self.frame_index = 0

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
        win.blit(self.animation[int(self.frame_index)],
                 self.animation[int(self.frame_index)].get_rect())

        self.frame_index += .1
        self.frame_index %= len(self.animation)
