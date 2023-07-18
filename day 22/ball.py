import random

from pongboard import SCR_WIDTH, SCR_LEN

from turtle import Turtle


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.setpos(0, 0)
        self.penup()
        self.shape('circle')
        self.color('#fff')
        self.speed(6)

        self.seth(random.randint(0, 359))

        self.fd(speed)
        self.xstep, self.ystep = self.pos()[0], self.pos()[1]

    def bounce_whale(self):
        if self.ycor() > SCR_LEN / 2 - 150 or self.ycor() < SCR_LEN / -2 + 100:
            self.ystep *= -1

    def bounce_with_something(self, something):
        if self.distance(something.pos()) <= 80 and (
                self.xcor() > SCR_WIDTH / 2 - 80 or self.xcor() < SCR_WIDTH / -2 + 80):
            self.xstep *= -1

    def move(self):
        self.bounce_whale()
        self.setpos(self.xcor() + self.xstep, self.ycor() + self.ystep)

    def hit_edge(self):
        if self.xcor() > SCR_WIDTH / 2 - 70 or self.xcor() < SCR_WIDTH / -2 + 60:
            return True
        return False

    def reset(self):
        self.setpos(0, 0)
        self.seth(random.randint(0, 359))
