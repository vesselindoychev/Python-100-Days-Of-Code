import tkinter

BACKGROUND_COLOR = "#B1DDC6"
FONT_STYLE = 'Ariel'
window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_card_front = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file='images/card_front.png')
canvas_card_front.create_image(400, 263, image=card_front)

title_text = canvas_card_front.create_text(400, 150, text='Title', font=(FONT_STYLE, 40, 'italic'))
word_text = canvas_card_front.create_text(400, 263, text='Word', font=(FONT_STYLE, 60, 'bold'))

canvas_card_front.grid(row=0, column=0, columnspan=2)
# canvas_card_front.pack()


right_image = tkinter.PhotoImage(file='images/right.png')
wrong_image = tkinter.PhotoImage(file='images/wrong.png')

right_btn = tkinter.Button(image=right_image, highlightthickness=0, command='')
right_btn.grid(row=1, column=0)

wrong_btn = tkinter.Button(image=wrong_image, highlightthickness=0, command='')
wrong_btn.grid(row=1, column=1)

window.mainloop()
