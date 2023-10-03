import random


def choose_random_num():
    random_num = random.randint(1, 100)
    return random_num


print('Welcome to the Number Guessing game!')
print('I\'m thinking of a number between 1 and 100.')
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

random_number = choose_random_num()


def algorithm(attempts, guess, random_number):
    if guess == random_number:
        attempts -= 1
        print(f'Good job! You got it.The answer was {guess}. You win.')
        return attempts
    if guess < random_number:
        attempts -= 1
        print('Too low.')
        return attempts
    if guess > random_number:
        attempts -= 1
        print('Too high.')
        return attempts


def is_guessed(guess, random_number):
    if guess == random_number:
        return True


def print_a_msg(attempts):
    print(f'You have {attempts} attempts remaining to guess the number.')


if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while True:
    print_a_msg(attempts)
    guess = int(input('Make a guess: '))

    current_attempts = algorithm(attempts, guess, random_number)
    if is_guessed(guess, random_number):
        break
    attempts = current_attempts

    if attempts == 0:
        print('You have run out of guesses. No more attempts. You lose.')
        break
    print('Guess again.')
