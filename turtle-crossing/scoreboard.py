from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.color("black")
        self.penup()
        self.goto(-220,260)
        self.hideturtle()
        self.write(f"Level: {self.lvl}", False, "center", FONT)

    def update_scoreboard(self):
        self.lvl += 1
        self.clear()
        self.write(f"Level: {self.lvl}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, "center", FONT)
