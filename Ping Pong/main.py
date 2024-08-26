from  turtle import Turtle , Screen
from paddle import Paddle
from  ball import Ball
from  scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(800 , 600)
screen.title('Ping PONG')

paddle1 = Paddle((350 , 0))
paddle2 = Paddle((-350 , 0))
ball = Ball()
score= Scoreboard()


screen.listen()

screen.listen()
screen.onkey(paddle1.move_up, "w")  # For moving paddle1 up with 'w'
screen.onkey(paddle1.move_down, "s")  # For moving paddle1 down with 's'
screen.onkey(paddle2.move_up, "Up")  # For moving paddle1 up with 'w'
screen.onkey(paddle2.move_down, "Down")  # For moving paddle1 down with 's'


game_on=True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    if paddle1.ycor() >260:
        paddle1.goto(350, 260)
    elif paddle1.ycor() < -260:
        paddle1.goto(350, -260)

    if paddle2.ycor() >260:
        paddle2.goto(-350, 260)
    elif paddle2.ycor() < -260:
        paddle2.goto(-350, -260)

    ball.move()

    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(paddle2) < 50 and ball.xcor() < -320 or ball.distance(paddle1) < 50 and ball.xcor() >320:
        ball.bounce2()

    if ball.xcor() > 400 :
        ball.return_position()
        score.add_scorel()

    if ball.xcor() < -400 :
        ball.return_position()
        score.add_scorer()
















screen.exitonclick()




