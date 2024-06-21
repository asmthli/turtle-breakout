import turtle as t

MOVE_INCREMENT = 2
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

        self.velocity = 0

        self.screen_width = None
        self.screen_height = None

        self.directions_pressed = []

    def set_initial_pos(self):
        self.goto(0, -250)

    def set_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def set_width(self, stretch_len_factor=6):
        self.shapesize(stretch_len=stretch_len_factor)
        self.pixel_width = BASE_PIXEL_WIDTH * stretch_len_factor

    def start_moving_left(self):
        # Check is necessary because of OS-level key repeating.
        if "LEFT" not in self.directions_pressed:
            self.directions_pressed.append("LEFT")

    def start_moving_right(self):
        if "RIGHT" not in self.directions_pressed:
            self.directions_pressed.append("RIGHT")

    def stop_moving_left(self):
        self.directions_pressed.remove("LEFT")

    def stop_moving_right(self):
        self.directions_pressed.remove("RIGHT")

    def move(self, acceleration):
        if not self.directions_pressed:
            self.velocity = 0
        elif self.directions_pressed[-1] == "LEFT":
            self.velocity -= acceleration
        elif self.directions_pressed[-1] == "RIGHT":
            self.velocity += acceleration

        distance_travelled = self.velocity * MOVE_INCREMENT

        x_coord = self.xcor() + distance_travelled
        self.setx(x_coord)
