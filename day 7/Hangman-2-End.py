import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

print("Selected word : "+word)
guess = input("Guess a letter : ").lower()

display = []

for i in range(len(word)):
    display.append('_')

for i in range(len(word)) :
    if guess == word[i]:
        display[i] = guess

print(display)