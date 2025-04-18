from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("pingpong")
screen.tracer(0)

r_paddle = Paddle((350,0))
r_score = Score((100, 270))
l_paddle = Paddle((-350,0))
l_score = Score((-100,270))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_end = False
while not game_end:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        l_score.increase()
        ball.reset_position()

    elif ball.xcor() < -380:
        r_score.increase()
        ball.reset_position()

screen.exitonclick()

