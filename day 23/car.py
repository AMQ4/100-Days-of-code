import random
import turtle
from turtle import Turtle

XSTARTING_COR = 700 / 2 + 40
XENDING_COR = -XSTARTING_COR
turtle.colormode(255)


class Car(Turtle):
    def __init__(self, ycor):
        super().__init__()
        self.set_random_color()
        self.speed(0)
        self.__speed = 0
        self.shape('square')
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.penup()
        self.goto(XSTARTING_COR, ycor)
        self.seth(180)

    def set_random_color(self):
        self.color(random.randint(10, 235), random.randint(10, 235), random.randint(10, 235))

    def set_speed(self, speed):
        self.__speed = speed

    def move(self):
        self.fd(self.__speed)

    def get_speed(self):
        return self.__speed
