import turtle
from turtle import Screen,Turtle
import pandas



screen=Screen()
screen.title("U.S States Quiz")
image="blank_states_img.gif"
screen.addshape(image)
screen.tracer(10)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
list_states=list(data.state)
lowercase_states=[string.lower() for string in list_states]

user_inputs=[]
score=0

condition=True
while condition:
    screen.update()
    user_ans = screen.textinput(title=f"Score: {score}/50", prompt="Guess the state.!").lower()
    if user_ans =="exit":
        missed_stated = [states for states in lowercase_states if states not in user_inputs]
        missed_data = pandas.DataFrame(missed_stated)
        missed_data.to_csv("missed_states")
        break
    if user_ans in lowercase_states:
        if user_ans not in user_inputs:

            user_inputs.append(user_ans)
            score+=1

            form_data=user_ans.title()

            row_state = data[data.state == form_data]
            x = row_state.x.item()
            y = row_state.y.item()

            tim = Turtle()
            tim.penup()
            tim.hideturtle()
            tim.goto(x, y)
            tim.color("green")
            tim.write(arg=f"{form_data}", align='center', font=("courier", 9, "bold"))

            if score == 50:
                condition=False
                tim.goto(0,0)
                tim.color("blue")
                tim.write(arg="Well done!", align='center', font=("courier", 15, "bold"))
                screen.exitonclick()

