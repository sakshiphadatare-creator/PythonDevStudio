import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# this based on my own logic
# for letter in range(0,nr_letters+1):
#     let = random.choice(letters[letter])
#     print(let ,end="")
# for symbol in range(0,nr_symbols+1):
#     sym =  random.choice(symbols[symbol])
#     print(sym  ,end="")
# for number in range(0,nr_numbers+1):
#     num = random.choice(numbers[number])
#     print(num, end="")
#
#
#
# password = ""
# for letter in range(0,nr_letters+1):
#     password += random.choice(letters[letter])
#
# for symbol in range(0,nr_symbol+1):
#     password +=  random.choice(symbols[symbol])
#
# for number in range(0,nr_numbers+1):
#     password += random.choice(numbers[number])
#
# print("Password : ",password )

#
# password_list = []
# for letter in range(0,nr_letters+1):
#     password_list.append(random.choice(letters[letter]))
#
# for symbol in range(0,nr_symbols+1):
#     password_list.append(random.choice(symbols[symbol]))
#
# for number in range(0,nr_numbers+1):
#     password_list.append(random.choice(numbers[number]))
#
# print("Password : ",password_list )
#
# random.shuffle(password_list)
# print(password_list)

# for char in password_list:
#     print(char,end="")


pass_ = []
for letter in range(0,nr_letters+1):
    pass_.append(random.choice(letters[letter]))

for symbol in range(0,nr_symbols+1):
    pass_.append(random.choice(symbols[symbol]))

for number in range(0,nr_numbers+1):
    pass_.append(random.choice(numbers[number]))
# print(pass_)
random.shuffle(pass_)

password = ""
for char in pass_:
    password += char
print("Your password is : ",password)



