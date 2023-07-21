import random
import time
from math import fabs
from turtle import Screen, mainloop, Turtle
from car import Car, XENDING_COR, XSTARTING_COR

level = 1
min_speed = 5
max_speed = 7
MAX_PLAYER_SPEED = 25


def update_level():
    global level
    screen_writer.clear()
    screen_writer.write(f"Level : {level}", False, "left", font=('Arial', 30, 'normal'))
    level += 1


def cars_generators():
    r = random.randint(1, 4)
    scr.tracer(0)
    j = 200
    i = 1
    while j > - 210:
        c = Car(j)
        c.set_speed(random.randint(min_speed, max_speed))
        cars.append(c)

        i += 1

        if i == r:
            i = 0
            j -= 40 * 2
        else:
            j -= 40
    scr.tracer(1)


def can_set_other_car(__car):
    return fabs(__car.xcor() - XENDING_COR) / __car.get_speed() < fabs(__car.xcor() - XSTARTING_COR) / max_speed


def up():
    player.seth(90)
    step()


def left():
    player.seth(180)
    step()


def right():
    player.seth(0)
    step()


def down():
    player.seth(270)
    step()


def step():
    player.fd(min_speed + max_speed // 2)


scr = Screen()
scr.setup(700, 600, 0, 0)
scr.title("Turtle Crossing Capstone")
scr.listen()
scr.onkey(down, 'Down')
scr.onkey(up, 'Up')
scr.onkey(left, 'Left')
scr.onkey(right, 'Right')
scr.onkey(step, 'space')

screen_writer = Turtle()
screen_writer.penup()
screen_writer.hideturtle()
screen_writer.goto(-350 + 15, 300 - 60)

player = Turtle()
player.shape('turtle')
player.penup()
player.seth(90)
player.setpos(0, -250)
player.speed(0)
update_level()

cars = []
cars_generators()
first_in = cars.copy()

game_running = True
while game_running:
    if player.ycor() > 225:
        scr.tracer(0)
        player.goto(0, -250)
        update_level()
        max_speed += 1
        min_speed += 1 if level % 2 == 1 else 0
        while len(cars) != 0:
            cars[0].hideturtle()
            cars.pop(0)

        while len(first_in) != 0:
            first_in[0].hideturtle()
            first_in.pop(0)

        cars_generators()
        first_in = cars.copy()
        scr.tracer(1)
    scr.tracer(0)
    for __car in cars:
        # if player.xcor() in range(int(__car.xcor()) - 40, int(__car.xcor()) + 45) and \
        #         player.ycor() in range(int(__car.ycor()) - 30, int(__car.ycor()) + 33):

        if player.distance(__car.pos()) <= 26:
            screen_writer.goto(0, 0)
            screen_writer.write("Game Over.", False, 'center', ('Arial', 36, 'normal'))
            time.sleep(3)
            scr.clear()
            screen_writer.write("Game Over.", False, 'center', ('Arial', 36, 'normal'))
            game_running = False
            break
        __car.move()
        if __car.distance(XENDING_COR, __car.ycor()) <= 20:
            __car.hideturtle()
            cars.remove(__car)

    for _ in range(len(first_in)):
        if can_set_other_car(first_in[_]):
            new_car = Car(first_in[_].ycor())
            new_car.set_speed(random.randint(min_speed, max_speed))
            cars.append(new_car)
            first_in[_] = new_car
    scr.tracer(1)
    time.sleep(.03)
mainloop()
