from art import logo
import messages
import random 

def hint(target_number,guessed_number):
    if target_number > guessed_number:
        print("\nToo Low.")
    else:
        print("\nToo High.")
def check_for_incorrect_difficulty_input(response):
    while response not in ["hard","easy","hc"]:
        response = input(" incorrect command typed , type 'easy' or 'hard' ,and 'hc' to hack! 🤫.\n> ")
    return response
def response_to_incorrect_answer(tries):
    selection = random.randint(0,1)
    if selection == 0:
        random_message = random.randint(0,len(messages.sarcasm_messages)-1)
        print(messages.sarcasm_messages[random_message])
        messages.sarcasm_messages.remove(messages.sarcasm_messages[random_message])
    else:
        print(messages.left_tries[tries-1])
def start_game(difficulty):
    target_number = random.randint(1,100)
    tries = 0
    if difficulty in ['easy',"hc"]:
        if difficulty == "hc":
            print(f"\nPssst, the correct answer is {target_number} 🤭")
        guessed_number = int(input("\nYou have 1️⃣ 0️⃣ attempts to crack the code and guess the mystery number! 🎯\nYour guess 🫣  : \n> "))
        tries = 10
        while tries > 1 and guessed_number != target_number:
            if guessed_number not in range(1,101):
                print(f"\n{guessed_number} is out of range 💀, try to guess other number in [1,100] 🫡")
                guessed_number = int(input("Make a guess :\n> "))
                continue
            hint(target_number,guessed_number)
            tries-= 1
            response_to_incorrect_answer(tries)
            guessed_number = int(input(f"You have {messages.number_emojis[tries]} attempts remaining to guess the number.\n\nMake a guess 🫣  : \n> "))
        if tries == 1 :
            print(f"\nOops you lost! 😬\nit was {target_number}\n😬")
            print(messages.game_over_message[random.randint(0,len(messages.game_over_message)-1)])
        elif tries >= 7:
            print("\nThat's correct!")
            print(messages.win_after_smal_tires[random.randint(0,len(messages.win_after_smal_tires)-1)])
        else:
            print("\nYou made it!")
            print(messages.win_ofter_all_tries[random.randint(0,len(messages.win_ofter_all_tries)-1)])
    else:
        guessed_number = int(input("\nYou  have 5️⃣  attempts to crack the code and guess the mystery number! 🎯\nYour guess 🫣  : \n> "))
        tries = 5
        while tries > 1 and guessed_number != target_number:
            if guessed_number not in range(1,101):
                print(f"\n{guessed_number} is out of range 💀, try to guess other number in [1,100] 🫡")
                guessed_number = int(input("Make a guess :\n> "))
                continue
            hint(target_number,guessed_number)
            tries-= 1
            response_to_incorrect_answer(tries)
            guessed_number = int(input(f"You have {messages.number_emojis[tries]} attempts remaining to guess the number.\n\nMake a guess 🫣  : \n> "))
        if tries == 1 :
            print(f"\nOops you lost! 😬\nit was {target_number}\n")
            print(messages.game_over_message[random.randint(0,len(messages.game_over_message)-1)])
        elif tries >= 4:
            print("\nThat's correct!")
            print(messages.win_after_smal_tires[random.randint(0,len(messages.win_after_smal_tires)-1)])
        else:
            print("\nYou made it!")
            print(messages.win_ofter_all_tries[random.randint(0,len(messages.win_ofter_all_tries)-1)])

print(logo)
print("🔢🤔 Guess the Number Game! 🔢🤔".center(50))
print("Can you guess the mysterious number 🔮🕵️‍♂️ I'm thinking of between 1️⃣ and 💯? 🤔")

difficulty =  input("I'm feeling lucky today. I bet you can't guess my number in 5 tries! 😉\n\n'easy' mode 🌼\n'hard' mode 🔥\n> ").lower()
start_game(check_for_incorrect_difficulty_input(difficulty))