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
        self.setx(self.xcor() + self.x_speed)
        self.sety(self.ycor() + self.y_speed)
        self.y_speed += self.y_acceleration
        self.countdown -= 1
        if self.countdown < 0:
            self.kill()
    
    def kill(self):
        self.objects.remove(self)
        self.clear()
        self.ht()
        del self
