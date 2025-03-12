import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user = screen.textinput("Make your bet","Enter a color (R/O/Y/G/B/I/V): ")
colors = ["red","orange","yellow","green","blue","indigo","violet"]
y = [-60,-40,-20,-0,20,40,60]
turtles = []
game_end = False

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y[i])
    turtles.append(new_turtle)

while not game_end:
    for i in turtles:
        if i.xcor() > 200:
            winner = i.pencolor()
            if winner == user:
                print(f"You won! The winner of the race is {winner}")
            else:
                print(f"You lost! The winner of the race is {winner}")
            game_end = True

        distance = random.randint(0,10)
        i.forward(distance)

screen.exitonclick()

