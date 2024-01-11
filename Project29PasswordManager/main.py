from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "username": username,
        "password": password,
    }}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}"
                                                   #   f"\nPassword: {password}\nIs it ok to save?")
        #if is_ok:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success!", message="Information saved with success!")

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", padx=30)
password_label.grid(row=3, column=0)

#Entries

website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)

#Definir valor padrão para email/username
#username_entry.insert(0, "matheus@email.com")

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=44)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
