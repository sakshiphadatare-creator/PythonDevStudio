from tkinter.font import names

import menu
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True
while is_on:
    option = my_menu.get_items()
    choice = input(f"What would you like to buy?({option}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = my_menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)







