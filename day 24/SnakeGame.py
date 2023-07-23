import turtle

from SnakeBoard import SnakeBoard, draw_boundaries
from Snake import Snake
import time


class SnakeGame:

    def __init__(self):
        self.__board = SnakeBoard()
        self.__move = {"Up": self.up, "Left": self.left, "Right": self.right, "Down": self.down}
        self.__hscore = 0
        self.__snake = None

    def start(self):
        with open('hscore.txt') as highest_score:
            self.__hscore = int(highest_score.read())
        self.__board.board_writer.clear()
        self.__board.scr.listen()
        self.__board.scr.onkey(None, 'Return')
        draw_boundaries()
        self.__board.update_score(0, self.__hscore)
        self.__board.difficulty()
        self.__board.reset_food()

        self.__board.scr.tracer(0)
        self.__snake = Snake()
        self.__board.scr.tracer(1)

        self.__board.scr.listen()
        for _ in self.__move:
            self.__board.scr.onkey(self.__move[_], _)

        score = 0
        flag = False

        while self.detect_collision():
            self.__board.scr.tracer(0)
            self.__snake.move()
            time.sleep(1 / self.__board.diff)
            if self.nome_nome(self.__board.food_pos()):
                self.__snake.append()
                score += self.__board.diff
                if score > self.__hscore:
                    flag = True
                    self.__hscore = score
                    with open('hscore.txt', 'w') as highest_score:
                        highest_score.write(str(self.__hscore))
                self.__board.update_score(score, self.__hscore)
            self.__board.scr.tracer(1)

        self.__board.game_over()
        time.sleep(3)
        self.__snake.hide()
        self.__board.clear(self.__snake)
        if flag:
            self.__board.board_writer.write(f"New High Score: {score}\nScore: {score}", False,
                                            'center', ('Arial', 36, 'bold'))
            self.__hscore = score
        else:
            self.__board.board_writer.write(f"Your Score: {score}", False,
                                            'center', ('Arial', 36, 'bold'))
        self.__board.scr.listen()
        self.__board.scr.onkey(self.start, 'Return')

        return

    def up(self):
        self.__board.scr.tracer(0)
        self.__snake.up()
        self.__board.scr.tracer(1)

    def right(self):
        self.__board.scr.tracer(0)
        self.__snake.right()
        self.__board.scr.tracer(1)

    def down(self):
        self.__board.scr.tracer(0)
        self.__snake.down()
        self.__board.scr.tracer(1)

    def left(self):
        self.__board.scr.tracer(0)
        self.__snake.left()
        self.__board.scr.tracer(1)

    def nome_nome(self, point):
        if self.__snake.snake[len(self.__snake.snake) - 1].distance(point[0], point[1]) <= 17:
            self.__board.reset_food()
            return True
        return False

    def detect_collision(self):
        for i in range(len(self.__snake.snake) - 4):
            if self.__snake.snake[i].distance(self.__snake.snake[len(self.__snake.snake) - 1].position()) < 10:
                return False
        return True
