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
        self.initial_width = 6
        self.set_width(self.initial_width)
        self.size = 1

        self.velocity = 0

        self.screen_width = None
        self.screen_height = None

        self.directions_pressed = []

    def set_initial_pos(self):
        self.goto(0, -250)

    def paddle_reset(self):
        self.size = 1
        self.set_width(self.initial_width)

    def reduce_size(self):
        current_width_factor = self.shapesize()[1]
        self.set_width(stretch_len_factor=current_width_factor * 0.85)
        self.size *= 0.85

    def set_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def set_width(self, stretch_len_factor):
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
        if self.check_right_wall_collision():
            self.velocity = 0
        elif self.check_left_wall_collision():
            self.velocity = 0

        if not self.directions_pressed:
            self.velocity = 0
        elif self.directions_pressed[-1] == "LEFT":
            self.velocity -= acceleration
        elif self.directions_pressed[-1] == "RIGHT":
            self.velocity += acceleration

        distance_travelled = self.velocity * MOVE_INCREMENT

        self.setx(self.xcor() + distance_travelled)

        # Stop the player from moving past the walls.
        if self.check_right_wall_collision():
            self.setx(self.screen_width // 2 - self.pixel_width // 2)
        elif self.check_left_wall_collision():
            self.setx(-1 * (self.screen_width // 2 - self.pixel_width // 2))

    def check_right_wall_collision(self):
        return self.xcor() + self.pixel_width // 2 >= self.screen_width // 2

    def check_left_wall_collision(self):
        return self.xcor() - self.pixel_width // 2 <= -1 * self.screen_width // 2
