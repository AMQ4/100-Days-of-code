from turtle import Screen


class Board:
    def __init__(self):
        self.scr = Screen()
        self.scr.bgcolor("black")
        self.scr.setup(600, 600, 0, 0)
        self.scr.listen()
