from src import *

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.v = [0, 0]
    
    @property    
    def x(self):return self.pos[0]
    @property
    def y(self):return self.pos[1]
    @property    
    def vx(self):return self.v[0]
    @property
    def vy(self):return self.v[1]
    
    def update(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
    
    def move(self, dirc):
        self.v = dirc
        
    def draw(self, win):
        pygame.draw.ellipse(win, (255, 110, 110), (self.x-20, self.y-20, self.x+20, self.y+20), 2)