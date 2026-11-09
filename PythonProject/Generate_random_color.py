import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255) # not write tim.colormode() that tim is the object, but we have to put actual turtle module.

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()