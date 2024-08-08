from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

data = pandas.read_csv("french_words.csv")
to_dict = data.to_dict(orient="records")

def next_card():
    global random_english, timer, random_dic
    window.after_cancel(timer)

    random_dic = random.choice(to_dict)
    random_french = random_dic["French"]
    random_english = random_dic["English"]
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=random_french)

    canvas.itemconfig(back_card, image=front_image)
    canvas.itemconfig(language, text="French", fill=BLACK_COLOR)
    canvas.itemconfig(word, text=random_french, fill=BLACK_COLOR)

    timer = window.after(3000, change)

def change():
    canvas.itemconfig(back_card, image=back_image)
    canvas.itemconfig(language, text="English", fill=WHITE_COLOR)
    canvas.itemconfig(word, text=random_english, fill=WHITE_COLOR)

def is_know():
    to_dict.remove(random_dic)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, change)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
back_card = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
correct_image = PhotoImage(file="right.png")
correct_button = Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_know)
correct_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



