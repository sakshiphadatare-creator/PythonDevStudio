from turtle import Turtle, Screen

tim = Turtle()

def forward_move():
    tim.forward(10)
screen = Screen()
screen.listen()
screen.onkey(key="space", fun=forward_move)
screen.exitonclick()