from tkinter import *
from turtle import *
import pandas
import random

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
start = 1
clock = None

current_card = {}
text = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("filipino_words.csv")
    text = original_data.to_dict(orient="records")
else:
    text = data.to_dict(orient="records")

def next_card():
    global current_card, timer
    window.after_cancel(timer)     #cancels yung naka schedule na timer bago matawag si new_card, then gumawa ng bagong timer para maging current timer
    current_card = random.choice(text)
    canvas.itemconfig(canvas_image,image=old_image)
    canvas.itemconfig(title, text="Filipino",fill="black")
    canvas.itemconfig(word, text=current_card["Filipino"],fill="black")
    timer = window.after(3000, flip_card)

def correct_button():
    text.remove(current_card)
    new_data = pandas.DataFrame(text)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")

window = Tk()
window.title("Translate")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer = window.after(3000, flip_card)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400,263)

title =canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
word = canvas.create_text(400,263,text="", font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0,command=correct_button)
right_button.grid(row=1,column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

next_card()

window.mainloop()

