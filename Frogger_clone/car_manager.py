import random
from turtle import Turtle
import scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.move_speed = 0.1
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-280, 280), random.randint(-250, 260))
        self.car_list.append(self)

    def reset_start(self):
        self.goto(random.randint(260, 280), random.randint(-250, 260))

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            new_y = car.ycor()
            car.goto(new_x, new_y)
            if car.xcor() < -300:
                car.reset_start()

    def generate_cars(self):
        for number in range(10):
            new_car = CarManager()
            self.car_list.append(new_car)

    def increase_speed(self):
        self.move_speed *= 0.9
