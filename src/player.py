from . import Entity
import pygame

class Player(Entity):
    speed = 5
    def __init__(self, pos):
        super().__init__(pos)
        self.animation = get_animation_frames(Image.open('assets/animations/player.png'), res)
        self.index = 0
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
        win.blit(self.animation[self.index], self.animation[self.index].get_rect())
