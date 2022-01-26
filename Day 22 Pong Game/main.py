from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
scoreboard = Scoreboard()
ball = Ball()

middle_line = Turtle()
middle_line.pencolor("white")
middle_line.penup()
middle_line.goto(0, -400)
for _ in range(1, 21):
    middle_line.pendown()
    middle_line.goto(0, middle_line.ycor() + 20)
    middle_line.penup()
    middle_line.goto(0, middle_line.ycor() + 20)

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True

while game_on:
    time.sleep(ball.motion_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 330 and ball.distance(r_paddle) < 50) or (ball.xcor() < -330 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 350:
        scoreboard.increase_l_score()
        ball.reset()
    if ball.xcor() < -350:
        scoreboard.increase_r_score()
        ball.reset()

# TODO: 3. Create a ball = Class
# TODO: 4. Create two scoreboards = Class
# TODO: 5. Make ball bouncing rules (screen and paddles)
screen.exitonclick()
