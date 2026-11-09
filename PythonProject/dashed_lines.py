import turtle as t
tim = t.Turtle()
for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.pen(fillcolor = "red")
    tim.forward(10)
    tim.pendown()


screen = t.Screen()
screen.exitonclick()