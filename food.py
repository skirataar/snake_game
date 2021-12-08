from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self.slow_power()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)

        self.setpos(random_x, random_y)

    def slow_power(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)

        self.setpos(random_x, random_y)

