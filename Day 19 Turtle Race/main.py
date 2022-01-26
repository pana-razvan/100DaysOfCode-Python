import turtle
from turtle import Turtle, Screen
from random import randint

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a colour: ")
winning_color = ""
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = 130
all_turtles = []

for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos)
    y_pos -= 50
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_on = False
            if winning_color == user_bet:
                print(f"Congratulations! You've won. The {winning_color} turtle won the race.")
            else:
                print(f"Sorry. You lost! The {winning_color} turtle won the race :(")
        rand_dist = randint(0, 5)
        turtle.forward(rand_dist)

screen.exitonclick()
