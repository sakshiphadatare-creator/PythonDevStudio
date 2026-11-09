from turtle import Turtle
#from module import class
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add the segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):  # call to this method by class object through
        for seg_num in range(len(self.segments) - 1, 0, -1):  # list starts from 0 and end element is -1    # 3,0,-1
            new_x = self.segments[seg_num - 1].xcor()  # X coordinates = list[3-1=2].x
            new_y = self.segments[seg_num - 1].ycor()  # Y coordinates = list[3-1=2].y
            self.segments[seg_num].goto(new_x, new_y)  # list[3] goto the [list[2],list[2]] 
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



