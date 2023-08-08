from random import randint
import turtle

from projectiles.spark import Spark


class Rocket(turtle.Turtle):

    def __init__(self, objects):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color('#FFFFFF')
        self.goto(randint(-50,50), -300)
        self.y_speed = 60 + randint(0, 10)
        self.x_speed = randint(-5, 5)
        self.y_acceleration = -6
        self.countdown = 17
        self.objects = objects
        self.objects.insert(0, self)

    def update(self):
        self.countdown -= 1
        if self.countdown < 0:
            self.explode()
            self.objects.remove(self)
            self.clear()
            self.ht()
            del self

    def explode(self):
        for i in range(randint(20, 30)):
            spark = Spark(self.xcor(), self.ycor(), self.objects)  # temporarily passing a god object, anti-pattern