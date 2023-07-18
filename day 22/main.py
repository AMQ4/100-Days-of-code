import random
from pongboard import PongBord
from paddle import Paddle
from ball import Ball

game = PongBord()
ball = Ball(random.randint(5, 10))

a, b = Paddle(), Paddle()
game.set_paddle(a)
game.set_paddle(b)
game.update_score(a, b)

while True:
    ball.move()
    ball.bounce_with_something(a)
    ball.bounce_with_something(b)

    if ball.hit_edge():
        if ball.xcor() > 0:
            a.score += 1
        else:
            b.score += 1

        game.update_score(a, b)
        ball.reset()
