from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def timer_reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0 or count_sec in range(0, 10):
    #     count_sec = "0" + str(count_sec)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks["text"] += '✓'


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.config(bg=YELLOW, highlightbackground=YELLOW, font=(FONT_NAME, 20, "bold"))
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.config(highlightbackground=YELLOW, font=(FONT_NAME, 20, "bold"))
reset_button.grid(row=2, column=2)

check_marks = Label(text="")
check_marks.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
check_marks.grid(row=3, column=1)
window.mainloop()
