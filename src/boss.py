from . import Entity
from PIL import Image
import pygame

class Boss(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.img = Image.open('assets/animations/boss.png')
        self.img = self.img.resize((self.img.width*4, self.img.height*4), Image.Resampling.NEAREST)
        self.img.save('AAA.png')
        self.imgs = pygame.image.load('AAA.png')
        
    def update(self):
        pass

    def draw(self, win):
        win.blit(self.imgs, (self.x-(self.img.width//2), self.y-(self.img.height//2)))