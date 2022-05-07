import pygame

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.v = [0, 0]
        self.speed = 4
    
    @property    
    def x(self):return self.pos[0]
    @property
    def y(self):return self.pos[1]
    @property    
    def vx(self):return self.v[0]
    @property
    def vy(self):return self.v[1]
    
    def update(self, win, deltaT):
        self.look()
        self.move(deltaT)
        self.draw(win)
    
    def look(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]: self.v[0] = -self.speed
        if keys[pygame.K_d]: self.v[0] =  self.speed
        if keys[pygame.K_w]: self.v[1] = -self.speed
        if keys[pygame.K_s]: self.v[1] =  self.speed
    
    def move(self, deltaT):
        self.v[0] *= 0.8
        self.v[1] *= 0.8
        self.pos[0] += self.v[0]#*deltaT*0.001
        self.pos[1] += self.v[1]#*deltaT*0.001
        
    def draw(self, win):
        pygame.draw.ellipse(win, (255, 110, 110), (self.x, self.y, 40, 40), 2)