import turtle
import random
tim = turtle.Turtle()
colors = ["red", "purple", "NavyBlue", "HotPink", "grey", "PowderBlue", "Green", "LightSeaGreen","SlateBlue1", "SlateGray1"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(directions))



screen = turtle.Screen()
screen.exitonclick()

# import turtle as t
# import random as rnd
# tim = t.Turtle()
# tim.pensize(20)
# tim.speed(int(input("Enter the speed of the turtle between 0 and 10:")))  # Instead of getting input only we write this words "normal", " fast and so on
# # tim.shapesize(5)   # this is used by expand the arrow (shape) size.we use this also (tim.turtlesize(5))
# colors = ["medium aquamarine", "IndianRed", "DarkOrchid", "DeepSkyBlue", "purple", "SeaGreen", "LightSeaGreen","pink", "blue"]
#
# directions = [0, 90, 180, 270]
# for _ in range(150):
#     tim.color(rnd.choice(colors))
#     tim.forward(50)
#     tim.setheading(rnd.choice(directions))



