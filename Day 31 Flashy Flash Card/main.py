from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
TRANSLATE_FROM = "French"
TRANSLATE_TO = "English"
current_card = {}
to_learn = {}


def load_data():
    global to_learn
    try:
        data = pandas.read_csv("data/words_to_learn.csv", index_col=0)
    except FileNotFoundError:
        original_data = pandas.read_csv("data/words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")


def display_translation():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text=TRANSLATE_TO, fill="white")
    canvas.itemconfig(word, text=current_card[TRANSLATE_TO], fill="white")


def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        print("That was the last word to learn.")
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text=TRANSLATE_FROM, fill="black")
    canvas.itemconfig(word, text=current_card[TRANSLATE_FROM], fill="black")
    flip_timer = window.after(3000, display_translation)


def word_is_known():
    try:
        to_learn.remove(current_card)
    except ValueError:
        pass
    next_card()
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv")


def reset_words():
    try:
        os.remove("data/words_to_learn.csv")
    except FileNotFoundError:
        pass
    load_data()


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, display_translation)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right = PhotoImage(file="images/right.png")
word_known = Button(image=right, highlightthickness=0, relief="flat", borderwidth=0, command=word_is_known)
word_known.grid(row=1, column=0)

wrong = PhotoImage(file="images/wrong.png")
word_not_known = Button(image=wrong, highlightthickness=0, relief="flat", borderwidth=0, command=next_card)
word_not_known.grid(row=1, column=1)

reset_button = Button(text="Reset", font=("Arial", 6, "italic"), width=20, command=reset_words)
reset_button.grid(row=1, column=0, columnspan=2)

load_data()
next_card()

window.mainloop()
