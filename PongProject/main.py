""" The first step of creating any large project is to break down the problem into smaller, bite-sized chunks.
Add the following comments to the starting code and try to tackle them one-by-one."""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#TODO:1 Create a screen with title, color and setup(size)
screen = Screen ()
screen.title("pong ")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)                                           # (td-3)  which Controls the animation, you have to manually update the screen and refresh it every single time. we'll need same sort of a while loop

#TODO:2 Create the paddle that response to key presses
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
# top_paddle = Paddle((100,100))                            # How to create the another paddle in the existing code

#TODO-3 Create the Ball class and make the ball move
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")                  # As you write function as a parameter, only write function_name whatever it is NOT write () sign.
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "w")


game_is_on = True
while game_is_on:
    time.sleep(ball.sleep_up)                                            # time module and sleep function (Don't write speed)
    screen.update()                                            # we use tracer() then we have to update every single time.
    ball.move()

    # TODO-4 Delect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #TODO-5 Delect the of r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() < 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Delect R paddle is misses
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    #  Delect L paddle is misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()








# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)   # stretch_wid is a height and stretch_len is a length
# paddle.penup()
# paddle.goto(350,0 )
#
#
# def paddle_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(350, new_y)
#
# def paddle_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(350,new_y)

# These lines are not bounce by both the sides (right & left)
# if ball.xcor() < -370 or ball.xcor() > 370:
#     ball.bounce_x()
