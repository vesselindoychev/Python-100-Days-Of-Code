# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.read().split('\n')
    for name in names:
        with open('Input/Letters/starting_letter.txt') as file:
            data = file.read().split('\n')

            search_text = data[0].split()[1]
            replace_text = f"{name},"
            data = '\n'.join(data)
            data = data.replace(search_text, replace_text)

            stripped_name = name.replace(' ', '_')
            with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as ready_file:
                ready_file.write(data)
