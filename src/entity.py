class Entity:
    v = [0, 0]
    speed = 4

    def __init__(self, pos):
        self.pos = pos

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def vx(self):
        return self.v[0]

    @property
    def vy(self):
        return self.v[1]

    def move(self):
        self.pos[0] += self.v[0]# * delta_time * 0.001
        self.pos[1] += self.v[1]# * delta_time * 0.001

    def update(self, delta_time):
        raise Exception(
            f'Undefined error: {self.__name__} has no defined function update()'
        )

    def draw(self, win):
        raise Exception(
            f'Undefined error: {self.__name__} has no defined function draw()'
        )
