import turtle
from random import randint

from projectiles.rocket import Rocket


objects = []

def rocket_launch():
    global objects
    rocket = Rocket(objects)

def game_exit():
    turtle.bye()
    
def kill_turtle(obj):
    objects.remove(obj)
    obj.clear()
    obj.ht()
    del obj
            
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
