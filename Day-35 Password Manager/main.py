import tkinter
from random_password import Random_password
from tkinter import messagebox
from tkinter import END
import json

rp=Random_password()

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)
s=password_entry.insert(0, "")

def save_datas():
    input_website=website_entry.get()
    input_email=email_entry.get()
    input_password=password_entry.get()
    input_dic={
        input_website:{
            "email":input_email,
            "password":input_password
        }
    }

    with open("all_details.json", mode="r") as reader:
        checker = json.load(reader)
    if input_website in checker:
        conformation=messagebox.askokcancel(title="Confirm Overwrite",message=f"The data for '{input_website}' already exists. Do you want to overwrite it?")
        if conformation:
            with open("all_details.json", mode="r") as reader:
                checker1 = json.load(reader)
                checker1[input_website]["email"]=input_email
                checker1[input_website]["password"] = input_password
                checker1.update(checker1)
            with open("all_details.json", mode="w")as rd:
                json.dump(checker1,rd)
    if len(input_website)==0 or len(input_password)==0:
        messagebox.showinfo(title="Oops",message="please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=input_website,
                                       message=f"These are the details entered:\nEmail:{input_email} \nPassword:{input_password}\nIs it ok to save this detail?")

        if is_ok:

            try:
                with open("all_details.json", mode="r") as reader:
                    a = json.load(reader)
                    a.update(input_dic)
            except:
                with open("all_details.json","w",)as detail:
                    json.dump(input_dic,detail,indent=4)
            else:
                with open("all_details.json",mode="w")as detail:
                    json.dump(a, detail,indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
def call_password():

    password_entry.delete(0,END,)
    password_entry.insert(0, f"{rp.rand_pass()}")

def search():
    a = website_entry.get()
    try:
        with open("all_details.json") as reader1:
            b = json.load(reader1)
            tkinter.messagebox.showinfo(title=a, message=f"Email:{b[a]["email"]}\nPassword:{b[a]["password"]}")
    except KeyError:
        tkinter.messagebox.showinfo(title="Oops", message=f"Sorry, no data found for your search.")

# Buttons
generate_password_button = tkinter.Button(text="Generate Password",command=call_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36,command=save_datas)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search",width=15,command=search)
search_button.grid(row=1, column=2)

window.mainloop()