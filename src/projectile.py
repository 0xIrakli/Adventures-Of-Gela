from . import Entity


class Projectile(Entity):
    speed = 500

    def __init__(self, x, y):
        super().__init__([x, y])

    def draw(self, win):
        # TODO: Irakli shen mixedav amas!
        ...

    def update(self, delta_time):
        super().move(delta_time)
        
    def draw(self, win):
        pygame.draw.ellipse(
            win,
            (255, 110, 110),
            (self.x, self.y, 40, 40),
            2
        )
