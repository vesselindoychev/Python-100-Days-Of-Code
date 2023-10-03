import time
from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# high_score = HighScore(scoreboard.score)

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

NUMBER = 300


def has_hit_the_wall():
    if snake.head.xcor() >= NUMBER or snake.head.xcor() <= -NUMBER or snake.head.ycor() >= NUMBER or snake.head.ycor() <= -NUMBER:
        return True


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score_point()

    if has_hit_the_wall():
        scoreboard.reset_score()
        snake.reset_snake()
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
screen.exitonclick()
