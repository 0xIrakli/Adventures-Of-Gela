from PIL import Image
import pygame
from src.player import Player

pygame.init()

disp = pygame.display
draw = pygame.draw


def init(size):
    return disp.set_mode(size)

def generate_tilemap(res):
    tiles = []
    tilemap = Image.open('/assests/levels/0/tilemap.png')
    for y in range(res.height/res):
        for x in range(res.width/res):
            pass