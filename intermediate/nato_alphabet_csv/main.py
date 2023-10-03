import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data.to_dict())

result = {row.letter: row.code for index, row in nato_data.iterrows()}
print(result)


def generate_phonetic():
    word_input = input(f"Enter a word: ")
    try:
        filtered_word = [result[ch.upper()] for ch in word_input]
    except KeyError:
        print(f"Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(filtered_word)


generate_phonetic()
