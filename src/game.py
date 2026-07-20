
from scoreboard import Score
from snake import Snake
import time
from turtle import Screen, tracer
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("#9bbc0f")
tracer(0)

snake = Snake()
food = Food()
points = Score()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

start = True

while start:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.movement.distance(food) < 15:
        food.random_position()
        snake.snake_grow()
        points.increase_score()

    if (
        snake.movement.xcor() > 280
        or snake.movement.xcor() < -280
        or snake.movement.ycor() > 280
        or snake.movement.ycor() < -280
    ):
        start = False
        points.game_over()
    for tail in snake.vishal_snake[1:]:
        if snake.movement.distance(tail) < 5:
            start = False
            points.game_over()


screen.exitonclick()
