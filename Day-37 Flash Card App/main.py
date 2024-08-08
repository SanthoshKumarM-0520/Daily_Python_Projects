from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR="#FFFFFF"
BLACK_COLOR="#000000"


to_learn=0

def next_card():

    global random_english , timer
    global random_dic
    global to_learn
    window.after_cancel(timer)

    try:
        data2 = pandas.read_csv("word_to_learn")
    except:
        data = pandas.read_csv("french_words.csv")
        to_learn = data.to_dict(orient="records")
    else:
        to_learn = data2.to_dict(orient="records")
    random_dic=random.choice(to_learn)
    random_french = (random_dic["French"])
    random_english = (random_dic["English"])
    canvas.itemconfig(language,text="French")
    canvas.itemconfig(word,text=random_french)

    canvas.itemconfig(back_card, image=front_image)
    canvas.itemconfig(language, text="French", fill=BLACK_COLOR)
    canvas.itemconfig(word, text=random_french, fill=BLACK_COLOR)

    timer=window.after(3000, change)

def change():
    canvas.itemconfig(back_card,image=back_image)
    canvas.itemconfig(language, text="English",fill=WHITE_COLOR)
    canvas.itemconfig(word, text=random_english,fill=WHITE_COLOR)

def is_know():
    global to_learn
    to_learn.remove(random_dic)
    word_to_learn=pandas.DataFrame(to_learn)
    word_to_learn.to_csv("word_to_learn",index=False)
    next_card()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer=window.after(3000,change)


#canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image=PhotoImage(file="card_front.png")
back_image=PhotoImage(file="card_back.png")
back_card=canvas.create_image(400,263,image=front_image)
language=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
correct_image=PhotoImage(file="right.png",)
correct_button=Button(image=correct_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_know)
correct_button.grid(column=0,row=1)


wrong_image=PhotoImage(file="wrong.png",)
wrong_button=Button(image=wrong_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
wrong_button.grid(column=1,row=1)

next_card()

window.mainloop()
