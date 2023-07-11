import time
import command
import data
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import syscommand


def make_transaction():
    if not command.check_recsources(False):
        print("The machine will be shut down due to lack of resources.")
        command.off()

    print("Welcome to the coffee shop!")
    order = input("What would you like? (espresso/latte/cappuccino) ?\n> ")

    if order not in data.MENU.keys():
        order = command.check_response(order)

    print(order)
    cost = input(f"${data.MENU[order]['cost']} please.\n> ")

    while not cost.replace('.', '').isnumeric() and cost != '.':
        cost = input("unexpected input, you can try again\n> ")

    if float(cost) < data.MENU[order]['cost']:
        print(f"Sorry that's not enough money. \n${cost} refunded.")
    else:
        for resource in data.MENU[order]['ingredients']:
            data.resources[resource] -= data.MENU[order]['ingredients'][resource]

        data.resources['cash'] += data.MENU[order]['cost']
        final_cost = float(cost) - data.MENU[order]['cost']

        if final_cost != 0:
            print(f"Here is ${final_cost} in change.")
            print(f"Here is your {order} ☕️. Enjoy!")


while True:
    make_transaction()
    time.sleep(5)
    syscommand.clear()
