import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
#print(phonetic_dict)


def generate_phonetic():

    word = input("\nEnter a word: \n").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
