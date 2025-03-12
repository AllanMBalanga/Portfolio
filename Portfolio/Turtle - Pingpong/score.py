from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

