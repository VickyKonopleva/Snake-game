from turtle import Turtle
POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
STEP=20
UP=90
LEFT=180
DOWN=270
RIGHT=0
class Snake:

    def __init__(self):
        self.snake=[]
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
        self.head=self.snake[0]

    def reset_snake(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.create_snake()

    def add_segment(self, position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.snake.append(new)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for piece_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece_num - 1].xcor()
            new_y = self.snake[piece_num - 1].ycor()
            self.snake[piece_num].goto(new_x, new_y)
        self.snake[0].forward(STEP)

    def up(self):
        if self.snake[0].heading()!=DOWN:
            self.snake[0].setheading(UP)
            self.move()

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
            self.move()

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
            self.move()

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
            self.move()

