from turtle import Screen, Turtle


def close():
    exit(0)


SCR_WIDTH = 1920
SCR_LEN = 1080


class PongBord:
    def __init__(self):
        self.scr = Screen()
        self.scr.bgcolor("black")
        self.scr.setup(.99999999, .9999999999, 0, 0)
        self.scr.listen()
        self.scr.onkey(close, 'Escape')

        self.__writer = Turtle()
        self.__writer.penup()
        self.__writer.color("#fff")
        self.__writer.hideturtle()
        self.__writer.goto(0, SCR_LEN / 2 - 200)

        self.__nopaddles = 2

    def set_paddle(self, paddle):
        if self.__nopaddles == 2:
            paddle.goto(self.scr.window_width() / -2 + 10, 0)
            paddle.set_up_key(self.scr)
            paddle.set_down_key(self.scr)
            self.__nopaddles -= 1

        elif self.__nopaddles == 1:
            paddle.goto(self.scr.window_width() / 2 - 20, 0)
            paddle.set_up_key(self.scr)
            paddle.set_down_key(self.scr)
            self.__nopaddles -= 1

        else:
            print("exceed the limit of paddles.")

        self.scr.listen()

    def update_score(self, paddlea, paddleb):
        self.__writer.clear()
        self.__writer.write(f"{paddlea.score} : {paddleb.score}", False, "center", ("Arial", 36, "bold"))



