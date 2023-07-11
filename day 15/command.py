import data


def menu():
    print("\n\n+ ---------------- +")
    for _ in data.MENU:
        print("| {:<17}|".format(f"{_}: {data.MENU[_]['cost']}$"))
    print("+ ---------------- +\n")
    response = input("> ")
    return check_response(response)


def fill():
    data.resources['milk'] = 600
    data.resources['water'] = 1000
    data.resources['coffee'] = 150
    print("\nThe machine has been filled with resources successfully.")
    response = input("\n> ")
    return check_response(response)


def check_recsources(siginal=True):
    answer = True
    i = 1
    resources = []
    __max = [0, 0, 0]
    current_resources_values = list(data.resources.values())
    for drink in data.MENU.keys():
        for resource in data.MENU[drink]["ingredients"]:
            resources.append(data.MENU[drink]["ingredients"][resource])
    for resource in resources:
        __max[i - 1] = max(__max[i - 1], resource)
        i += 1
        if i > 3:
            i = 1

    resources = list(data.resources)
    for i in range(3):
        if __max[i] > current_resources_values[i]:
            print(f"There is not enough {resources[i]}.")
            answer = False
    if siginal and answer is False:
        if input("\ntype 'fill' to refill the machine\n> ").lower() == "fill":
            fill()
    if siginal:
        print("The machine is filled, and here is a report :", end="")
        return report()
    return answer


def report():
    print("\n\n+ ---------------- +")

    for _ in data.resources.keys():
        print("| {:<17}|".format(
            f"{_}: {data.resources[_]}{'ml' if _ not in ['coffee', 'cash'] else 'g' if _ != 'cash' else '$'}"))

    print("+ ---------------- +\n")
    response = input("> ")
    return check_response(response)


def man():
    print("\n\nWelcome to the manual page for machine coffee.\n|\n+", end="-> ")
    print("* report -> get a report about the resources.\n|\n+-> * menu -> show the menu.\n|\n+", end="->")
    print("* exit -> turn off the machine.\n|\n+", end="->")
    print("* fill -> to refill the machine with resources.\n|\n+", end="->")
    print("* chkres -> to check the resources.\n")
    response = input("> ")
    return check_response(response)


def check_response(response):
    while response not in commands.keys() and response not in data.MENU.keys():
        response = input(f"`{response}` not  defined , type `man` to view the manual for help. \n> ").lower()
    if response in data.MENU.keys():
        return response
    else:
        response = commands[response]()
    return response


def off():
    exit()


commands = {"man": man, "menu": menu, "report": report, "exit": off, "fill": fill, "chkres": check_recsources}
