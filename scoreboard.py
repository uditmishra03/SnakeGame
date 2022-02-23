from turtle import Turtle
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.high_score = 0
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()
