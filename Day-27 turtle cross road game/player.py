from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
    def turtle_move(self):
        self.forward(30)
    def turtle_recenter(self):
        self.goto(0,-280)
