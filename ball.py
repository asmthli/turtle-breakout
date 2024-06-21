import turtle as t

MOVE_INCREMENT = 5
BASE_PIXEL_WIDTH = 20
BASE_PIXEL_HEIGHT = 20


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("square")
        self.color("red")

        self.pixel_width = BASE_PIXEL_WIDTH
        self.pixel_height = BASE_PIXEL_HEIGHT

        self.x_velocity = 1
        self.y_velocity = 1

    def move(self):
        x_coord = self.xcor() + self.x_velocity * MOVE_INCREMENT
        y_coord = self.ycor() + self.y_velocity * MOVE_INCREMENT
        self.goto(x_coord, y_coord)
