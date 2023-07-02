import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

print("Selected word : "+word)

display = []
no_blanks = len(word)

for i in range(no_blanks):
    display.append('_')
while no_blanks > 0 : # or simply if '_' in / not in display 
    guess = input("Guess a letter : ").lower()
    for i in range(len(word)) :
        if guess == word[i]:
            display[i] = guess
            no_blanks -= 1
    print(display)
print("You win!")