import turtle as t


class GameOverDisplay(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    def show(self):
        self.clear()
        self.write("  GAME OVER!",
                   align="center",
                   font=("arial", 20, "normal"))
