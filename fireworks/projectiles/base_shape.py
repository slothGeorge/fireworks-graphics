import turtle


class Basic_Moving_Shape(turtle.Turtle):
    '''Blueprint for other projectiles'''
    def __init__(self, objects):
        self.objects = objects
        self.objects.insert(0, self)
        self.y_acceleration = -6
        
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")

    def update(self):
        self.countdown -= 1
        if self.countdown < 0:
            self.objects.remove(self)
            self.clear()
            self.ht()
            del self
