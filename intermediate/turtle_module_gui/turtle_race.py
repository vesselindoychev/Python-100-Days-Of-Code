import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=700, height=500)
user_guess = screen.textinput(title='Make your guess', prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'green', 'orange', 'yellow', 'blue', 'purple']
x_coordinates = -340
y_coordinates = 160
counter = 0
all_turtles = []

for i in range(len(colors)):
    turtle_instance = Turtle(shape='turtle')
    turtle_instance.color(colors[i])
    turtle_instance.penup()
    turtle_instance.goto(x=x_coordinates, y=y_coordinates - counter)
    counter += 50
    all_turtles.append(turtle_instance)

is_race_on = False

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 340:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won! Winning color is {winning_color}")
            else:
                print(f"You have lost!  Winning color is {winning_color}")
            break
        step = random.randint(0, 10)
        turtle.forward(step)

screen.exitonclick()
