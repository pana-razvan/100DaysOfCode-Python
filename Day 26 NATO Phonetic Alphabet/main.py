import pandas

phonetic_alphabet = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
phonetic_alphabet_dict = {
    row.letter: row.code
    for (index, row) in phonetic_alphabet.iterrows()
}


def generate_phonetic_letters():
    user_input = input("Enter a word or type 'EXIT' to quit: ").upper()
    if user_input == "EXIT":
        pass
    else:
        try:
            output = [phonetic_alphabet_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_phonetic_letters()
        else:
            print(output)


generate_phonetic_letters()

