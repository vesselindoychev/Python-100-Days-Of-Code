import math
import tkinter
import time

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
checkmark_string = '✔'
checkmark_counter = 1
checkmark_number = 0
timer = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_count():
    global reps
    global checkmark_counter
    global checkmark_number
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text='Short Break', fg=RED)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


def count_down(count):
    global checkmark_number
    global checkmark_counter
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmark_counter += 1
        if checkmark_counter % 2 == 0:
            checkmark_number += 1
            checkmark.config(text=f"{checkmark_number * checkmark_string}")
        start_count()


# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global reps
    global checkmark_counter
    global checkmark_number
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text='Timer', fg=GREEN)
    reps = 0
    checkmark_counter = 0
    checkmark_number = 0
    checkmark.config(text='')


# ---------------------------- UI SETUP ------------------------------- #

blank_space = ''
window = tkinter.Tk()
window.title(f"Pomodoro GUI")
window.minsize(width=700, height=600)
window.config(padx=300, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, 'bold'))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text='Start', command=start_count)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', command=reset_time)
reset_button.grid(column=2, row=2)

checkmark = tkinter.Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()
