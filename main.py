# Detect if turtle and car are colliding
# Keep track of levels
# End game when turtle collides with car
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen and animation time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player's turtle
player = Player()

# Initialize car manager
car_manager = CarManager()

# Initialize scoreboard
scoreboard = Scoreboard()

# Check for player movement
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Start generating/moving cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect if player reaches goal area and increase car speed after
    if player.is_at_finish():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Detect if player collides with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
