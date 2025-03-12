from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        """ data.txt starts at 0, which is now equal to self,high_score"""
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move= False, align=ALIGN, font=FONT)
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            """writes the current high_score sa data.txt na magiging equivalent later 
            ni self.high_score kapag ni-run uli yung game"""

            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.increase_score()








