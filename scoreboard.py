import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.score = 0

        self.color("white")

        self.penup()
        self.hideturtle()
        self.set_position(screen_width, screen_height)

    def draw(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   font=("Courier", 18, "italic"))

    def set_position(self, screen_width, screen_height):
        x = -1 * (screen_width / 2) + 25
        y = screen_height / 2 - 38

        self.goto(x, y)


