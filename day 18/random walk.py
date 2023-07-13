import random
from turtle import *

direction = [90, 180, 270, 360]

t = Turtle()
t.pensize(15)
t.speed(0)

for i in range(1000):
    t.seth(random.choice(direction))
    t.color((random.random(), random.random(), random.random()))
    t.forward(20)

done()
