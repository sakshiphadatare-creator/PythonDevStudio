import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print("What's you choice? \n0. Rock\n1. Paper\n2. Scissors\n3. Exit\n ")
# choice = int(input("Enter here : "))
#
# if choice == 0:
#     print("Your choice (rock):\n", rock)
#
#     options = [scissors, paper, rock]
#     print("Computer choose :\n", random.choice(options))
#
#     if options[0] == scissors:
#         print("You win ")
#     elif options[1] == paper:
#         print("You lose ")
#     else:
#         print("It's a draw ")
#
# elif choice == 1:
#     print("Your choice (paper):\n", paper)
#
#     options = [scissors, rock, paper]
#     print("Computer choose :\n", random.choice(options))
#
#     if options[0] == scissors:
#         print("You Lose ")
#     elif options[1] == rock:
#         print("You win ")
#     else:
#         print("It's a draw ")
#
# elif choice == 2:
#     print("Your choice (paper):\n", scissors)
#
#     options = [rock, paper, scissors]
#     print(f"Computer choose :\n{random.choice(options)}")
#
#     if options[0] == rock:
#         print("You win ")
#     elif options[1] == paper:
#         print("You Lose ")
#     else:
#         print("It's a draw ")
#
# else:
#     print("You Exit fron the Game successfully.")

images = [rock, paper, scissors]
print("What's you choice? \n0. Rock\n1. Paper\n2. Scissors ")
user_choice = int(input("Enter here : "))
print(images[user_choice])
computer_choice = random.randint(0,2)
print("Computer choice:  ",images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice.")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif user_choice == computer_choice :
    print("It's a draw")















