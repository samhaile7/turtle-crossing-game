import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True



cars = CarManager()

while game_is_on:
    cars.create_car()
    cars.move_left()
    if player.distance()

    time.sleep(0.1)
    screen.update()



screen.exitonclick()
