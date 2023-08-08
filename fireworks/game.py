import turtle

from projectiles.rocket import Rocket


class Game:

    def __init__(self):
        self.objects = list()

        turtle.setup(800, 600)
        turtle.onkey(self.exit, "Escape")
        turtle.onkey(self.rocket_launch, "space")
        turtle.listen()

        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.title("Rio fireworks demo animation")
        self.window.bgcolor("#13008D")

        self.draw_text('Press SPACE to firework // Press ESC to close', 0, 250, '#FFFFFF')

    def draw_text(self, text, x, y, fill="black"):
        my_text = turtle.Turtle()
        my_text.speed(0)
        my_text.penup()
        my_text.goto(x, y)
        my_text.color(fill)
        my_text.write(text, align='center', font=('Verdana', 20, 'normal'))
        my_text.hideturtle()

    def animate(self):
        if len(self.objects) > 0:
            for obj in self.objects:
                obj.setx(obj.xcor() + obj.x_speed)
                obj.sety(obj.ycor() + obj.y_speed)
                obj.y_speed += obj.y_acceleration
                obj.update()
        self.window.ontimer(self.animate, 20)

    def run(self):
        self.animate()
        while True:
            self.window.update()

    def rocket_launch(self):
        rocket = Rocket(self.objects)

    def exit(self):
        turtle.bye()
