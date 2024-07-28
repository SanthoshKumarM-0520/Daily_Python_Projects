from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
        self.goto(-200,250)
        self.Scoreboard()
    def Scoreboard(self):
        self.write(arg=f"LEVEL : {self.score} / 5 ", align='center',font=("Courier", 15, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
    def score_increase(self):
        self.clear()
        self.score += 1
        self.Scoreboard()
    def lose(self):
        self.color("blue")
        self.goto(10,-50)
        self.write(arg=f"Oops! You hit a car at {self.score}th level ", align='center', font=("Courier", 15, "normal"))
    def win(self):
        self.color("green")
        self.goto(0,0)
        self.write("YOU WIN", align="center", font=("Courier", 50, "normal"))



