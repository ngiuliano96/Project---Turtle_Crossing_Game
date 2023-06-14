import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "blue", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.setpos(340, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            if car.xcor() > -340:
                car.forward(self.car_speed)
            else:
                self.all_cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
