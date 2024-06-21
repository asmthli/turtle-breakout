import time
import turtle as t

from paddle import Paddle
from screen_wrapper import ScreenWrapper


class Game:
    def __init__(self):
        self.paddle = Paddle()

        self.screen = ScreenWrapper()
        self.screen.setup_event_handlers(self.paddle)

        self.paddle.set_screen_size(self.screen.screen.window_width(),
                                    self.screen.screen.window_height())

        self.paddle.set_initial_pos()

    def start_game_loop(self):
        running = True
        while running:
            self.paddle.move()

            time.sleep(0.01)
            t.update()


if __name__ == "__main__":
    Game().start_game_loop()


