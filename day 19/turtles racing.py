import random
import turtle
from turtle import Turtle, Screen, done

TURTLE_WIDTH = 40
turtle.colormode(255)
__turtles = []

colors = ['red',
          'green',
          'blue',
          'yellow',
          'orange',
          'purple',
          'pink',
          'cyan']


def init_the_race():
    y = -150
    random.shuffle(colors)
    for i in range(len(colors)):
        __turtle = Turtle('turtle')
        __turtle.color(colors[i])
        __turtle.penup()
        __turtle.speed(1)
        __turtles.append(__turtle)
    i = len(__turtles) - 1
    while i > -1:
        __turtles[i].goto(x=-275, y=y)
        i -= 1
        y += 42.5


def start_the_race():
    i = 0
    final_line = screen.window_width()//2 - TURTLE_WIDTH//2
    while __turtles[i].xcor() < final_line:
        i = random.randint(0, len(__turtles)-1)
        __turtles[i].fd(random.randint(0, 10))
    turtle.colormode(1)
    return __turtles[i].pencolor()


def result(guessed_color, winning_turtle):
    if guessed_color is not None:
        if winning_turtle == guessed_color:
            print(f"You've won! The {winning_turtle} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_turtle} turtle is the winner!")
    else:
        print(f"The {winning_turtle} turtle is the winner!")


screen = Screen()
screen.setup(width=600, height=400, startx=0, starty=0)

guess = screen.textinput(title="make your bet", prompt="Which color turtle will win in the race?")
guess = guess.lower() if guess is not None else guess

while guess not in colors and guess is not None:
    guess = screen.textinput(title="make your bet", prompt=f"{guess} , not found, choose from rainbow colors.")
    guess = guess.lower() if guess is not None else guess

init_the_race()
winning_turtle = start_the_race()
result(guess, winning_turtle)
done()
