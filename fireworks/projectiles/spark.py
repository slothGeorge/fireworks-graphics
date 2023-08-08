from random import randint

from projectiles.base_shape import Basic_Moving_Shape


class Spark(Basic_Moving_Shape):
    def __init__(self, x, y):
        super().__init__()
        color = [randint(100,255), randint(100,255), randint(100,255)]
        self.color(f"#{''.join(f'{hex(i)[2:].upper():0>2}' for i in color)}")
        self.goto(x,y)
        self.resizemode("user")
        self.shapesize(randint(1,4), randint(1,4))
        self.y_speed = randint(20, 50)
        self.x_speed = randint(-20, 20)
        self.countdown = randint(7, 21)
