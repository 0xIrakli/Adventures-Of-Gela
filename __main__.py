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
    width, height = size = (game.level.width, game.level.height)
    win = pygame.display.set_mode(size)
    rect = pygame.rect.Rect
    walls = [
        rect(0, 0, width, 64),
        rect(width-64, 0, 64, height),
        rect(0, height-64, width, 64),
        rect(0, 0, 64, height)
    ]
    frame_count = 0

    while True:
        if frame_count % 10 == 0:
            game.player.update_frame_index()
        game.loop(win, walls)
        pygame.display.update()
        clock.tick(60)
        frame_count += 1


if __name__ == '__main__':
    main()
