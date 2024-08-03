import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
tick = "✓"
timer=None

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label_time.config(text="Timer")
    tick_symbol.config(text="")

def start_timer():
    global rep
    rep+=1

    if rep == 1 or rep == 3 or rep == 5 or rep == 7:
        count_down(count=25 * 60)
        label_time.config(text="Work",fg=GREEN)
    elif rep == 2 or rep == 4 or rep == 6:
        count_down(count=5 * 60)
        label_time.config(text="Small Break",fg=PINK)
    else:
        count_down(count=20 * 60)
        label_time.config(text="Long Break",fg=PINK)


def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec <10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        global tick
        if rep == 1 or rep == 3 or rep == 5 or rep == 7:
            tick_symbol.config(text=tick)
            tick += "✓"
        start_timer()






window=tkinter.Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)




label_time=tkinter.Label(text="Timer",bg=YELLOW,font=(FONT_NAME,25,"bold"),fg=GREEN)
label_time.grid(column=2,row=0)


canvas=tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=1)




start_button=tkinter.Button(text="Start",command=start_timer)
start_button.grid(column=0,row=5)

reset_button=tkinter.Button(text="Reset",command=reset)
reset_button.grid(column=3,row=5)


tick_symbol=tkinter.Label(fg=GREEN,bg=YELLOW)
tick_symbol.grid(column=2,row=6)



window.mainloop()

