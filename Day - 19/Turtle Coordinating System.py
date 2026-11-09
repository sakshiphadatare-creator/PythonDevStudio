from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.bgcolor("yellow")
screen.setup(width=500, height=400)    # Set the size and position of the main window
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle do you want to move?") #  take input from user

colors =["red", "purple", "NavyBlue", "HotPink", "grey", "PowderBlue", "Green" ,"SlateBlue1", "SlateGray1"]
y_list = [-70, -40, -10, 20, 80, 50]    # refer to graph page
all_turtles = []

for turtle_index in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230 , y= y_list[turtle_index])     # Positions of the turtle
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:     #Return the turtle’s x coordinate.     # 250 - (40/2) = 230
            is_race_on = False                                             #  250 - 20 = 230
            winning_turtle = turtle.pencolor()      #Return or set pencolor and fillcolor. we write only turtle.color() is this way return us two parameter i.e pencolor and fillcolor
            if winning_turtle == user_bet:
                print("You Win!!")
            else:
                print(f"You Lose!!, The {winning_turtle} turtle is the winner.")

        random_distance = (random.randint(0,10))
        turtle.forward(random_distance)

screen.title("Turtle Coordinating System")
screen.bgcolor("LightPink")

screen.exitonclick()