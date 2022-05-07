from PIL import Image
from src import *
import pygame

pygame.init()

disp = pygame.display
draw = pygame.draw
        
REZ = 64 #dava upscalebt im 8x8 spritebs pygameit
WIDTH = 16
HEIGHT = 8

MOVEMENT = {
    pygame.K_a: [-1,  0],
    pygame.K_d: [ 1,  0],
    pygame.K_s: [ 0,  1],
    pygame.K_w: [ 0, -1]
}

img = Image.open('assets/levels/0/tilemap.png')

base = [
    [
        1 if (i % WIDTH) * (j % HEIGHT) > 0 else 0
        for j in range(HEIGHT)
    ] for i in range(WIDTH)
]

def build_levels(levels):
    img = Image.new("RGB", (len(base[0])*8, len(base)*8))
    for level in levels:
        for y in range(len(base)):
            for x in range(len(base[0])):
                img.paste(level[base[y][x]], box=(x*8, y*8, (x+1)*8, (y+1)*8))
    img.save('img.png')

def init(size):
    return disp.set_mode(size)

def generate_tilemap(res):
    tiles = []
    tilemap = Image.open('assets/levels/0/tilemap.png')
    for y in range(tilemap.height//res):
        for x in range(tilemap.width//res):
            tiles.append(image.crop((res*x, res*y, res, res)))
    return tiles

win = init((WIDTH*REZ, HEIGHT*REZ))
tilemap = generate_tilemap(16)

def main():
    for j, i in enumerate(generate_tilemap(16)):
        i.save(f'{j}.png')
    player = Player([10, 10])
    clock = pygame.time.Clock()
    while True:
        win.fill((51, 51, 51))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        player.update(win, clock.tick(60))
        disp.update()

main()
