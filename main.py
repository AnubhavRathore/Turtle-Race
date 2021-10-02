import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(fun=player.go_up, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player.is_at_finish_line():
        player.restart()
        car_manager.cross()
        scoreboard.score()

    """My own method if turtle crosses finish line"""
    # if player.ycor() >= 280:
    #     player.restart()
    #     car_manager.cross()
    #     scoreboard.score()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    car_manager.create_car()
    car_manager.move()
    screen.update()

screen.exitonclick()
