from .projectile import Projectile, ProjectileEmitter
from .player import Player
from .boss import Boss
from PIL import Image
from .utils import generate_tilemap, build_level
import pygame


class Game:
    def __init__(self, base):
        self.base = base
        self.player = Player([100, 100])
        self.boss = Boss([0, 0])
        self.level_n = 0
        self.level = 0
        self.level_surface = 0
        self.level_surface_rect = 0

        self.count = 0

        self.projectiles = []

    def shoot_projectile(self):
        self.projectiles.append(self.projectile_emitter.get_projectile())

    def create_level(self, tilemap_path, base, win):
        img = Image.open(tilemap_path)

        tilemap = generate_tilemap(16)
        lev = build_level(tilemap, base, self.level_n, 16)
        lev = lev.resize((lev.width*4, lev.height*4), 0)
        self.boss.pos[0] = lev.width-64
        self.boss.pos[1] = lev.height//2
        lev.save('background.png')
        self.level = lev
        self.level_surface = pygame.image.load("background.png").convert(win)
        self.level_surface_rect = self.level_surface.get_rect()

        self.projectile_emitter = ProjectileEmitter(win)

    def loop(self, win, walls):
        win.fill((0, 0, 0))
        win.blit(self.level_surface, self.level_surface_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        self.boss.update(self.player)
        self.player.update(walls)

        if not self.boss.alive:
            self.level_n += 1
            if self.level_n >= 4:
                print('---------YOU WON YOU ARE FREE---------')
                pygame.quit()
                quit()
            else:
                self.boss.alive = True
                self.create_level('assets/levels/tilemap.png', self.base, win)
        player_rect = self.player.get_bounding_rect()

        for projectile in self.projectiles:
            projectile.update()
            projectile.draw(win)

            if player_rect.collidelist([projectile.get_bounding_rect()]) != -1:
                print('---------YOU LOST---------')
                quit()

        self.boss.draw(win)
        self.player.draw(win)

        self.count += 1

        if self.count % 15 == 0:
            self.shoot_projectile()
