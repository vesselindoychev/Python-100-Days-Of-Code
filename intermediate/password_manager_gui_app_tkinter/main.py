import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]

    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.delete(0, tkinter.END)
    password_input.insert(tkinter.END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_entry = website_input.get().title()
    email_or_username_entry = email_or_username_input.get()
    password_entry = password_input.get()

    new_data = {
        website_entry: {
            'email_or_username': email_or_username_entry,
            'password': password_entry,
        }
    }
    if website_entry == '' or email_or_username_entry == '' or password_entry == '':
        show_warning()
    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except ValueError:
            with open('data.json', mode='w') as file3:
                json.dump(new_data, file3, indent=4)
        else:
            with open('data.json', mode='w') as file2:
                json.dump(data, file2, indent=4)

        website_input.delete(0, tkinter.END)
        email_or_username_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)

        show_confirmation()


def show_warning():
    messagebox.showinfo(title='Warning', message='You should fill all of the fields!')


def show_confirmation():
    messagebox.showinfo(title='Confirmation', message='Data is saved')


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width=600, height=500)
window.title('Password Manager')
window.config(padx=50, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)

website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_or_username_label = tkinter.Label(text='Email/Username:')
email_or_username_label.grid(row=2, column=0)

email_or_username_input = tkinter.Entry(width=35)
email_or_username_input.grid(row=2, column=1, columnspan=2)
email_or_username_input.insert(tkinter.END, 'veselindoi123@gmail.com')

password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_btn = tkinter.Button(text='Generate Password', command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = tkinter.Button(text='Add', width=30, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
