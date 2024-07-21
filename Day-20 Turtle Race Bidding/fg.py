from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Turtle Bidding",prompt="Enter the turtle color you need.")


colors=["red","black","blue","green","orange"]
position=[-70,-40,-10,20,50]

turtle_list=[]
for z in range (0,5):
    turt=Turtle(shape="turtle")
    turt.penup()
    turt.color(colors[z])
    turt.goto(x=-230,y=position[z])
    turtle_list.append(turt)
a=turtle_list[2]
print(a.pencolor())