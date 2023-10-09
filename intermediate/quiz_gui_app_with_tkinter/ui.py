import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150, 125, text=f"lorem ipsum...", font=('Arial', 20, 'italic'),
                                                     width=280)

        self.check_img = tkinter.PhotoImage(file='images/true.png')
        self.cross_img = tkinter.PhotoImage(file='images/false.png')

        self.true_btn = tkinter.Button(image=self.check_img, highlightthickness=0,
                                       command=lambda m="True": self.which_btn_is_pressed(m))
        self.true_btn.grid(row=2, column=0)

        self.false_btn = tkinter.Button(image=self.cross_img, highlightthickness=0,
                                        command=lambda m='False': self.which_btn_is_pressed(m))
        self.false_btn.grid(row=2, column=1)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            self.show_score()
            self.true_btn.grid_remove()
            self.false_btn.grid_remove()

    def show_score(self):
        self.canvas.itemconfig(self.question_text,
                               text=f"You've completed the quiz\nYour Final score was: {self.score}/10")

    def which_btn_is_pressed(self, btn_press):

        correct_answer = self.quiz.check_answer()
        if btn_press == 'True' and correct_answer == 'True':
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.get_next_q()

        elif btn_press == 'False' and correct_answer == 'False':
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')
            self.get_next_q()
        else:
            self.get_next_q()
