from PIL import Image
from src import *

WIDTH = 16
HEIGHT = 8


def main():
    pygame.init()

    clock = pygame.time.Clock()

    base = [
        [
            (i % (HEIGHT - 1)) * (j % (WIDTH - 1)) > 0
            for j in range(WIDTH)
        ] for i in range(HEIGHT)
    ]

    game = Game()
    win = pygame.display.set_mode((500, 500))
    game.create_level('assets/levels/tilemap.png', base, win)
    win = pygame.display.set_mode((game.level.width, game.level.height))

    frame_count = 0
    while True:
        game.loop(win, frame_count)
        pygame.display.update()
        clock.tick(60)
        frame_count += 1

if __name__ == '__main__':
    main()
