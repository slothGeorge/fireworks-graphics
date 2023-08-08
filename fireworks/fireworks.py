import turtle
from random import randint

objects = []

def rocket_launch():
    rocket = Rocket()

def game_exit():
    turtle.bye()
    
def kill_turtle(obj):
    objects.remove(obj)
    obj.clear()
    obj.ht()
    del obj

class Spark(turtle.Turtle):
    def __init__(self, x, y):
        global ojbects
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
        objects.insert(0, self)
    def update(self):
        self.countdown -= 1
        if self.countdown < 0:
            kill_turtle(self)

def explode(x, y):
    for i in range(randint(20, 30)):
        spark = Spark(x, y)

class Rocket(turtle.Turtle):
    def __init__(self):
        global objects
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color('#FFFFFF')
        self.goto(randint(-50,50), -300)
        self.y_speed = 60 + randint(0, 10)
        self.x_speed = randint(-5, 5)
        self.y_acceleration = -6
        self.countdown = 17
        objects.insert(0, self)
    def update(self):
        self.countdown -= 1
        if self.countdown < 0:
            explode(self.xcor(), self.ycor())
            kill_turtle(self)
            
def animate():
    global objects
    if len(objects)>0:
        for obj in objects:
            obj.setx(obj.xcor() + obj.x_speed)
            obj.sety(obj.ycor() + obj.y_speed)
            obj.y_speed += obj.y_acceleration
            obj.update()
    window.ontimer(animate, 20)

def draw_text(text, x, y, fill="black"):
    my_text = turtle.Turtle()
    my_text.speed(0)
    my_text.penup()
    my_text.goto(x, y)
    my_text.color(fill)
    my_text.write(text, align='center', font=('Verdana', 20, 'normal'))
    my_text.hideturtle()
    
turtle.setup(800, 600)
turtle.onkey(game_exit, "Escape")
turtle.onkey(rocket_launch, "space")
turtle.listen()

window = turtle.Screen()
window.tracer(0)
window.title("Rio fireworks demo animation")
window.bgcolor("#13008D")

draw_text('Press SPACE to firework // Press ESC to close', 0, 250, '#FFFFFF')

animate()

while True:
    window.update()
