import turtle
from turtle import Turtle,Screen
import json

screen=Screen()
screen.title("India Map")
screen.setup(width=600,height=600)
tn_image="map.gif"
screen.addshape(tn_image)
turtle.shape(tn_image)

count=0
#to take x & y from the Map
'''def find_xy(x, y):
    global count
    count+=1
    district=tamil_nadu_districts[count-1]
    dic_dis={
        district:{"xaxis":x,"yaxis":y}
    }
    print(dic_dis)
    try:
        with open("Disxy.json",mode="r")as reader:
            r=json.load(reader)
            r.update(dic_dis)
    except:

        with open("Disxy.json",mode="w")as writer1:
            json.dump(dic_dis,writer1,indent=4)
    else:

        with open("Disxy.json",mode="w")as writer2:
            json.dump(r,writer2,indent=4)

screen.onscreenclick(find_xy)'''

tim=Turtle()
tim.penup()
tim.hideturtle()
tim.speed(0)

try:
    with open("to_learn.json")as reader1:
        r=json.load(reader1)
except FileNotFoundError:
    check_list=[
    "Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri",
    "Dindigul", "Erode", "Kallakurichi", "Kanchipuram", "Kanyakumari", "Karur",
    "Krishnagiri", "Madurai", "Mayiladuthurai", "Nagapattinam", "Namakkal", "Nilgiris",
    "Perambalur", "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem", "Sivaganga",
    "Tenkasi", "Thanjavur", "Theni", "Thiruvallur", "Thiruvarur", "Thoothukudi",
    "Tiruchirappalli", "Tirunelveli", "Tirupattur", "Tiruppur", "Tiruvannamalai", "Vellore",
    "Viluppuram", "Virudhunagar"
]
else:
    check_list = r["remaining_districts"]
    print(len(check_list))

try:
    with open("score.txt",mode="r")as score_reader:
        score=int(score_reader.read())
except:
    score = 0

user_inputs=[]
while True:

    if score == 38:
        tim.color("blue")
        tim.goto(-150, 0)
        tim.write("YOU WIN", font=("courier", 40, "bold"))
        break

    user_ans = screen.textinput(title=f"Score: {score}/38", prompt="Guess the district.!").title()

    if user_ans == "Exit":
        break
    else:
        try:
            check_list.remove(user_ans)
            score += 1
            with open("Disxy.json") as reader:
                a = json.load(reader)
                x_axis = a[user_ans]['xaxis']
                y_axis = a[user_ans]['yaxis']
                tim.goto(x=x_axis, y=y_axis)
                tim.write(f"{user_ans}")
            remaining_districts = {"remaining_districts": check_list}
            try:
                with open("to_learn.json", mode="r") as rlc:
                    f = json.load(rlc)
                    f.update(remaining_districts)
            except:
                with open("to_learn.json", mode="w") as writter1:
                    json.dump(remaining_districts, writter1, indent=2)
                with open("score.txt","w")as score_data1:
                    score_data1.write(str(score))
            else:
                with open("to_learn.json", mode="w") as writter2:
                    json.dump(f, writter2, indent=2)
                with open("score.txt", "w") as score_data2:
                    score_data2.write(str(score))
        except ValueError:
            pass

screen.exitonclick()






