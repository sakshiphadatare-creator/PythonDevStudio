def translate(word):
    translation = " "
    for letter in word:
        if letter in "AEIOUaeiou":
            translation = translation + 'r'
        else:
            translation + translation + letter   #give us only translate letter.
            #translation = translation + letter   # Give us a word with translate letter.

    return translation
print(translate(input("Enter the keyword: ")))


