from turtle import Turtle
# Constant written in capital letter
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):   # insides the parathesis we write class_name and class_name first letter should be capitalized.
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()   # Hide the screen line

    def update_scoreboard(self):
        self.goto(0, 226)
        self.write(f"Score: {self.scoreboard} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_result(self):
        self.scoreboard += 1
        self.clear()
        self.update_scoreboard()




