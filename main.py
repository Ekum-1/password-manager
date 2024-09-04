from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
        saved_web: {
            "email": saved_email,
            "password": saved_password,
        }
    }

    if len(saved_password) == 0 or len(saved_web) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    web_name = website_entry.get()
    # Ensure the file can be opened
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found.")
        return

    if len(web_name) == 0:
        messagebox.showinfo(title="Error", message="No website given for search")
    else:
        try:
            # Check if the website is in the data
            if web_name in data:
                email = data[web_name]["email"]
                password = data[web_name]["password"]
                messagebox.showinfo(title=f"{web_name}",
                                    message=f"Email: {email}\nPassword: "
                                            f"{password}")
            else:
                # Trigger an exception if web_name is not in the data
                raise KeyError
        except KeyError:
            # Catches the KeyError and handles the case where website not found
            messagebox.showinfo(title="Error",
                                message=f"no details for \"{web_name}\" exist.")

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

# Frame to combine website_entry and search_button
website_frame = Frame(window)
website_frame.grid(column=1, row=1, columnspan=2, sticky="w")

# Entries
website_entry = Entry(website_frame, width=21)
website_entry.grid(column=0, row=0)
website_entry.focus()

user_entry = Entry(width=39)
user_entry.grid(column=1, row=2, columnspan=2, sticky="w")
user_entry.insert(0, "myemail@gmail.com")


# Frame to combine password_entry and generate_btn
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2, sticky="w")

password_entry = Entry(password_frame, width=21)
password_entry.grid(column=0, row=0)

# Buttons
search_button = Button(website_frame, text="Search", width=14, command=find_password)
search_button.grid(column=1, row=0)

generate_btn = Button(password_frame, text="Generate Password", width=14, command=generate_password)
generate_btn.grid(column=1, row=0)

add_btn = Button(text="Add", width=33, command=get_info)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
