
from tkinter import *
from turtle import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
clock_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(clock_timer)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    timer.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps == 9:
        reps = reps - 9

    work_sec = WORK_MIN*60
    short_sec = SHORT_BREAK_MIN*60
    long_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_sec)
        timer.config(text="BREAK",fg=RED)
    if reps % 2 == 0:
        count_down(short_sec)
        timer.config(text="BREAK",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="WORK",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock_timer
        clock_timer = window.after(1000,count_down,count - 1)

    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato Gaming")
window.config(padx=100,pady=50,bg=YELLOW)

timer = Label(text="TIMER", font = (FONT_NAME, 35, "bold"),bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)
timer.config(padx=5,pady=5)

check = Label(font = (FONT_NAME, 15, "bold"),bg=YELLOW, fg=GREEN)
check.grid(column=1, row=4)
check.config(padx=5,pady=5)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=2)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=3)
start_button.config(padx=5,pady=5)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)
reset_button.config(padx=5,pady=5)

window.mainloop()