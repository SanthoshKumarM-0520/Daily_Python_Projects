from turtle import Screen
from player import Player
from car import Car
import time
from score import score

screen=Screen()
screen.setup(width=600,height=600)
screen.listen()
screen.tracer(10)


player=Player()

car=Car()

scoreboard=score()

screen.onkey(player.turtle_move,"Up")


speed=0.045

game_on=True
while game_on:
    screen.update()
    time.sleep(speed)
    car.create_car()
    car.move()
    for z in car.all_cars:
        if player.distance(z)<20:
            scoreboard.game_over()
            scoreboard.lose()
            game_on=False
    if player.ycor()>=290:
        player.turtle_recenter()
        scoreboard.score_increase()
        car.level -= 1
        speed -= 0.010
    if scoreboard.score == 5:
        scoreboard.win()
        game_on=False


screen.exitonclick()