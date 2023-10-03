import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('green')
turtle.pensize(10)
turtle.speed(10)
directions = [90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk():
    while True:
        turtle.color(random_color())
        turtle.forward(30)
        turtle.setheading(random.choice(directions))


random_walk()
screen = Screen()
screen.exitonclick()
