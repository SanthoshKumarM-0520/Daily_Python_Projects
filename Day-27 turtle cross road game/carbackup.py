from turtle import Turtle

class CarBack(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")
        self.setheading(180)
        self.goto(280,-240)
    def carBack_move(self):
        self.forward(10)

