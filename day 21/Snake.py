from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        for i in range(-20, 40, 20):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.setx(i)
            t.speed(6)
            self.snake.append(t)

    def auto_move(self):
        if self.snake[len(self.snake)-1].xcor() >= 280:
            self.snake[len(self.snake) - 1].setx(-280)
        if self.snake[len(self.snake)-1].xcor() <= -280 and self.snake[len(self.snake)-1].heading() == 180:
            self.snake[len(self.snake) - 1].setx(280)

        if self.snake[len(self.snake) - 1].ycor() <= -280:
            self.snake[len(self.snake) - 1].sety(250)
        if self.snake[len(self.snake)-1].ycor() >= 250 and self.snake[len(self.snake)-1].heading() == 90:
            self.snake[len(self.snake) - 1].sety(-280)

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

    def append(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.speed(6)

        segment.seth(self.snake[0].heading())
        if segment.heading() == 0 or segment.heading() == 360:
            segment.sety(self.snake[0].ycor())
            segment.setx(self.snake[0].xcor() - 20)
        elif segment.heading() == 180:
            segment.sety(self.snake[0].ycor())
            segment.setx(self.snake[0].xcor() + 20)
        elif segment.heading() == 90:
            segment.setx(self.snake[0].xcor())
            segment.sety(self.snake[0].ycor() - 20)
        else:
            segment.setx(self.snake[0].xcor())
            segment.sety(self.snake[0].ycor() + 20)

        self.snake.insert(0, segment)
