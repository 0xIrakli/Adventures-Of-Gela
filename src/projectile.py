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
