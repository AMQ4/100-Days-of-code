#from replit import clear
from art import logo
from clear import clear_the_terminal
print(logo)
print("\nWelcome to the secrte auction program.")
bidders = {}
response = "yes"
while response == "yes":
  name = input("What is your name? : ")
  bidders[name] = int(input("What's your bids? : $"))
  response = input(
    "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear_the_terminal()

maximum_bid = max(bidders.values())
winners = [bidder for bidder, bid in bidders.items() if bid == maximum_bid]

if len(winners) == 1:
  print("The winner is " + winners[0] +
        f" with a bid of {bidders[winners[0]]}.")
else:
  print("The winners are:")
  print(', '.join(winners))
  print(f"With a bids of {bidders[winners[0]]}.")
