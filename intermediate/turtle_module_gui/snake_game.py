import time
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)
counter = 0
all_segments = []

new_turtle = Turtle(shape='square')

for i in range(3):
    turtle_instance = Turtle(shape='square')
    turtle_instance.penup()
    turtle_instance.color('white')
    turtle_instance.goto(x=-20 - counter, y=0)
    counter -= 20
    all_segments.append(turtle_instance)

while True:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(all_segments) - 1, 0, -1):
        new_x = all_segments[segment_number - 1].xcor()
        new_y = all_segments[segment_number - 1].ycor()
        all_segments[segment_number].goto(new_x, new_y)
    all_segments[0].forward(20)
