from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print("Sorry that item is not available.")
            continue
        else:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
