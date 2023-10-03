import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.is_winnable():
        turtle.go_to_start()
        scoreboard.update_level()
        car_manager.update_car_speed()

screen.exitonclick()
