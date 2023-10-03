import random

from game_data import data


def update_data_length():
    return len(data_clone)


def play(dicts):
    result = f"Compare A: "
    followers = {}
    counter = 0
    letter = ''
    winnable = []
    for d in dicts:
        result += f"{d['name']}, a {d['description']}, from {d['country']}."
        if counter == 0:
            letter = 'A'
        else:
            letter = 'B'

        followers[letter] = d['follower_count']
        print(result)
        result = ''
        result = f"VS\nAgainst B: "
        counter += 1
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if followers['A'] > followers['B']:
        winnable.append('A')
        winnable.append(followers['A'])
    else:
        winnable.append('B')
        winnable.append(followers['B'])
    return answer, winnable


not_is_over = True
starting_choice = True
is_wrong = False
score = 0

first_num = 0
first_choice = 0
second_choice = 0

data_clone = data
data_length = update_data_length()

confirmation = input("Type 'y' to play or 'n' to exit: ")

if confirmation == 'y':
    while not_is_over and len(data) > 1:
        if starting_choice:
            first_num = random.randint(1, data_length)
            first_choice = data[first_num]
            data.pop(first_num)
            starting_choice = False
            data_length = update_data_length()
        else:
            first_choice = second_choice
        second_num = random.randint(1, data_length)
        second_choice = data[second_num]
        data.pop(second_num)
        data_length = update_data_length()

        answer = play([first_choice, second_choice])
        guess = answer[0]
        correct_answer = answer[1]
        if guess == correct_answer[0]:
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            confirmation2 = input('Do you want to play again? Type \'yes\' to confirm or \'no\' to exit: ').lower()
            if confirmation2 == 'yes':
                data_clone = data
                continue
            not_is_over = False

else:
    print('Exit()')