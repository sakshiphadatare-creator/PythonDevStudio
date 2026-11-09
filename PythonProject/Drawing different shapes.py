import turtle as t
import random as rnd
tim = t.Turtle()
colors = ["medium aquamarine", "IndianRed", "DarkOrchid", "DeepSkyBlue", "Wheat", "SeaGreen", "SlateBlue1", "SlateGray1"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for num_of_shape in range(3,11):
    tim.color(rnd.choice(colors))
    draw_shape(num_of_shape)


screen = t.Screen()
screen.exitonclick()
