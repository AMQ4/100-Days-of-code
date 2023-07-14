from turtle import Turtle, Screen, done


def a_head():
    t.fd(50)


def right():
    t.right(10)


def left():
    t.left(10)


def back():
    t.backward(50)


def clear():
    t.clear()


def up():
    if t.isdown():
        t.penup()
    else:
        t.pendown()


def reset():
    t.penup()
    t.home()
    t.pendown()


move = {'w': a_head, 'd': right, 's': back, 'a': left, 'c': clear, 'space': up, 'r': reset}

t = Turtle()
s = Screen()

s.listen()
for key in move:
    s.onkey(move[key], key)

done()
