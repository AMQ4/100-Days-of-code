import random

names =  input()

list_of_names = names.split(', ')
print(list_of_names[random.randint(0,len(list_of_names)-1)]+" is going to buy the meal today!")