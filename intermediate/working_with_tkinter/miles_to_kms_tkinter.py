import tkinter


def calculate_miles_to_kms():
    current_miles = int(starting_entry.get())
    result = current_miles * 1.609344
    result_label.config(text=result)


window = tkinter.Tk()
window.minsize()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)


starting_entry = tkinter.Entry(width=10)
starting_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

string_label = tkinter.Label(text='is equal to')
string_label.grid(column=0, row=1)

result_label = tkinter.Label(text='0')
result_label.grid(column=1, row=1)

kms_label = tkinter.Label(text='Km')
kms_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text='Calculate', command=calculate_miles_to_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()
