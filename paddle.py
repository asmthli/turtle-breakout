import turtle as t

MOVE_INCREMENT = 5
BASE_PIXEL_WIDTH = 20
BASE_PIXEL_HEIGHT = 20


class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("square")
        self.pixel_width = BASE_PIXEL_WIDTH
        self.pixel_height = BASE_PIXEL_HEIGHT
        self.set_width()

        self.speed = 1

        self.screen_width = None
        self.screen_height = None

        self.direction = None

    def set_initial_pos(self):
        self.goto(0, -250)

    def set_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def set_width(self, stretch_len_factor=6):
        self.shapesize(stretch_len=stretch_len_factor)
        self.pixel_width = BASE_PIXEL_WIDTH * stretch_len_factor

    def start_moving_left(self):
        self.direction = "LEFT"

    def start_moving_right(self):
        self.direction = "RIGHT"

    def stop_moving(self):
        self.direction = None

    def move(self):
        if self.direction is None:
            distance_travelled = 0
        elif self.direction == "LEFT":
            distance_travelled = -1 * self.speed * MOVE_INCREMENT
        elif self.direction == "RIGHT":
            distance_travelled = self.speed * MOVE_INCREMENT
        else:
            distance_travelled = 0

        x_coord = self.xcor() + distance_travelled
        self.setx(x_coord)
