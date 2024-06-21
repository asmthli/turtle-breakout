import turtle as t


class ScreenWrapper:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.title("Breakout!")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

    def setup_event_handlers(self, paddle):
        self.screen.listen()

        self.screen.onkeypress(paddle.start_moving_left, key="a")
        self.screen.onkeypress(paddle.start_moving_right, key="d")
        self.screen.onkeyrelease(paddle.stop_moving, key="d")
        self.screen.onkeyrelease(paddle.stop_moving, key="a")
