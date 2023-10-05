import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_STYLE = 'Ariel'
COUNT = 3
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas_card_front.itemconfig(title_text, text='French', fill='black')
    canvas_card_front.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas_card_front.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas_card_front.itemconfig(card_background, image=card_back_img)
    canvas_card_front.itemconfig(title_text, text='English', fill='white')
    canvas_card_front.itemconfig(word_text, text=current_card['English'], fill='white')


def remove_card():
    data_dict.remove(current_card)
    new_data_frame = pandas.DataFrame(data_dict)
    new_data_frame.to_csv('data/words_to_learn.csv', index=False)

    next_card()


window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas_card_front = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = tkinter.PhotoImage(file='images/card_front.png')
card_back_img = tkinter.PhotoImage(file='images/card_back.png')
card_background = canvas_card_front.create_image(400, 263, image=card_front_img)

title_text = canvas_card_front.create_text(400, 150, text='Title', font=(FONT_STYLE, 40, 'italic'))
word_text = canvas_card_front.create_text(400, 263, text='Word', font=(FONT_STYLE, 60, 'bold'))

canvas_card_front.grid(row=0, column=0, columnspan=2)

right_image = tkinter.PhotoImage(file='images/right.png')
wrong_image = tkinter.PhotoImage(file='images/wrong.png')

right_btn = tkinter.Button(image=right_image, highlightthickness=0, command=remove_card)
right_btn.grid(row=1, column=0)

wrong_btn = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)

next_card()

window.mainloop()
