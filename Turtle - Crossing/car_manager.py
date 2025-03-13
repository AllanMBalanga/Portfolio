from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE # List to hold all car objects

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch to make it look like a car
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y = random.randint(-250,250)
            new_car.goto(300, y)  # Start at the right edge
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars to the left."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increment(self):
        self.car_speed += MOVE_INCREMENT

