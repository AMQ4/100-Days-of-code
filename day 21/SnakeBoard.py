from random import randint
from turtle import Screen, Turtle


def draw_boundaries():
    __turtle = Turtle()

    __turtle.penup()
    __turtle.goto(-295, -300)

    __turtle.pendown()
    __turtle.speed(3)
    __turtle.color("white")

    __turtle.fd(585)
    __turtle.left(90)

    __turtle.fd(570)
    __turtle.left(90)

    __turtle.fd(585)
    __turtle.left(90)

    __turtle.fd(570)
    __turtle.hideturtle()


class SnakeBoard:
    def __init__(self):
        self.food = Turtle()
        self.diff = 10

        self.scr = Screen()
        self.scr.bgcolor("black")
        self.scr.setup(640, 640, 0, 0)
        self.difficulty()
        self.scr.listen()

        self.score = 0
        self.board_writer = Turtle()
        self.board_writer.hideturtle()
        self.board_writer.penup()
        self.board_writer.goto(0, 280)
        self.board_writer.color("white")
        self.update_score()

        self.food.shape('circle')
        self.food.shapesize(stretch_len=.5, stretch_wid=.5)
        self.food.color('blue')
        self.food.speed(0)
        self.food.penup()
        self.food.goto(randint(-285, 280), randint(-294, 264))

    def reset_food(self):
        self.food.goto(randint(-285, 280), randint(-294, 264))

    def food_pos(self):
        pos = (self.food.xcor(), self.food.ycor())
        return pos

    def update_score(self):
        self.board_writer.clear()
        self.board_writer.write(f"Score: {self.score}", align="center", font=("Arial", 21, "bold"))
        self.score += self.diff

    def game_over(self):
        self.board_writer.setpos(0, 0)
        self.board_writer.write(f"Game Over.", align="center", font=("Arial", 21, "normal"))

    def difficulty(self):
        ans = ''
        ans = self.scr.textinput("Set Difficulty", "Enter the difficulty level (1-5):")
        if ans is None or ans == '':
            return

        while True:
            if ans is None or ans == '':
                break
            elif not ans.isdigit():
                ans = self.scr.textinput("Set Difficulty", "Invalid input! Difficulty should be a number in [1,5]")
            elif int(ans) not in range(1, 6):
                ans = self.scr.textinput("Set Difficulty", "Incorrect number! Difficulty should be a number in [1,5]")
            else:
                break

        if ans.isdigit():
            self.diff = int(ans) * 10
