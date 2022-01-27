from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF5959"
BLUE = "#676FA3"
SKY = "#1C6DD0"
SNOW = "#EEF2FF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        label.config(text="Work", fg=PINK)
        count_down(work_sec)
    elif reps % 8 == 0:
        label.config(text="Break", fg=BLUE)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=SKY)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer, reps
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{math.floor(count / 60)}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count % 60}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for n in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=SNOW)

label = Label(text="Timer", fg=SKY, bg=SNOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, bg=SNOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks = Label(bg=SNOW, fg=SKY)
check_marks.grid(column=1, row=3)

window.mainloop()
