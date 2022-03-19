from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")
screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increasing_score()

    #detect collision with walls
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset_screen()
        snake.reset_snake()


    #detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment)<5:
            score.reset_screen()
            snake.reset_snake()



screen.exitonclick()