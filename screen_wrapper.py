import turtle as t


class ScreenWrapper:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.title("Breakout!")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("slategrey")
        self.screen.tracer(0)

    def setup_input_handlers(self, paddle):
        self.screen.listen()

        self.screen.onkeypress(paddle.start_moving_left, key="a")
        self.screen.onkeypress(paddle.start_moving_right, key="d")
        self.screen.onkeyrelease(paddle.stop_moving_left, key="a")
        self.screen.onkeyrelease(paddle.stop_moving_right, key="d")

    def setup_game_loop_event(self, game_loop, game_tick_interval):
        def game_loop_event_handler():
            game_loop()
            self.screen.ontimer(fun=game_loop_event_handler, t=game_tick_interval)

        # Necessary otherwise first iteration would occur on setup.
        self.screen.ontimer(fun=game_loop_event_handler, t=game_tick_interval)
