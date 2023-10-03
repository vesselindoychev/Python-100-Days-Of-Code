import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()

screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1000, height=1000)

states_file = pandas.read_csv('50_states.csv')
guessed_state_score = 0
guessed_states = []
states_list = states_file.state.to_list()


while len(guessed_states) < 50:
    player_answer = screen.textinput(title=f'{guessed_state_score}/{len(states_file)} States Correct',
                                     prompt="What's another state's name?").title()

    if player_answer == 'Exit':
        missing_states_data = pandas.DataFrame(states_list)
        missing_states_data.to_csv('states_to_learn.csv')
        break

    if player_answer in states_list:
        current_state = states_file[states_file.state == player_answer]
        guessed_state_score += 1
        guessed_states.append(player_answer)

        current_x = current_state.get('x').to_list()[0]
        current_y = current_state.get('y').to_list()[0]

        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(current_x, current_y)
        t.write(player_answer)
        states_list.remove(player_answer)


