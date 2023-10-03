from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_coordinate, y=y_coordinate)

    def go_up(self):
        new_y = self.ycor() + 100
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 100
        self.goto(self.xcor(), new_y)
