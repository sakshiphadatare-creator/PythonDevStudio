import art
import random as rand
EASY_LEVEL_GUESS = 10
DIFFICULT_LEVEL_GUESS = 5
def check_result(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it!, the correct answer is {actual_answer}")

def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_GUESS
    elif level == "hard":
        return DIFFICULT_LEVEL_GUESS

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!🤝")
    """ Random number generator between 1 to 100"""
    print("I'm thinking of a number between 1 and 100.")
    answer = rand.randint(1, 100)
    print(answer)
    turns = set_difficulty()  # store because of run the function
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_result(guess, answer, turns)  # store because of run the function
        if turns == 0:
            print("You've run out the guesses. You lose!👎🏻")
            return
        elif turns != guess:
            print("Guess again")

game()
















