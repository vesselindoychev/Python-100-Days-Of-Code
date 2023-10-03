from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.left(90)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_winnable(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)