from turtle import Turtle,Screen, distance
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

player =  Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finished_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_score()

    



