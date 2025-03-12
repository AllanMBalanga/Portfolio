from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        y = self.ycor() +20
        self.goto(self.xcor(),y)

    def down(self):
        y = self.ycor() -20
        self.goto(self.xcor(),y)




















