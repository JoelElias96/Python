from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(260, 260)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score:{self.score}", align="right", move=True, font=("Courie", 25, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", move=True, font=("Courie", 25, "normal"))
