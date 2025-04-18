from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.speed(0)
        self.food_pos()

    def food_pos(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)