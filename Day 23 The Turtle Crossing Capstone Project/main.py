import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move_up, "Up")
scoreboard = Scoreboard()
car_manager = CarManager()

once = True

game_is_on = True
while game_is_on:
    while once:
        for n in range(110):
            car_manager.new_car()
            car_manager.move_cars()
            screen.update()
        once = False
    screen.update()
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move_cars()

    if player.is_at_finish_line():
        scoreboard.level_up()
        car_manager.level_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
