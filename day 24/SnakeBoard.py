from random import randint
from turtle import Screen, Turtle

global_drawer = Turtle()


def draw_boundaries():
    global_drawer.showturtle()

    global_drawer.penup()
    global_drawer.goto(-295, -300)

    global_drawer.pendown()
    global_drawer.speed(3)
    global_drawer.color("white")

    global_drawer.fd(585)
    global_drawer.left(90)

    global_drawer.fd(570)
    global_drawer.left(90)

    global_drawer.fd(585)
    global_drawer.left(90)

    global_drawer.fd(570)

    global_drawer.hideturtle()
    global_drawer.left(90)


class SnakeBoard:
    def __init__(self):
        self.diff = 10

        self.scr = Screen()
        self.scr.bgcolor("black")
        self.scr.setup(640, 640, 0, 0)

        self.board_writer = Turtle()
        self.board_writer.hideturtle()
        self.board_writer.penup()
        self.board_writer.color("white")

        self.__food = Turtle()
        self.__food.hideturtle()
        self.__food.shape('circle')
        self.__food.shapesize(stretch_len=.5, stretch_wid=.5)
        self.__food.color('blue')
        self.__food.speed(0)
        self.__food.penup()

    def reset_food(self):
        self.__food.goto(randint(-280, 280), randint(-290, 260))#280
        self.__food.showturtle()

    def food_pos(self):
        pos = (self.__food.xcor(), self.__food.ycor())
        return pos

    def update_score(self, score, hscore):
        self.board_writer.clear()
        self.board_writer.goto(0, 280)
        self.board_writer.write(f"Score: {score}      Highest score: {hscore}",
                                align="center", font=("Arial", 21, "bold"))

    def game_over(self):
        self.board_writer.setpos(0, 0)
        self.board_writer.write(f"Game Over.", align="center", font=("Arial", 21, "normal"))

    def difficulty(self):
        ans = self.scr.textinput("Set Difficulty", "Enter the difficulty level (1-7):")
        if ans is None or ans == '':
            return

        while True:
            if ans is None or ans == '':
                break
            elif not ans.isdigit():
                ans = self.scr.textinput("Set Difficulty", "Invalid input! Difficulty should be a number in [1,7]")
            elif int(ans) not in range(1, 8):
                ans = self.scr.textinput("Set Difficulty", "Incorrect number! Difficulty should be a number in [1,7]")
            else:
                break

        if ans.isdigit():
            self.diff = int(ans) * 10

    def clear(self, snake):
        snake.hide()
        self.__food.hideturtle()
        self.scr.tracer(0)
        self.board_writer.clear()
        global_drawer.clear()
        snake.kill_snake()
        self.scr.bgcolor('#000')
        self.scr.tracer(1)
