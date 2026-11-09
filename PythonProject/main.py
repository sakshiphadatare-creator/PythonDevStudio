from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("black")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(100)

#Create a square
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)

# different way to import module as shown in below:
# import turtle
# tim = turtle.Turtle()
#
# from turtle import Turtle
# tim2 = Turtle()
#
# from turtle import *
# tim3 = Turtle()
#
# import turtle as timmy
# timmy = timmy.Turtle()
# timmy.shape("turtle")
# timmy.color("red")

# import random as rnd
# choice = rnd.randint(0,10)
# print(choice)








screen = Screen()
screen.exitonclick()

