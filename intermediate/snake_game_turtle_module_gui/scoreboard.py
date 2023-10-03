from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.take_high_score_from_file())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.rewrite_high_score()
        self.score = 0
        self.update_scoreboard()

    def add_score_point(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def rewrite_high_score(self):
        with open('score_file.txt', mode='w') as score_file:
            score_file.write(f"{self.high_score}")

    @staticmethod
    def take_high_score_from_file():
        with open('score_file.txt') as score_file:
            high_score_result = score_file.read()
            return high_score_result
