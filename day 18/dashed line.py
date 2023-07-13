from turtle import *
t = Turtle()
f = True
for i in range(50):
    t.forward(10)
    if f:
        t.penup()
        f = False
    else:
        t.pendown()
        f = True
done()
