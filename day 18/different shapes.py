import random
from turtle import *


t = Turtle()
t.penup()
t.sety(-200)
t.pendown()

noSides = 3
angle = 360
lenOfSide = 150
i = 0

while True:
    t.left(angle/noSides)
    t.forward(lenOfSide)
    i += 1

    if i == 11:
        break
    elif i == noSides:
        i = 0
        noSides += 1
        color = (random.random(), random.random(), random.random())
        t.color(color)
done()
