import tkinter

window = tkinter.Tk()

window.title('Tkinter Widgets Demo')
window.minsize(width=500, height=500)

label = tkinter.Label(text='This is new text', font=('Arial', 14))
# label.grid(column=2, row=0)
label.pack()

button = tkinter.Button(text='Click me')
# button.grid(column=2, row=1)
button.pack()

entry = tkinter.Entry(width=20)
entry.pack()

text_area = tkinter.Text(height=5, width=30)
text_area.focus()
text_area.insert(tkinter.END, 'Random demo text')
text_area.pack()

spinbox = tkinter.Spinbox(from_=0, to=10, width=6)
spinbox.pack()

scale = tkinter.Scale(from_=0, to=50)
scale.pack()


def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


def radio_used():
    print(radio_button_state.get())


radio_button_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text='Option1', value=1, variable=radio_button_state, command=radio_used)

radio_button2 = tkinter.Radiobutton(text='Option2', value=2, variable=radio_button_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


window.mainloop()
