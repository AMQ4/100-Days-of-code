from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True :
    order = input("\nWhat would you like? (latte/espresso/cappuccino/): \n> ")
    if order == "off" :
        print("Bye !")
        exit()
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else :
        order = menu.find_drink(order)
        if order is not None and coffee_maker.is_resource_sufficient(order):
            money_machine.make_payment(order.cost)
            coffee_maker.make_coffee(order)