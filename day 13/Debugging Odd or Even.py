number = int(input("Which number do you want to check?"))

# the bug: You can't assign an integral value to en expression. 
# how to fix: Change the assignment operator to equality operator '=='if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")