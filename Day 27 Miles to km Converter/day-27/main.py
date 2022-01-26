from tkinter import *


def my_button_click():
    my_label["text"] = input_box.get()


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=45, pady=45)

# Labels
my_label = Label(text="I am a label")
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=12, pady=12)

# Button
button1 = Button(text="Click me!", command=my_button_click)
button1.grid(column=1, row=1)

button2 = Button(text="Click me!", command=my_button_click)
button2.grid(column=2, row=0)


# Entry
input_box = Entry(width=30)
input_box.grid(column=3, row=2)

window.mainloop()
