year = input("Which year do you want to check?")
# the bug: you can not use the modulo '%' operator with a string.
# how to fix: use a type cast to convert from a string to int ,  just uuncomment the 
# following line of code to fix issue.
# year = int(year)

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  