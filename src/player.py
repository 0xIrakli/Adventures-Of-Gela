from .entity import Entity
from .utils import get_animation_frames
import pygame
from PIL import Image
from math import atan2


class Player(Entity):
    speed = 5

    def __init__(self, pos):
        super().__init__(pos)
        self.animation = get_animation_frames(
            Image.open('assets/animations/player.png'), 16)
        self.frame_index = 0
        self.current_rot = 0
        self.lastpos = []
        self.bar = 0

    def update_frame_index(self):
        if abs(self.vx) + abs(self.vy) <= 0.2:
            self.frame_index = 0
        else:
            self.frame_index = (self.frame_index + 1) % len(self.animation)

    def get_bounding_rect(self):
        self.look()
        rect1 = self.handle_rotation(
            self.animation[self.frame_index]).get_rect()
        rect = pygame.rect.Rect(
            self.x+rect1.left, self.y+rect1.top, rect1.right, rect1.bottom)
        return rect

    def update(self, walls):
        l = self.get_bounding_rect().collidelist(walls)

        if l == -1:
            self.move()
        elif l == 0:
            self.pos[1] += self.speed
            self.v[1] *= 0
        elif l == 1:
            self.pos[0] += -self.speed
            self.v[0] *= 0
        elif l == 2:
            self.pos[1] += -self.speed
            self.v[1] *= 0
        elif l == 3:
            self.pos[0] += self.speed
            self.v[0] *= 0
            
        self.bar += 1

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

    def handle_rotation(self, img):
        target = atan2(self.v[1], self.v[0]) * 180 / \
            3.1415926 if abs(self.v[0] * self.v[1]
                             ) > 0.0001 else self.current_rot
        self.current_rot += target - self.current_rot

        return pygame.transform.rotate(img, -self.current_rot)

    def draw(self, win):
        img = self.handle_rotation(
            self.animation[int(self.frame_index)].copy())

        win.blit(img, pygame.rect.Rect(self.x, self.y, self.x +
                 img.get_width(), self.y+img.get_height()))
