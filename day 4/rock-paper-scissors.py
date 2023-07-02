import random
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

options = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n\n"))
computer_choice = random.randint(0,2) 

if choice >= 3 or choice < 0:  
    print("You typed an invalid number, you lose!")
else:
    print(options[choice])
    print("\nComputer chose:\n")
    print(options[computer_choice]+"\n")
    
    if choice < computer_choice :
        print("You lose")
    elif choice == computer_choice:
        print("It's a draw")
    else:
        print("You win!")