from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_info():
    saved_web = website_entry.get()
    saved_email = user_entry.get()
    saved_password = password_entry.get()
    data = f"{saved_web} | {saved_email} | {saved_password}\n"

    if len(saved_password) == 0 or len(saved_web) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=saved_web,
                                       message=f"These are the details entered: \nEmail:{saved_email}\n"
                                               f"Password: {saved_password} \nis it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{data}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=280, height=280, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

# Entries
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

user_entry = Entry(width=39)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_entry.insert(0, "myemail@gmail.com")

# Frame to combine password_entry and generate_btn
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2, sticky="w")

password_entry = Entry(password_frame, width=21)
password_entry.grid(column=0, row=0)

generate_btn = Button(password_frame, text="Generate Password", width=14, command=generate_password)
generate_btn.grid(column=1, row=0)

add_btn = Button(text="Add", width=33, command=get_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
