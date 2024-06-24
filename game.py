from ball import Ball
from brick import RedBrick, YellowBrick, OrangeBrick, GreenBrick
from paddle import Paddle
from screen_wrapper import ScreenWrapper
from scoreboard import Scoreboard
from life_counter import LifeCounter
from game_over_display import GameOverDisplay

GAME_TICK_INTERVAL = 1  # milliseconds


class Game:
    def __init__(self):
        self.paddle = Paddle()
        self.ball = Ball()

        self.screen = ScreenWrapper()
        self.screen.setup_input_handlers(self.paddle)
        self.screen.setup_game_loop_event(game_loop=self.game_loop,
                                          game_tick_interval=GAME_TICK_INTERVAL)

        self.paddle.set_screen_size(self.screen.screen.window_width(),
                                    self.screen.screen.window_height())

        self.paddle.set_initial_pos()

        self.bricks = self.create_bricks(columns=14, rows=8, gap_width=3)

        self.score_board = Scoreboard(self.screen.screen.window_width(),
                                      self.screen.screen.window_height())
        self.life_counter = LifeCounter(self.screen.screen.window_width(),
                                        self.screen.screen.window_height())

        self.ball.random_reset(self.screen.screen.window_width())

        self.game_over_display = GameOverDisplay()

    def game_loop(self):
        self.paddle.move(acceleration=0.35)
        self.ball.move(self.screen.screen.window_width(),
                       self.screen.screen.window_height())
        self.ball.check_paddle_collision(self.paddle, 0.4)

        for brick in self.bricks:
            if brick.check_ball_collision(self.ball):
                self.score_board.score += brick.points
                brick.hide()
                break

        if self.ball.is_off_screen(self.screen.screen.window_height()):
            self.life_counter.lives -= 1
            self.ball.random_reset(self.screen.screen.window_width())

        self.score_board.draw()
        self.life_counter.draw()

        if self.life_counter.lives == 2:
            self.game_over_display.show()
            answer = self.screen.screen.textinput("Game over!", "Play again?: [y/n]")
            if answer == "y":
                self.reset()
            else:
                self.screen.screen.bye()

        self.screen.screen.update()

    def create_bricks(self, rows, columns, gap_width):
        w = self.screen.screen.window_width()
        g = gap_width
        brick_width = (w - g * (columns - 1)) // columns

        x_origin = -1 * w // 2 + brick_width // 2
        y_origin = 245

        bricks = []
        for i in range(columns):
            for j in range(rows):
                x_value = x_origin + i * (brick_width + gap_width)
                y_value = y_origin - j * (gap_width + 15)

                if j < 2:
                    brick_type = RedBrick
                elif j < 4:
                    brick_type = OrangeBrick
                elif j < 6:
                    brick_type = GreenBrick
                else:
                    brick_type = YellowBrick

                brick = brick_type(x=x_value,
                                   y=y_value,
                                   width=brick_width,
                                   height=15)
                bricks.append(brick)
        return bricks

    def start_game_loop(self):
        self.screen.screen.mainloop()

    def reset(self):
        self.game_over_display.clear()
        self.screen.screen.listen()
        self.score_board.score = 0
        self.life_counter.lives = 3
        self.ball.random_reset(self.screen.screen.window_width())

        for brick in self.bricks:
            brick.reset()


if __name__ == "__main__":
    Game().start_game_loop()
