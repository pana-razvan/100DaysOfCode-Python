from turtle import Turtle
from random import choice


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("crimson", "yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = choice(range(-280, 280)[::20])
        random_y = choice(range(-280, 280)[::20])
        self.goto(random_x, random_y)
