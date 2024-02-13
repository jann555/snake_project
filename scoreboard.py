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
        self.high_score = None
        self.__read_high_score()
        self.refresh_score()

    def increase_score(self):
        self.points += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.points}  High score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            self.__save_high_score()
        self.points = 0
        self.refresh_score()

    def __save_high_score(self):
        with open('high_scores.txt', mode='w', encoding="utf-8") as file:
            file.write(f'{self.high_score}')

    def __read_high_score(self):
        with open('high_scores.txt', mode='r', encoding="utf-8") as file:
            file.readable()
            score = int(file.read(1)) if file.readable() else 0
            self.high_score = score

