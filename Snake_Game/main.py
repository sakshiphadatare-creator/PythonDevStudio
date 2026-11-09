from turtle import Screen

import segment

from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 500, height=500)
screen.bgcolor("black")
screen.title("My Snake Game!")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


    # Delect collision with food
    if snake.head.distance(food) < 15:   #head is instance attribute of snake self.segments[0]
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()
        scoreboard.increase_result()

    # Delect collision with wall
    if snake.head.xcor() > 230 or snake.head.ycor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() < -230:
        game_is_on = False
        scoreboard.game_over()

    # Delect collision with tail      #######
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:

            game_is_on = False
            scoreboard.game_over()
    #if the head collides with any segment in the tail:
           # Trigger game_over



screen.exitonclick()



# square1 = Turtle("square")
# square1.color("white")
# square1.goto(-20,0)
# square1.penup()
#
# square2 = Turtle("square")
# square2.color("white")
# square2.goto(-40,0)
# square2.penup()