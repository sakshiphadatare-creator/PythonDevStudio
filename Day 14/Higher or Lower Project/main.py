import random as rand
from art import logo, vs
import game_data
# define the format_data() refer to the game_data.py and return it.
def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, {account_description} from {account_country}"

# define the check_answer() inside the function a_follower,b_follower,guess and check if a > b then return user_guess equals to 'a' else user_guess equals to 'b'.
def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

# print logo
print(logo)
score = 0
game_continue = True
# Generate the random accounts from the game data.
b_account = rand.choice(game_data.data)

# Make a game repeatable.
while game_continue:

    # Making account at position b become the next account at position a.
    a_account = b_account
    b_account = rand.choice(game_data.data)

    if a_account == b_account :
        b_account = rand.choice(game_data.data)

    # Print it as a required form.
    print(f"Compare A: {format_data(a_account)}")
    print(vs)
    print(f"Against compare B: {format_data(b_account)}")

    # Ask a user for a guess.
    guess = input("Who has more follower's, Type 'A' or 'B': ").lower()

    # Clear the screen.
    print("\n" * 20)

    # Print logo.
    print(logo)

    # Get follower counts of each account.
    a_count_follower = a_account['follower_count']
    b_count_follower = b_account['follower_count']

    # Check if user is correct.
    is_correct = check_answer(guess, a_count_follower, b_count_follower)

    # Give user feedback on their Guess.
    # score keeping if is_correct then score increase by 1 and print you're guess is right else you're wrong stop the program
    if is_correct:
        score += 1
        print(f"You're right!, current score : {score}")
    else:
        print(f"You're wrong, Final score : {score}")
        game_continue = False


