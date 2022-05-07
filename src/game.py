from . import Player, Image, generate_tilemap, build_level, pygame


class Game:
    def __init__(self):
        self.player = Player([10, 10])

    def load_tilemap(self, tilemap_path, base):
        img = Image.open(tilemap_path)

        tilemap = generate_tilemap(16)
        build_level(tilemap, base, 0, 16)

    def loop(self, win):
        win.fill((51, 51, 51))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        self.player.update()
        self.player.draw(win)
