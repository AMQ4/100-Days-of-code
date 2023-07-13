import random
from colors import colors
import turtle

WIDTH = 300
HEIGHT = 300
RADIUS = 20


def dot(color, radius):
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    move(radius)


def turtle_init():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(-WIDTH, -HEIGHT)
    turtle.pendown()


def move(amount):
    turtle.penup()
    turtle.fd(amount * 5)


turtle_init()

while turtle.ycor() < HEIGHT:
    while turtle.xcor() < WIDTH:
        dot(random.choice(colors), RADIUS)  # also we can use the pre-written one , turtle.dot(color, radius)
    turtle.setx(-WIDTH)
    turtle.sety(turtle.ycor() + RADIUS * 5)
turtle.done()

