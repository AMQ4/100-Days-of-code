<<<<<<< HEAD
import logo
import math

=======
import math
>>>>>>> origin/main
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text , shift):
    text = list(text)
    for i in range(len(text)):
<<<<<<< HEAD
        if text[i] not in alphabet:
            continue
=======
>>>>>>> origin/main
        text[i] = alphabet[(alphabet.index(text[i])+shift) % 26]
    return ''.join(text)

def decrypt(text,shift):
    return encrypt(text=text,shift= int(math.fabs(26-shift%26)))

<<<<<<< HEAD



print(logo.logo)

response = "yes"
while response == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        print("The encoded text is: "+encrypt(text=text,shift=shift))
    else:
        print("The decoded text is: "+decrypt(text=text,shift=shift))

    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    
=======
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    print("The encoded text is: "+encrypt(text=text,shift=shift))
else:
    print("The decoded text is: "+decrypt(text=text,shift=shift))

>>>>>>> origin/main
