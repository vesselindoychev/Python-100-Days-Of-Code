import pandas


nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_data.to_dict())

result = {row.letter: row.code for index, row in nato_data.iterrows()}
print(result)


while True:
    word_input = input(f"Enter a word: ")
    filtered_word = [result[ch.upper()] for ch in word_input]

    print(filtered_word)

