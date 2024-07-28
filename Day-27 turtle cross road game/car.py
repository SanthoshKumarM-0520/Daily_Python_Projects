import random
from turtle import Turtle

class Car:
    def __init__(self):
        self.all_cars=[]
        self.colors = ["red", "yellow", "blue", "orange", "green", "brown", "pink"]
        self.level=6



    def create_car(self):
        random_number=random.randint(1,self.level)
        if random_number == 1:

            new_car=Turtle("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_color=random.choice(self.colors)
            new_car.color(random_color)
            random_y=random.randint(-240,240)
            new_car.goto(290,random_y)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(20)










