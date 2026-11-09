# {new_key : key_value for (index, row) in df.iterrows()}
# day - 30 Next go password generator
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format :
phonetic_alphabets = {row.letter : row.code for (index,row) in data.iterrows()}
print(phonetic_alphabets)

#TODO 2. Create a list of the phonetic code words from the word that the user inputs.

def generate_phonetic():
    user_input = input("Enter a name: ").upper()
    try:
        output_data = [phonetic_alphabets[value] for value in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabet Please.")
        generate_phonetic()
    else:
        print(output_data)
generate_phonetic()

# this is mine
# is_alphabet_present = True
# while is_alphabet_present:
#     user_input = input("Enter a name: ").upper()
#     try:
#         output_data = [phonetic_alphabets[value] for value in user_input]
#     except KeyError:
#         print("Sorry, Only letters in the alphabet Please.")
#     else:
#         print(output_data)
#         is_alphabet_present = False





