from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.points = 0
        self.refresh_score()

    def increase_score(self):
        self.clear()
        self.points += 1
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score: {self.points} ", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=FONT, align=ALIGNMENT)
