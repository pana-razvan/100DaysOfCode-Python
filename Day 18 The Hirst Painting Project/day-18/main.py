# Turtle Intro
import random
import turtle as t
from random import choice


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
tim.hideturtle()
t.colormode(255)

# Challenge 1 - Draw a Square
for i in range(4):
    tim.forward(100)
    tim.left(360 / 4)

# Challenge 2 - Draw a Dashed Line
for i in range(50):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

# Challenge 3 - Drawing Different Shapes
color_list=["red", "blue", "dark green", "pink", "crimson", "brown", "navy blue", "light blue", "light pink", "grey"]
for sides in range(3, 11):
    tim.pencolor(random.choice(color_list))
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)

# Challenge 4 - Generate a Random Walk
tim.pensize(15)
tim.speed("fastest")
for _ in range(150):
    tim.setheading(random.choice([0, 90, 180, 270]))
    tim.pencolor(random_colour())
    tim.forward(30)

# Challenge 5 - Draw a Spirograph
tim.speed(0)
screen = t.Screen()


def draw_spirograph(no_of_circles):
    for _ in range(no_of_circles):
        tim.pencolor(random_colour())
        tim.circle(100)
        tim.left(360 / no_of_circles)


draw_spirograph(50)
screen.exitonclick()
