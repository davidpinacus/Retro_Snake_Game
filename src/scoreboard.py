from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        #self.high_score=0
        self.penup()
        self.hideturtle()
        self.goto(y=275, x=0)
        self.color("#0f380f")
        self.score = 0

        with open("high_score.txt") as file:
            self.high_score=int(file.read())
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", align="center", font=("Courier", 17, "bold"))

    
    def check_score(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("high_score.txt","w") as file:
                file.write(str(self.high_score))

    def increase_score(self):
        self.score+=1
        self.check_score()
        self.display()
    
    def display(self):
        self.clear()
        self.write(f"Score: {self.score}        High Score:{self.high_score}", align="center", font=("Courier", 17, "bold"))

