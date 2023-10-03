import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('green')

timmy_the_turtle.speed('fastest')
radius = 100


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def make_spirograph(gap_size):
    for _ in range(360 // gap_size):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(radius)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)


make_spirograph(5)
screen = Screen()
screen.exitonclick()
