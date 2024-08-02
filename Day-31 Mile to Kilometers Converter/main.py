import tkinter


window=tkinter.Tk()
window.title("Mile to KM")
window.minsize(width=300,height=300)
window.config(padx=10,pady=10)



label_wel=tkinter.Label(text="WELCOME",font=("Arial",15,"bold"))
label_wel.grid(column=2,row=0)


label_mile=tkinter.Label(text="Enter the Mile",font=("Arial",10,"bold"))
label_mile.grid(column=1,row=1)

entry_mile=tkinter.Entry(width=10)
entry_mile.grid(column=2,row=1)

label_isequal=tkinter.Label(text="is equal to",font=("Arial",10,"bold"))
label_isequal.grid(column=1,row=3)

label_ans=tkinter.Label(text="0",font=("Arial",10,"bold"))
label_ans.grid(column=2,row=3)

label_km=tkinter.Label(text="Km",font=("Arial",10,"bold"))
label_km.grid(column=3,row=3)


def calculate():
    mile=int(entry_mile.get())
    ans=(mile*1.60934)
    label_ans.config(text=ans)

button=tkinter.Button(text="Calculate",command=calculate)
button.grid(column=2,row=4)

window.mainloop()