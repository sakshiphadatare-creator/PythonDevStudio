print(True or False and False)   # True
print(bool([]))  # False

print("-------------------- While loop ---------------------")

''' Definition : While loop in Python is repeatedly execute a block of codes as long as 
                 the specified condition is true. 
    It is basically used for scenarios where the number of iterations is not known beforehand, and depends
    Dynamic condition within the loop, so the syntax of the while loop is as follows 
    While condition is going to print out what the condition should be meet according to your data.'''

no = 1
while no <= 4:
    print(no)
    no+=1

no = 0
while no <= 100:
    print(no)
    no+=2

count = 1
while count<=5:
    print("Count : ",count)
    count+=1

while True:
    user_input = input("Enter the exist to stop: ").lower()
    if user_input == "exist":
        break
print("you entered: ", user_input)

is_true = True
while is_true:
    user_input = input("Enter the 'exist' to STOP : ").lower()
    if user_input == "exist":
        is_true = False
    print("You entered:", user_input)

print("-------------------- Guessing game ---------------------")

the_word = "kiwi"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != the_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Guess the word:").lower()
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("you lost the game.")
else:
    print("You Won!")



print("-------------------- For loop ---------------------")
'''  Definition of for loop: The for statement is used to iterate over the elements of a sequence 
    (such as a string, tuple or list) or other iterable object.
    it allows to execute a bloch of code multiple times once for each item in the sequence.
    
'''

for word in "medical":
    print(word)

#How to print index using range
words = ['come', 'eat', 'time', 'elephant', 'toll']
for index in range(len(words)):
    print(words[index])
    print(index)


fruit = ["apple", "banana", "cherry"]

for index in range(4):
    if index == 0:
        print("first item")
        break
    else:
        print("Nothing is here!!")

#Operation in dictionary
my_dic = {'name':'sakshi', 'age':19, 'city':'pune'}

for key,value in my_dic.items():
    print(key,":", value)
for key in my_dic.keys():
    print(key)
for value in my_dic.values():
    print(value)













