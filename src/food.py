import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#0f380f")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.random_position()

    def random_position(self):
        x_axis = random.randint(-280, 280)
        y_axis = random.randint(-280, 280)
        self.goto(x=x_axis, y=y_axis)
