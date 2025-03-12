from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("yaguding")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_end = False

while not game_end:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.food_pos()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280  or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        score.increase_score()

    for segment in snake.snake[1:]:  # Exclude the head
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()