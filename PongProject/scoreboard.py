from turtle import Turtle

#TODO -6 Score keeping and changing the ball speed.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()      # Hide the turtle means hide the shape
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="center", font=('courier', 80, 'normal'))
        self.goto(50, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()