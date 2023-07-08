# this is a FizzBuzz game we have done before in day 5 , the 
# program should print 'Fizz' if we get a number divisable
# by 3, 'buzz' when it divisable by 5 ,and FizzBuzz when it 
# divisable by both , 3 and 5.

# the bugs :
# - the program print 'FizzBuzz' when it hitting with a number divisable
#   by 3 or 5 , to fix , change `or` operator to `and` operator.
#
# - the program is still printing the number 3 , that's it because 
#   it uses other if statement instead of elif. So, to fix , change
#   the line of code `if number % 3 == 0:` to `elif number % 3 == 0:`.
#
# - finally , the program print a list instead of the number it self,
#   change the print statement to `print(number)` to fix.

for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])