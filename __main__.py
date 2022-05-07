from PIL import Image
from src import *
import pygame

pygame.init()

disp = pygame.display
draw = pygame.draw

RES = 64  # dava upscalebt im 8x8 spritebs pygameit
WIDTH = 16
HEIGHT = 8

img = Image.open('assets/levels/0/tilemap.png')

base = [
    [
        1 if (i % WIDTH) * (j % HEIGHT) > 0 else 0
        for j in range(HEIGHT)
    ] for i in range(WIDTH)
]


def build_level(tilemap, level, level_n, res):
    img = Image.new("RGBA", (len(level[0]) * res, len(level) * res))
    for y in range(len(level)):
        for x in range(len(level[0])):
            img.paste(rand.choice(tilemap[level_n][level[y][x]]), box=(
                x * res, y * res, (y + 1) * res, (x + 1) * res))
    img.save('img.png')


def init(size):
    return disp.set_mode(size)


win = init((WIDTH*RES, HEIGHT*RES))
ress = 16
tilemap = generate_tilemap(ress)

print(tilemap)


def main():
    build_level(tilemap, base, 0, ress)
    player = Player([10, 10])
    clock = pygame.time.Clock()

    while True:
        win.fill((51, 51, 51))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        player.update(clock.tick(60))
        player.draw(win)
        disp.update()


main()
