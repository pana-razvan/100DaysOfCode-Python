from tkinter import *


def convert():
    converted_value["text"] = round(float(value_to_convert.get()) * 1.60934, 2)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=15, pady=15)

text_1 = Label(text="Miles")
text_1.grid(column=2, row=0)

text_2 = Label(text="is equal to")
text_2.grid(column=0, row=1)

text_2 = Label(text="Km")
text_2.grid(column=2, row=1)

value_to_convert = Entry(width=10)
value_to_convert.grid(column=1, row=0)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

button = Button(text="Calculate", width=10, command=convert)
button.grid(column=1, row=2)

window.mainloop()
