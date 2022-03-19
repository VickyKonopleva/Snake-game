from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("yellow")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

