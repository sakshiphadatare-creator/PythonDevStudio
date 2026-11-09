from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10    # -10
        self.sleep_up = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move   # Instead of write this we also write new_x = self.xcor() + 10 It's doesn't make sense both are same but writing methodology id different
        new_y = self.ycor() + self.y_move   # move Y co-ordinate - 10 Instead of + 10 because we have to set the bounce position * -10
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1    # 10 * -1 = -10

    def bounce_x(self):
        self.x_move *= -1    # reverse the collision
        self.sleep_up *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.sleep_up = 0.1
        self.bounce_x()

    def sleep_up(self):
        self.sleep_up += 0.1


 #     self.shapesize(stretch_wid=2, stretch_len=2)
    #     self.goto(0,0)
    # def go_right(self):
    #     self.setposition(350,260)
    #
    # def go_left(self):
    #     self.setposition(-350,250)