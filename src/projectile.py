from . import Entity


class Projectile(Entity):
    speed = 500

    def __init__(self, x, y):
        super().__init__([x, y])

    def draw(self, win):
        # TODO: Irakli shen mixedav amas!
        ...

    def update(self):
        super().move()
        
    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (240, 240, 240),
            (self.x, self.y, 20, 20),
            2
        )
