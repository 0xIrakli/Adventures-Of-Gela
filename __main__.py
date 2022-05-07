from PIL import Image
from src import *


REZ = 64  # dava upscalebt im 8x8 spritebs pygameit
WIDTH = 16
HEIGHT = 8


def main():
    pygame.init()

    win = pygame.display.set_mode((WIDTH * REZ, HEIGHT * REZ))
    clock = pygame.time.Clock()

    base = [
        [
            (i % (HEIGHT - 1)) * (j % (WIDTH - 1)) > 0
            for j in range(WIDTH)
        ] for i in range(HEIGHT)
    ]

    game = Game()
    game.load_tilemap('assets/levels/0/tilemap.png', base)

    while True:
        game.loop(win)
        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
