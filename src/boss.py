from . import Entity
from PIL import Image
import pygame

class Boss(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = Image.open('assets/animations/boss.png')
        self.img = self.img.resize(img.width*4, img.height*4)
        self.img.save('AAA.png')
        self.img = pygame.image.load('AAA.png').convert(win)
        
    def update(self):
        pass

    def draw(self, win):
        win.blit(self.img, self.x-img.width, self.y-img.height)