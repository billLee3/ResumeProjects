import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()
car_manager.generate_cars()

# car_manager.move()

screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True

while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.move()

    if player.ycor() >= 280:
        scoreboard.level_up()
        player.reset_position()
        car_manager.increase_speed()

    for car in car_manager.car_list:
        if car.distance(player) <= 20:
            player.reset_position()
#     contact with car via the distance function



