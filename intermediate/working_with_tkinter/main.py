import tkinter
from tkinter import Tk


def button_clicked():
    my_label.config(text=my_entry.get())


window = Tk()

window.title('My First GUI')
window.minsize(width=600, height=300)

# Label

my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack()
# my_label.place(x=0, y=200)
my_label.grid(column=0, row=0)

my_label['text'] = 'New Text'
my_label.config(text='New Text')

# Button

new_button = tkinter.Button(text='Accept')
new_button.grid(column=2, row=0)

my_button = tkinter.Button(text='Click me', command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

# Entry
my_entry = tkinter.Entry()
# my_entry.pack()
my_entry.grid(column=3, row=2)
window.mainloop()
