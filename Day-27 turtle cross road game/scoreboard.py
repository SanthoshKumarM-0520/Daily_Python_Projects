from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def gameover(self):
        self.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
    def turtle_crossed(self):
        self.write("TURTLE CROSSED", align="center", font=("Courier", 60, "normal"))
