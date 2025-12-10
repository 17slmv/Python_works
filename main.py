from turtle import *
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.cars_move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.is_at_finish():
        player.go_start()
        cars.level_up()
        score.increase_level()

exitonclick()