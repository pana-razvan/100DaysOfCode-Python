import turtle as t
import random

import colorgram

colours = colorgram.extract("image.jpg", 30)
rgb_colours = []

for item in colours:
    rgb_colours.append(tuple(item.rgb))

with open("colors.txt", "w") as file:
    for item in rgb_colours:
        file.write(f"{str(item)}\n")

t.colormode(255)
screen = t.Screen()
jim = t.Turtle()
jim.hideturtle()
jim.penup()
jim.speed(0)

dot_canvas_size = 10
dot_gap = 50
dot_size = 25

jim.setposition(- dot_canvas_size*dot_gap / 2, - dot_canvas_size*dot_gap / 2)

for dot_count in range(1, dot_canvas_size*dot_canvas_size+1):
    jim.dot(dot_size, random.choice(rgb_colours))
    jim.forward(dot_gap)
    if dot_count % dot_canvas_size == 0:
        jim.left(90)
        jim.forward(dot_gap)
        jim.left(90)
        jim.forward(dot_gap * dot_canvas_size)
        jim.setheading(0)

screen.exitonclick()
