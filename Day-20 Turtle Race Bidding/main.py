from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Turtle Bidding",prompt="Enter the turtle color you need.")


colors=["red","black","blue","green","orange"]
position=[-70,-40,-10,20,50]
all_turtle=[]
for turle_index in range(0,5):
    turlez=Turtle(shape="turtle")
    turlez.color(colors[turle_index])
    turlez.penup()

    turlez.goto(x=-230,y=position[turle_index])
    all_turtle.append(turlez)






race_on=False
if user_bet:
    race_on=True



while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>220\
                :
            race_on=False
            turtle_color=turtle.pencolor()
            if turtle_color == user_bet:
                print(f"YOU WIN , {turtle_color} turtle win the race")
            else:
                print(f"YOU LOSE , {turtle_color} turtle win the race")


        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()