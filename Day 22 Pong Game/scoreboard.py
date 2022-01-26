from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 240)
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-80, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(80, 220)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.update()

    def increase_l_score(self):
        self.l_score += 1
        self.update()
