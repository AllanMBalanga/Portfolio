import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        car.increment()
        score.increase()

    for i in car.all_cars:
        if i.distance(player) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()