from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-30, 280)
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.current_score} ", move=False, align="center", font=("Courier New", 12, "bold"))
