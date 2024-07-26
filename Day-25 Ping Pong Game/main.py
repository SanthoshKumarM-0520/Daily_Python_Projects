import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


ball=Ball()



scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

speed=0.035

game_on=True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()
        speed -= 0.005


    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        speed -= 0.005



    if ball.xcor() > 340:
        ball.recenter()
        scoreboard.l_point()
        speed = 0.035

    if ball.xcor() < -340:
        ball.recenter()
        scoreboard.r_point()
        speed = 0.035

screen.exitonclick()
