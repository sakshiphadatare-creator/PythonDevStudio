# from module import class
from turtle import Turtle
import random
class Food(Turtle):
    # Call the turtle class then initializes food shape, color, size & refresh
    def __init__(self):
        super().__init__()   # No put inside anything, we just initialize the super class
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    # Move the food at a randon location
    def refresh(self):
        x_random = random.randint(-230, 230)  # x_random is for horizontal (left-right) position. [ width= 10 and length = 10   10+10 = 20
        y_random = random.randint(-230,230)  # y_random is for vertical (up-down) position.       250 - 20 = 230  setup = 500  x-axis (positive and negative each )= 250 and y-axis = 250 ]
        self.goto(x_random, y_random)


