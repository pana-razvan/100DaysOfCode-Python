import random
from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS_START_RANGE_Y = range(-250, 250)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=0.8, stretch_len=2)
            car.goto(300, choice(CARS_START_RANGE_Y[::20]))
# check for the new car if is on the same lane as any of the existing cars and move it further if it overlaps
            for turtle in self.cars:
                while turtle.ycor() == car.ycor() and car.xcor() - turtle.xcor() < 80:
                    car.goto(car.xcor()+80, car.ycor())
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
