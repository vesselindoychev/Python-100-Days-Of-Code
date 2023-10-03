rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

items = {
    '0': rock,
    '1': paper,
    '2': scissors
}

# if starting_choice == 0:
#   item = rock
# elif starting_choice == 1:
#   item = paper
# else:
#   item = scissors

print(items[user_choice])

computer_random_choice = str(random.randint(0, 2))

print('Computer chose:')
print(items[computer_random_choice])

if items[user_choice] == rock:
    if items[computer_random_choice] == paper:
        print('You lose')
    elif items[computer_random_choice] == scissors:
        print('You win')
    else:
        print('It\'s a draw')

elif items[user_choice] == paper:
    if items[computer_random_choice] == rock:
        print('You win')
    elif items[computer_random_choice] == scissors:
        print('You lose')
    else:
        print('It\'s a draw')

else:
    if items[computer_random_choice] == rock:
        print('You lose')
    elif items[computer_random_choice] == paper:
        print('You win')
    else:
        print('It\'s a draw')



