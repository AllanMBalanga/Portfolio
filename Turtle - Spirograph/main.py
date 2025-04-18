import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def spirograph(degree):
    for i in range(int(360/degree)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + degree)

spirograph(3.6)

screen = Screen()
screen.exitonclick()