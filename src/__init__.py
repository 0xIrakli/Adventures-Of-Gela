from PIL import Image
import pygame

from src.player import Player

pygame.init()

disp = pygame.display
draw = pygame.draw


def init(size):
    return disp.set_mode(size)
