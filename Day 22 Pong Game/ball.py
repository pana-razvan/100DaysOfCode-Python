from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white", "crimson")
        self.penup()
        self.x_motion = 10
        self.y_motion = 10
        self.motion_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_motion
        new_y = self.ycor() + self.y_motion
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_motion = -self.y_motion

    def bounce_x(self):
        self.x_motion = -self.x_motion
        self.motion_speed *= 0.95

    def reset(self):
        self.home()
        self.motion_speed = 0.1
        self.bounce_x()
