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
        self.current_rot = 0
        
    def update_frame_index(self):
        if abs(self.vx) + abs(self.vy) <= 0.1:
            self.frame_index = 0
        else:
            self.frame_index = (self.frame_index + 1) %len(self.animation)

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

    def check(self, img):
        if self.v[0] >= 0.8 and self.v[1] >= 0.8:
            self.current_rot = 135-self.current_rot
        elif self.v[0] <= -0.8 and self.v[1] <= -0.8:
            self.current_rot = 315-self.current_rot
        elif self.v[0] >= 0.8 and self.v[1] <= -0.8:
            self.current_rot = 45-self.current_rot
        elif self.v[0] <= -0.8 and self.v[1] >= 0.8:
            self.current_rot = 225-self.current_rot
        elif self.v[0] >= 0.8:
            self.current_rot = 90-self.current_rot
        elif self.v[0] <= -0.8:
            self.current_rot = 270-self.current_rot
        elif self.v[1] >= 0.8:
            self.current_rot = 180-self.current_rot
        elif self.v[1] <= -0.8:
            self.current_rot = 0-self.current_rot
        return pygame.transform.rotate(img, self.current_rot)

    def draw(self, win):
        img = self.check(self.animation[int(self.frame_index)].copy())
        win.blit(img, pygame.rect.Rect(self.x, self.y, self.x+img.get_width(), self.y+img.get_height()))
