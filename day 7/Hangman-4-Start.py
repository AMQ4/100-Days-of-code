import logo
import states
import random
import word_list

print(logo.logo)
word = random.choice(word_list.word_list)

display = []
no_blanks = len(word)
lives = 0

print(f"pssst, the solution is {word}.")
for i in range(no_blanks):
    display.append('_')

while no_blanks > 0 and lives < 6: # or simply if '_' in / not in display 
    prev_no_blanks = no_blanks
    guess = input("Guess a letter : ").lower()
    
    if guess not in display:
        for i in range(len(word)) :
            if guess == word[i]:
                display[i] = guess
                no_blanks -= 1
    if no_blanks == prev_no_blanks:
        if guess in display:
            print(f"You've already guessed {guess}")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(states.states[lives])
            lives+= 1      
        
    print(''.join(display),'\n')

if no_blanks == 0:
    print("You win!")
elif lives == 6:
    print("Game over.\n")