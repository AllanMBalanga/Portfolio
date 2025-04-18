from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-200,250)
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=FONT)



