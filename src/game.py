from .player import Player
from PIL import Image
from .utils import generate_tilemap, build_level
import pygame


class Game:
    def __init__(self):
        self.player = Player([100, 100])
        self.level = 0
        self.level_surface = 0
        self.level_surface_rect = 0

    def create_level(self, tilemap_path, base, win):
        img = Image.open(tilemap_path)

        tilemap = generate_tilemap(16)
        lev = build_level(tilemap, base, 1, 16)
        lev = lev.resize((lev.width*4, lev.height*4), 0)
        lev.save('background.png')
        self.level = lev
        self.level_surface = pygame.image.load("background.png").convert(win)
        self.level_surface_rect = self.level_surface.get_rect()

    def loop(self, win, walls):
        win.fill((0, 0, 0))
        win.blit(self.level_surface, self.level_surface_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        self.player.draw(win)
        self.player.update(walls)
