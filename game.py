import time
import turtle as t

from paddle import Paddle
from screen_wrapper import ScreenWrapper

GAME_TICK_INTERVAL = 10  # milliseconds


class Game:
    def __init__(self):
        self.paddle = Paddle()

        self.screen = ScreenWrapper()
        self.screen.setup_input_handlers(self.paddle)
        self.screen.setup_game_loop_event(game_loop=self.game_loop,
                                          game_tick_interval=GAME_TICK_INTERVAL)

        self.paddle.set_screen_size(self.screen.screen.window_width(),
                                    self.screen.screen.window_height())

        self.paddle.set_initial_pos()

    def game_loop(self):
        self.paddle.move()

        self.screen.screen.update()

    def start_game_loop(self):
        self.screen.screen.mainloop()


if __name__ == "__main__":
    Game().start_game_loop()
