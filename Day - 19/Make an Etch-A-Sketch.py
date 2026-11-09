from turtle import Turtle, Screen

tim = Turtle()
def forward_move():
    tim.forward(10)
def backward_move():
    tim.backward(10)
def left_move():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def right_move():
    new_heading = tim.heading() - 10     # tim.left(10)
    tim.setheading(new_heading)

def clear():
    tim.clear()  # clear the screen
    tim.penup()   # It's means don't write
    tim.home()   # coming to the original position
    tim.pendown() # To write

screen = Screen()
screen.listen()   # Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to pass listen() to the onclick method.
                   # turtle.onkey(fun, key) # turtle.onkeyrelease(fun, key) # Parameters: # fun – a function with no arguments or None # key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
screen.onkey(key="w", fun=forward_move)
screen.onkey(key="s", fun=backward_move)
screen.onkey(key="a", fun=left_move)
screen.onkey(key="d", fun=right_move)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

# from turtle import Turtle, Screen
#
# tim = Turtle()
# def forward_move():
#     tim.forward(10)
# def backward_move():
#     tim.backward(10)
# def counter_circle():
#     tim.left(10)
#     # this works same as above expression
#     # new_heading = tim.heading() + 10
#     # tim.setheading(new_heading)
#
# def clockwise():
#     tim.right(10)
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen = Screen()
# screen.listen()
# screen.onkey(key="w" , fun=forward_move)
# screen.onkey(key="s" , fun=backward_move)
# screen.onkey(key="a" , fun=counter_circle)
# screen.onkey(key="d" ,fun=clockwise)
# screen.onkey(key="c" , fun=clear_drawing)
# screen.exitonclick()