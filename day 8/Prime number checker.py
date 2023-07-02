#Write your code below this line 👇
# trial division

import math
def is_prime(number):
    if number <=1:
        return True
    for i in range(2,int(math.sqrt(n))):
        if(n%i == 0):
            return False
    return True


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))

if is_prime(number=n) == True:
    print(f"It's a prime number.")
else:
    print(f"It's not a prime number.")