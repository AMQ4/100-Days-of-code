from turtle import *

t = Turtle()
side = int(input("Enter the length of the square side :\n> "))

for i in range(4):
    t.forward(side)
    t.left(90)

done()
