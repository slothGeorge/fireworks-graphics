from random import randint

from projectiles.base_shape import Basic_Moving_Shape


COLOR_BOUNDS = (100, 255)


class Spark(Basic_Moving_Shape):
    def __init__(self, x, y):
        super().__init__()
        self.color(self.get_random_color())
        self.goto(x,y)
        self.resizemode("user")
        self.shapesize(randint(1,4), randint(1,4))
        self.y_speed = randint(20, 50)
        self.x_speed = randint(-20, 20)
        self.countdown = randint(7, 21)
    
    @staticmethod
    def get_random_color():
        color_parts = ['#']
        color_parts += [
            hex(randint(*COLOR_BOUNDS))[2:]  # to chop off starting '0x' part
            for _ in range(3)
        ]
        colors_text = ''.join(color_parts)
        return colors_text
