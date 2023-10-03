import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

display = list('_' * len(chosen_word))

lives = 6
guessed_letter = False
is_lose = False

print(logo)

while '_' in display:
    guess = input('Guess a letter: ').lower()
    guessed_letter = False

    if guess in display:
        print(f'You\'ve already guessed {guess}')
        continue

    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
            guessed_letter = True

    if not guessed_letter:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(' '.join(display))
        print(stages[lives])

    else:
        print(' '.join(display))
        print(stages[lives])

    if lives == 0:
        is_lose = True
        break

if is_lose:
    print('You lose.\n'
          f'Correct word is {chosen_word}')
else:
    print('You win.')
