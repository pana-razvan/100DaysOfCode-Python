from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_coffee_machine_menu = Menu()
my_money_machine = MoneyMachine()
frappe = MenuItem("frappe", 100, 50, 24, 2)
my_coffee_machine_menu.menu.append(frappe)
my_coffee_maker.resources["water"] = 1000
my_coffee_maker.resources["coffee"] = 1000
my_coffee_maker.resources["milk"] = 1000

is_on = True

while is_on:
    user_choice = input(f"What would you like? ({my_coffee_machine_menu.get_items()}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_coffee_machine_menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)