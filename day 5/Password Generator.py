import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

available_indices = []
n = nr_letters+nr_numbers+nr_symbols

# generate an initial password
password = [] 

for i in range(0,n):
    password.append('#')
    available_indices.append(i)

for i in range(nr_letters):
    random_index = random.randint(0,len(available_indices)-1)
    password[available_indices[random_index]] = letters[random.randint(0,len(letters)-1)]
    available_indices.pop(random_index)

for i in range(nr_numbers):
    random_index = random.randint(0,len(available_indices)-1)
    password[available_indices[random_index]] = numbers[random.randint(0,len(numbers)-1)]
    available_indices.pop(random_index)

for i in range(nr_symbols):
    random_index = random.randint(0,len(available_indices)-1)
    password[available_indices[random_index]] = symbols[random.randint(0,len(symbols)-1)]
    available_indices.pop(random_index)

# you can generate the password first in order of letters first then symbols
# then number and then apply random.shuffle(password) to reorder the list in a 
# random order.

for i in password:
    print(i,end='')
print()

# password = ''.join(password)
# print(password)
