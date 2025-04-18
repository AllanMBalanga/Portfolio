from turtle import Turtle
x=[(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in x:
            self.add_snake(i)

    def add_snake(self, i):
        ekans = Turtle(shape="square")
        ekans.color("white")
        ekans.penup()
        ekans.goto(i)
        self.snake.append(ekans)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]


    def move(self):
        for snake_head in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_head - 1].xcor()
            new_y = self.snake[snake_head - 1].ycor()
            self.snake[snake_head].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

