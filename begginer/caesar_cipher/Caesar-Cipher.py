from art import logo


def caesar(text, shift, direction):
    end_text = ''
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            end_text += letter
            continue
        position = alphabet.index(letter)
        position += shift
        new_letter = alphabet[position]
        end_text += new_letter

    print(f"Here is the {direction}d result: {end_text}")


while True:
    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(text=text, shift=shift, direction=direction)

    confirmation = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if confirmation == 'no':
        print('Goodbye')
        break
