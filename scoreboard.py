from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.score()

    def score(self):
        self.clear()
        self.write(arg=f"Level: {self.new_score}", move=False, align="left", font=FONT)
        self.new_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAMEOVER", move=False, align="center", font=("Arial", 20, "normal"))

