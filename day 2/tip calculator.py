print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# to calculate the tip , we simply divide the selevted percentage by 100 then multiply it 
# by the amount of bull , then add this result to the bill. However , here the added one is actully 
# the bill! 

tip = (1+tip / 100)
bill = bill * tip

#here I call format function to print 2 numbers after the decimal each time.
print("Each one should pay :{:.2f}".format(round(bill / people,2)))