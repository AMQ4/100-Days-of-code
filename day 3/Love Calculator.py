# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# to avoid names LikE THiS 
name1 = name1.upper()
name2 = name2.upper()

# count no. word 'TRUE' occurs
TRUE = name2.count('T') + name1.count('T')

TRUE += name2.count('U') + name1.count('U')
TRUE += name2.count('R') + name1.count('R')
TRUE += name2.count('E') + name1.count('E')

# count no. word 'LOVE' occurs
LOVE = name2.count('L') + name1.count('L')

LOVE += name2.count('O') + name1.count('O')
LOVE += name2.count('V') + name1.count('V')
LOVE += name2.count('E') + name1.count('E')

# now , make a string of two digits and cast as the score of love!
 
count = int(str(TRUE) + str(LOVE))

if count < 10 or count > 90:
    print(f"Your score is {count}, you go together like coke and mentos.")
elif count > 40 and count < 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")