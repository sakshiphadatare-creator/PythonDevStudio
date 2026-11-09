from typing import KeysView

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: check the resources sufficient if not sufficient resources then display sorry
def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print("“Sorry there is not enough {item}.”")
        return False
    return True


# TODO: process coins
# if sufficient resources to make the required drink then user insert coin
# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# calculate the money
def process_coins():

    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("Hoe many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pinnies?: ")) * 0.01
    return total


# TODO: CHECK TRANSECTION Check that the user has inserted enough money to purchase the drink they selected
# the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered

def is_transection_successfully(recevied_money, drink_cost):
    if recevied_money >= drink_cost:
        change =round(recevied_money - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



# TODO: if the transection successfully then the make the drink
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: show the prompt again for next customer
prompt_continue = True
while prompt_continue:
    # TODO: Ask user what would you like?
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    # TODO: turn off coffee machine by entering 'off' to the prompt

    if choice == 'off':
        prompt_continue = False

    # TODO: if user enter 'report' to the prompt then generate all report
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money:{profit} ")
    else :
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
        if is_transection_successfully(payment, drink['cost']):
            make_coffee(choice, drink['ingredients'])


















