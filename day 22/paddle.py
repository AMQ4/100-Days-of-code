import time

from pongboard import SCR_LEN
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=7, stretch_len=.7)
        self.penup()

    def set_up_key(self, screen):
        up = screen.textinput("", "select the up key from keyboard")
        screen.listen()
        screen.onkey(self.__up, up)

    def set_down_key(self, screen):
        down = screen.textinput("", "select the down key from keyboard")
        screen.listen()
        screen.onkey(self.__down, down)

    def __up(self):
        if self.ycor() + 20 < SCR_LEN / 2 - 200:
            self.goto(self.xcor(), self.ycor() + 20)

    def __down(self):
        if self.ycor() - 20 > SCR_LEN / -2 + self.shapesize()[0] / 2:
            self.goto(self.xcor(), self.ycor() - 20)
