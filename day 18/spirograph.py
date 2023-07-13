import random
from turtle import Turtle, done

t = Turtle()
t.speed(0)
i = 0
t.circle(100)
t.seth(5)
while t.heading() != 0:
    t.color((random.random(), random.random(), random.random()))
    t.circle(100)
    i += 5
    t.seth(i)
done()
