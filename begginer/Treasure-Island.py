
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right_question = input('You are at a crossroad, where do you want to go? Type "left" or "right" ')
if left_or_right_question.lower() == 'left':
    swim_or_wait_question = input('Hello, adventurer! You arrived at a dock in the middle of the ocean. You have a choice.\n'
                                  'Swim through the ocean or wait for a pirate ship to notice you and take you on the board.\n'
                                  'Type "swim" or "wait" ')
    if swim_or_wait_question.lower() == 'wait':
        which_door_question = input('You successfully have been taken by the pirates. They took you to abandoned island.\n'
                                    'You see 4 different doors in front of you. They are magical and can teleport you to different destinations.\n'
                                    'Which door will you open?\n'
                                    'Type "Red", "Blue", "Yellow" or "Green" ').lower()
        if which_door_question == 'red':
            print('You have been teleported to burning wood and you burned. Game over.')
        elif which_door_question == 'blue':
            print('You have been teleported to arena with wild beasts. They killed you and ate you. Game over.')
        elif which_door_question == 'yellow':
            print('Congratulations. You Win!')
        else:
            print('Sorry, player! Wrong door. Game over.')
    else:
        print('O-o-o you have been attacked by a trout. Game over.')
else:
    print('You fall into a hole. Game Over. Try again.')
