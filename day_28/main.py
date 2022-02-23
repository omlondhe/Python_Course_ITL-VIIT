from tkinter import *
from PIL import ImageTk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#212121"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_value, text="00:00")
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    count_time(WORK_MIN * 60)
    title.config(text="WORK", fg=GREEN)
    if reps % 8 == 0:
        title.config(text="LONG BREAK", fg=RED)
        count_time(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title.config(text="SHORT BREAK", fg=PINK)
        count_time(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_time(count):
    canvas.itemconfig(timer_value, text=f'{math.floor(count/60):02d}:{count%60:02d}')
    if count > 0:
        global timer 
        timer = window.after(1000, count_time, count - 1)
    else: 
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions): mark += "✓"
        checkmarks.config(text=mark) 
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 51))
title.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
background = ImageTk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
timer_value = canvas.create_text(100, 130, text="WELCOME", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="✓", fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=2)

window.mainloop()