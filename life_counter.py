import turtle as t


class LifeCounter(t.Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.lives = 3

        self.color("white")

        self.penup()
        self.hideturtle()
        self.set_position(screen_width, screen_height)

    def draw(self):
        self.clear()
        self.write(f"Lives: {self.lives}",
                   align="right",
                   font=("Courier", 18, "italic"))

    def set_position(self, screen_width, screen_height):
        x = (screen_width / 2) - 35
        y = screen_height / 2 - 38

        self.goto(x, y)
