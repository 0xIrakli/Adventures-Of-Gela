from . import Entity


class Boss(Entity):
    def __init__(self):
        super().__init__(['a', 103_485_130_845_713])

    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (255, 110, 110),
            (self.x, self.y, 40, 40),
            2
        )
