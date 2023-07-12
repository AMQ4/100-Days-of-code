from data import data
import random
import art
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from syscommand import clear

score = 0

def correct_answer(answer):
    response = None
    while answer not in ['a','b']:
        response = input("incorrect input, juat `A` or `B` \n> ").lower()
    return response

def next_comparison(influenster):
    global score

    second_influenster = None
    clear()
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {influenster['name']}, a {influenster['description']}, from {influenster['country']}.")
    print(art.vs)
    
    second_influenster = random.choice(data)
    data.remove(second_influenster)
    

    print(f"Against B: {second_influenster['name']}, a {second_influenster['description']}, from {second_influenster['country']}.")
    response = input("Who has more followers? Type 'A' or 'B':\n > ").lower()

    if response not in ['A','B']:
        correct_answer(response)
    
    response = influenster if response == 'a' else second_influenster

    if response['follower_count'] == max(influenster['follower_count'],second_influenster['follower_count']) :
        score+= 1
        if len(data) != 0:
            next_comparison(second_influenster)
        else:
            print(f"\nCongratulations, you won !\nFinal score :{score}")
            exit(0)
        
    else:
        clear()
        print(f"Sorry, that's wrong. \nFinal score: {score}")
        exit(0)

def new_game():
    global score

    first_influenster = random.choice(data)
    data.remove(first_influenster)

    second_influenster = random.choice(data)
    data.remove(second_influenster)
    
    
    print(f"Compare A: {first_influenster['name']}, a {first_influenster['description']}, from {first_influenster['country']}.")
    print(art.vs)
    print(f"Against B: {second_influenster['name']}, a {second_influenster['description']}, from {second_influenster['country']}.")
    response = input("Who has more followers? Type 'A' or 'B':\n > ").lower()

    if response not in ['a','b']:
        correct_answer(response)

    response = first_influenster if response == 'a' else second_influenster

    if response['follower_count'] == (first_influenster['follower_count'] if first_influenster['follower_count'] > second_influenster['follower_count']else second_influenster['follower_count']) :
        score+= 1
        next_comparison(second_influenster)
    else:
        clear()
        print(f"Sorry, that's wrong. \nFinal score: {score}")
        exit(0)






print(art.logo)
new_game()
