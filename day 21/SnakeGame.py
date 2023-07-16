from SnakeBoard import SnakeBoard
from Snake import Snake
import time


class SnakeGame:

    def __init__(self):
        self.b = SnakeBoard()
        self.b.scr.tracer(0)
        self.snake = Snake()
        self.b.scr.update()
        self.b.scr.tracer(1)
        self.move = {"Up": self.up, "Left": self.left, "Right": self.right, "Down": self.down}
        for _ in self.move:
            self.b.scr.onkey(self.move[_], _)

        while self.detect_collision():
            self.b.scr.tracer(0)
            self.snake.auto_move()
            if self.nome_nome(self.b.food_pos()):
                self.snake.append()
                self.b.update_score()
            self.b.scr.tracer(1)
            time.sleep(1 / self.b.diff)

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

    def nome_nome(self, point):
        if self.snake.snake[len(self.snake.snake) - 1].distance(point[0], point[1]) <= 20:
            self.b.reset_food()
            return True
        return False

    def detect_collision(self):
        for i in range(len(self.snake.snake) - 1):
            if self.snake.snake[i].distance(self.snake.snake[len(self.snake.snake) - 1].position()) < 10:
                self.b.game_over()
                return False
        return True
