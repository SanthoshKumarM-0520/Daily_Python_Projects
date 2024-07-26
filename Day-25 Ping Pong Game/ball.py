from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()

        self.x_cor=10
        self.y_cor = 10

    def move(self):

        x_cor=self.xcor()+self.x_cor
        y_cor = self.ycor() + self.y_cor
        self.goto(x_cor,y_cor)
    def wall_bounce(self):
        self.y_cor *= -1
    def paddle_bounce(self):
        self.x_cor *= -1
        self.move()
    def recenter(self):
        self.goto(0,0)
        self.paddle_bounce()

















