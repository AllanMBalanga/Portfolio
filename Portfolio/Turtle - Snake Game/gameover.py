from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("Game Over", align=ALIGN, font=FONT)
