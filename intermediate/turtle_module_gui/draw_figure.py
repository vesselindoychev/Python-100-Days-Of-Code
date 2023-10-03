import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('green')

"""
360 / 4 or 340 / 6
"""

turtle.pos()

sides = [x for x in range(3, 11)]
colors = ['red', 'purple', 'green', 'yellow', 'orange', 'blue', 'pink', 'red', 'gray', 'wheat', 'chocolate']


def draw_figure():
    color_index = -1
    for side in sides:
        angle = 360 / side
        color_index += 1
        for _ in range(side):
            turtle.color(colors[color_index])
            turtle.colormode(255)
            turtle.forward(100)
            turtle.right(angle)


draw_figure()
screen = Screen()
screen.exitonclick()
