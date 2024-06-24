import turtle as t


class GameOverDisplay(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    def show_win(self):
        self.clear()
        self.write("         You win!\nPress Space to Play Again",
                   align="center",
                   font=("arial", 20, "normal"))

    def show_loss(self):
        self.clear()
        self.write("         GAME OVER!\nPress Space to Play Again",
                   align="center",
                   font=("arial", 20, "normal"))
