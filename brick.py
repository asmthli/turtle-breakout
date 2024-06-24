import turtle as t

from ball import Ball

BASE_PIXEL_WIDTH = 20
BASE_PIXEL_HEIGHT = 20


class Brick(t.Turtle):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.points = 0
        self.shape("square")
        self.pixel_width = BASE_PIXEL_WIDTH
        self.pixel_height = BASE_PIXEL_HEIGHT
        self.set_size(width, height)

        self.original_x = x
        self.original_y = y

        self.penup()
        self.setx(x)
        self.sety(y)

    def set_size(self, width, height=BASE_PIXEL_HEIGHT):
        width_factor = width / BASE_PIXEL_WIDTH
        height_factor = height / BASE_PIXEL_HEIGHT
        self.shapesize(stretch_len=width_factor, stretch_wid=height_factor)
        self.pixel_width = width
        self.pixel_height = height

    def hide(self):
        self.goto(x=10000, y=10000)

    def reset(self):
        self.goto(x=self.original_x, y=self.original_y)
        
    def check_ball_collision(self, ball: Ball):
        if abs(self.xcor() - ball.xcor()) <= (self.pixel_width + ball.pixel_width) // 2:
            if abs(self.ycor() - ball.ycor()) <= (self.pixel_height + ball.pixel_height) // 2:
                ball.x_plane_bounce()
                return True
        return False


class RedBrick(Brick):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color("red")
        self.points = 7


class OrangeBrick(Brick):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color("orange")
        self.points = 5


class GreenBrick(Brick):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color("green")
        self.points = 3


class YellowBrick(Brick):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color("yellow")
        self.points = 1

