from turtle import Turtle
FONT=("Courier", 20, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.shape()
        self.ht()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def reset_screen(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.update_scoreboard()

        # self.write("Game over", align="center", font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", align="center", font=FONT)

    def increasing_score(self):
        self.score+=1
        self.update_scoreboard()

