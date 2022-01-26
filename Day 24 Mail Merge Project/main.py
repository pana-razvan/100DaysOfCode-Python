with open("Input/Names/invited_names.txt") as names:
    n_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    example_letter_text = letter.read()

    for name in n_list:
        stripped_name = name.strip()
        with open(f"Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as new_letter:
            new_letter.write(example_letter_text.replace("[name]", stripped_name))
