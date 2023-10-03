import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Paddle(x_coordinate=350, y_coordinate=0)
left_paddle = Paddle(x_coordinate=-350, y_coordinate=0)
ball = Ball(x_position=0, y_position=0)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')


def has_hit_the_paddle():
    if ball.distance(right_paddle) < 50 and ball.xcor() < 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        return True


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_top_right()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # if ball.xcor() > 380 or ball.xcor() < -380:
    #     ball.bounce_x()

    if has_hit_the_paddle():
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_right_point()

screen.exitonclick()
