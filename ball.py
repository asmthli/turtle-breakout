import turtle as t
import random


MOVE_INCREMENT = 2
TOP_INITIAL_SPEED = 2
SPEED_LIMIT = 4


BASE_PIXEL_WIDTH = 20
BASE_PIXEL_HEIGHT = 20


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("circle")
        self.color("red")

        self.pixel_width = BASE_PIXEL_WIDTH
        self.pixel_height = BASE_PIXEL_HEIGHT

        self.x_velocity = 0
        self.y_velocity = -2

    def random_reset(self, window_width):
        x = random.randint(-1 * window_width // 2 + self.pixel_width, window_width // 2 - self.pixel_width)
        self.setx(x)
        self.sety(30)

        self.x_velocity = random.randint(-TOP_INITIAL_SPEED, TOP_INITIAL_SPEED)

    def hide(self):
        self.goto(10000, 10000)

    def move(self, screen_width, screen_height):
        x_coord = self.xcor() + self.x_velocity * MOVE_INCREMENT
        y_coord = self.ycor() + self.y_velocity * MOVE_INCREMENT

        # There is a bizarre bug - The window does not seem to show the full
        # width of the screen in the positive direction. No div by 2 to account for this.
        if x_coord + self.pixel_width >= (screen_width // 2):
            x_coord = (screen_width // 2) - self.pixel_width
            self.y_plane_bounce()
        elif x_coord - self.pixel_width // 2 <= -1 * (screen_width // 2):
            x_coord = -1 * (screen_width // 2) + self.pixel_width // 2
            self.y_plane_bounce()

        if y_coord + self.pixel_height / 2 >= (screen_height // 2):
            y_coord = (screen_height // 2) - self.pixel_height // 2
            self.x_plane_bounce()

        self.goto(x_coord, y_coord)

    def is_off_screen(self, screen_height):
        return self.ycor() < -1 * screen_height // 2

    def check_paddle_collision(self, paddle, momentum_coefficient):
        if abs(self.xcor() - paddle.xcor()) <= (self.pixel_width + paddle.pixel_width) // 2:
            if abs(self.ycor() - paddle.ycor()) <= (self.pixel_height + paddle.pixel_height) // 2:
                self.paddle_bounce(paddle, momentum_coefficient=momentum_coefficient)

    def paddle_bounce(self, paddle, momentum_coefficient):
        speed_boost = momentum_coefficient * paddle.velocity
        if abs(self.x_velocity + speed_boost) <= SPEED_LIMIT:
            self.x_velocity += speed_boost

        if self.ycor() > paddle.ycor():
            self.x_plane_bounce()
            self.sety(paddle.ycor() + paddle.pixel_height / 2 + self.pixel_height / 2)
        elif self.xcor() < paddle.xcor():
            self.y_plane_bounce()
            self.setx(paddle.xcor() - paddle.pixel_width / 2 - self.pixel_width / 2)
        elif self.xcor() > paddle.xcor():
            self.y_plane_bounce()
            self.setx(paddle.xcor() + paddle.pixel_width / 2 + self.pixel_width / 2)

    def x_plane_bounce(self):
        self.y_velocity *= -1

    def y_plane_bounce(self):
        self.x_velocity *= -1
