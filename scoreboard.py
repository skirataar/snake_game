from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 18, 'normal')
FONT2 = ("Courier", 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.score = 0
        self.update_score()
        self.ht()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT1)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("Game Over.", False, ALIGNMENT, FONT2)
