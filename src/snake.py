from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.vishal_snake = []
        self.create_snake()
        self.movement = self.vishal_snake[0]

    def create_snake(self):
        for count in range(3):
            new_thala = Turtle(shape="square")
            new_thala.color("#0f380f")
            new_thala.penup()
            new_thala.goto(x=(count * -20), y=0)
            self.vishal_snake.append(new_thala)

    def snake_grow(self):
        snake_tail = self.vishal_snake[-1]
        new_thala = Turtle(shape="square")
        new_thala.color("#0f380f")
        new_thala.penup()
        new_thala.goto(snake_tail.position())
        self.vishal_snake.append(new_thala)

    def move(self):
        for step in range(len(self.vishal_snake) - 1, 0, -1):
            x_pos = self.vishal_snake[step - 1].xcor()
            y_pos = self.vishal_snake[step - 1].ycor()
            self.vishal_snake[step].goto(x_pos, y_pos)
        self.vishal_snake[0].forward(DISTANCE)

    def move_up(self):
        if self.movement.heading() != DOWN:
            self.movement.setheading(UP)

    def move_down(self):
        if self.movement.heading() != UP:
            self.movement.setheading(DOWN)

    def move_left(self):
        if self.movement.heading() != RIGHT:
            self.movement.setheading(LEFT)

    def move_right(self):
        if self.movement.heading() != LEFT:
            self.movement.setheading(RIGHT)
