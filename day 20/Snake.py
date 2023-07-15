from turtle import Turtle


class Snake:

    def __init__(self):
        self.speed = 1
        self.snake = []
        for i in range(-20, 40, 20):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.setx(i)
            t.speed(self.speed)
            self.snake.append(t)

    def auto_move(self):
        for i in range(len(self.snake)):
            if i == len(self.snake) - 1:
                self.snake[i].fd(20)
            else:
                self.snake[i].setpos(self.snake[i + 1].pos())

    def up(self):
        header = len(self.snake) - 1
        if self.snake[header].xcor() - self.snake[header-1].xcor() != 0:
            if self.snake[header].xcor() - self.snake[header-1].xcor() > 0:
                self.snake[header].left(90)
            else:
                self.snake[header].right(90)

    def left(self):
        header = len(self.snake) - 1
        if self.snake[header].ycor() - self.snake[header - 1].ycor() != 0:
            if self.snake[header].ycor() - self.snake[header - 1].ycor() > 0:
                self.snake[header].left(90)
            else:
                self.snake[header].right(90)

    def right(self):
        header = len(self.snake) - 1
        if self.snake[header].ycor() - self.snake[header - 1].ycor() != 0:
            if self.snake[header].ycor() - self.snake[header - 1].ycor() > 0:
                self.snake[header].right(90)
            else:
                self.snake[header].left(90)

    def down(self):
        header = len(self.snake) - 1
        if self.snake[header].xcor() - self.snake[header - 1].xcor() != 0:
            if self.snake[header].xcor() - self.snake[header - 1].xcor() > 0:
                self.snake[header].right(90)
            else:
                self.snake[header].left(90)
