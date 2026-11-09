alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
def caesar( original_text, shifted_amount,direction):
    #  Use the value of the user chosen 'direction' variable to determine which functionality to use.
    cipher_text = ""
    for letter in original_text:

        if direction == "decode":
            shifted_amount *= -1

        shifted_index = alphabet.index(letter) + shifted_amount
        cipher_text += alphabet[shifted_index]
    print(f"Here is the {direction}d result: {cipher_text}")
caesar(direction = direction,original_text=text,shifted_amount=shift)









