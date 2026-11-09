import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(2)     # optional
t.colormode(255)   # this is mode so we have to write module alignment

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(150)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.speed("fastest")
# t.colormode(255)   # this is mode so we have to write module alignment
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors
#
# for _ in range(100):
#     tim.circle(150)
#     tim.color(random_color())
#     current = tim.heading()
#     tim.setheading(current + 5)
#
#
# screen = t.Screen()
# screen.exitonclick()