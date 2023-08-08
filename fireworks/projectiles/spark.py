from random import randint
import turtle

# from fireworks.fireworks import kill_turtle


class Spark(turtle.Turtle):
    def __init__(self, x, y, objects):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        color = [randint(100,255), randint(100,255), randint(100,255)]
        self.color(f"#{''.join(f'{hex(i)[2:].upper():0>2}' for i in color)}")
        self.goto(x,y)
        self.resizemode("user")
        self.shapesize(randint(1,4), randint(1,4))
        self.y_speed = randint(20, 50)
        self.x_speed = randint(-20, 20)
        self.y_acceleration = -6
        self.countdown = randint(7, 21)
        self.objects = objects
        self.objects.insert(0, self)
    def update(self):
        self.countdown -= 1
        if self.countdown < 0:
            # kill_turtle(self)
            self.objects.remove(self)
            self.clear()
            self.ht()
            del self
