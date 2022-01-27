from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate():
    """PASSWORD GENERATOR"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


def save():
    """SAVE PASSWORD"""
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            print("file not found - it was created right now")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


def search():
    """SEARCH"""
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            account = json.load(data_file)
        email = account[website]["username"]
        password = account[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    except KeyError:
        if messagebox.askyesno(title="Error", message=f"You don't have the {website} account password saved.\n"
                                                      "Would you like to generate one now?"):
            generate()
    else:
        messagebox.showinfo(title=f"{website}", message=f"Username: {email}\nPassword: {password}")
        pyperclip.copy(password)


# ----------------------------- UI SETUP ----------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", width=15)
website_label.grid(column=0, row=1)
email_label = Label(text="Username:", width=15)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", width=15)
password_label.grid(column=0, row=3, )

website_input = Entry(width=34)
website_input.grid(column=1, row=1, sticky="W")
website_input.focus()

search_btn = Button(text="Search", width=14, command=search, takefocus=1, relief="raised")
search_btn.grid(column=2, row=1)

username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2, sticky="W")
username_input.insert(0, "pana.razvan@yahoo.com")

password_input = Entry(width=34)
password_input.grid(column=1, row=3, sticky="W")

generate_btn = Button(text="Generate Password", width=14, command=generate, takefocus=1, relief="raised")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=44, command=save, takefocus=1, relief="raised")
add_btn.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()
