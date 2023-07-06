import art
import random
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from commands import clear
# represent the deck.
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def face_cards():
    """ This function returns a random face card or 10.
      Called after the random choice is 10 ,where 10 represent all the face cards."""
    return random.choice([10, 'J', 'Q', 'K'])

def has_balckjack(player):
    return True if len(player[0]) == 2 and player[1] == 21 else False

def pick_card():
    picked_card = random.choice(cards)
    return picked_card if picked_card != 10 else face_cards()
  
def info(player,dealer,flag):
  if not flag:
    print(f"\n   Your cards: {player[0]}, current score: {player[1]}")
    print(f"   Computer's first card: {dealer[0][0]}\n")
  else :
    print(f"\n   Your final hand: {player[0]}, final score: {player[1]}")
    print(f"   my final hand: {dealer[0]}, final score: {dealer[1]}\n")
  
def initial_score(player_card):
  """Called one time once the game is started."""
  sum = 0
  for card in player_card:
    sum+= card if card not in ['A','J','Q','K'] else 11 if card == 'A' else 10
  return sum
  
def new_game():
    player, dealer = [[], 0], [[], 0]
    player[0] = [pick_card() for _ in range(2)]
    dealer[0] = [pick_card() for _ in range(2)]
    player[1] = initial_score(player[0])
    dealer[1] = initial_score(dealer[0])

    info(player,dealer,False)
  
    if has_balckjack(player):
      info(player,dealer,True)
      print("BlackJack 😳! You won 😤")
      return 10
    elif has_balckjack(dealer):
      info(player,dealer,True)
      print("I won 😎, I have a BlackJack 🤪")
      return 20
    response = input("Type 'hit' to pick another card, or 'stand' to pass:\n> ").lower()
    while response == "hit":
      picked_card = pick_card() 
      player[0].append(picked_card)

      if picked_card in ['J','Q','K']:
        player[1]+= 10
      elif picked_card == 'A':
        player[1]+= 1 if 11 + player[1] > 21 else 11
      else :
        player[1]+= picked_card

      info(player,dealer,False)
      
      if player[1] > 21:
        info(player,dealer,True)
        print(f"You went over. You lose 😹")
        return 0
      elif player[1] == 21:
        break
      else:
        response = input("> ").lower()
        
    while dealer[1] < 16:
      picked_card = pick_card() 
      dealer[0].append(picked_card)

      if picked_card in ['J','Q','K']:
        dealer[1]+= 10
      elif picked_card == 'A':
        dealer[1]+= 1 if 11 + dealer[1] > 21 else 11
      else :
        dealer[1]+= picked_card
      
      if dealer[1] > 21:
        info(player,dealer,True)
        print(f"I went over 😢. You won 😭")
        return 1
        
      elif player[1] == 21:
        info(player,dealer,True)
        print("I won 🥳")
        return 0

    info(player,dealer,True)
    if player[1] > dealer[1]:
      print("You won 😒")
      return 1
    elif player[1] < dealer[1]:
      print("I won 🥳")
      return 0
    else:
      return -1

print(art.logo)
print(art.welcoming)
response = 'y'

while response == 'y':
  result = new_game()
  if result == 0:
    response = input("Type 'yes' if you want to lose again or 'no' if it is enough for you today 🤭\n> ")[0]
    
  elif result == 1:
    response = input("Would you like to play again ,please 🥺👉 👈\n> ")[0]
  
  elif result == 10:
    response = input("That was fast ⚡️, would you like to play again 🙄?\n> ")[0]
  elif result == -1:
    response = input("It's a draw 🤹‍♀️ \nWould you like to start another game ?\n> ")[0]
  else :
    response = input("Would you like to start a new game, loser 😏?\n> ")[0]
  clear()
print("We had a very fun time 😄, see you later 👋 ")