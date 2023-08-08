from random import randint

from projectiles.base_shape import Basic_Moving_Shape


class Rocket(Basic_Moving_Shape):

    def __init__(self):
        super().__init__()
        self.is_rocket = True
        self.color('#FFFFFF')
        self.goto(randint(-50,50), -300)
        self.y_speed = 60 + randint(0, 10)
        self.x_speed = randint(-5, 5)
        self.countdown = 17
