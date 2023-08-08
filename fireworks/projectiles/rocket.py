from random import randint

from projectiles.base_shape import Basic_Moving_Shape
from projectiles.spark import Spark


class Rocket(Basic_Moving_Shape):

    def __init__(self, objects):
        super().__init__(objects)
        self.color('#FFFFFF')
        self.goto(randint(-50,50), -300)
        self.y_speed = 60 + randint(0, 10)
        self.x_speed = randint(-5, 5)
        self.countdown = 17

    def update(self):
        super().update()
        if self.countdown < 0:
            self.explode()

    def explode(self):
        for i in range(randint(20, 30)):
            spark = Spark(self.xcor(), self.ycor(), self.objects)  # temporarily passing a god object, anti-pattern