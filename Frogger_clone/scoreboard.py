from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
        self.color("black")

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()





