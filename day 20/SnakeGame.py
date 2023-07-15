from Board import Board
from Snake import Snake
import time


class SnakeGame:

    def __init__(self):

        self.b = Board()
        self.b.scr.tracer(0)

        self.snake = Snake()
        self.b.scr.update()
        self.b.scr.tracer(1)

        self.move = {"Up": self.up, "Left": self.left, "Right": self.right, "Down": self.down}

        for _ in self.move:
            self.b.scr.onkey(self.move[_], _)

        while True:
            self.b.scr.tracer(0)
            self.snake.auto_move()
            self.b.scr.tracer(1)
            time.sleep(.2)

    def up(self):
        self.b.scr.tracer(0)
        self.snake.up()
        self.b.scr.tracer(1)

    def right(self):
        self.b.scr.tracer(0)
        self.snake.right()
        self.b.scr.tracer(1)

    def down(self):
        self.b.scr.tracer(0)
        self.snake.down()
        self.b.scr.tracer(1)

    def left(self):
        self.b.scr.tracer(0)
        self.snake.left()
        self.b.scr.tracer(1)
