from ball import Ball
from brick import RedBrick, YellowBrick, OrangeBrick, GreenBrick
from paddle import Paddle
from screen_wrapper import ScreenWrapper
from scoreboard import Scoreboard
from life_counter import LifeCounter

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

        self.bricks = self.create_bricks(columns=14, gap_width=3)

        self.score_board = Scoreboard(self.screen.screen.window_width(),
                                      self.screen.screen.window_height())
        self.life_counter = LifeCounter(self.screen.screen.window_width(),
                                        self.screen.screen.window_height())

        self.ball.random_reset(self.screen.screen.window_width())

    def game_loop(self):
        self.paddle.move(acceleration=0.35)
        self.ball.move(self.screen.screen.window_width(),
                       self.screen.screen.window_height())
        self.ball.check_paddle_collision(self.paddle, 0.4)

        for brick in self.bricks:
            if brick.check_ball_collision(self.ball):
                self.bricks.remove(brick)
                self.score_board.score += brick.points
                brick.hide()
                break

        if self.ball.is_off_screen(self.screen.screen.window_height()):
            self.life_counter.lives -= 1
            self.ball.random_reset(self.screen.screen.window_width())

        self.score_board.draw()
        self.life_counter.draw()

        self.screen.screen.update()

    def create_bricks(self, columns, gap_width):
        w = self.screen.screen.window_width()
        g = gap_width
        brick_width = (w - g * (columns - 1)) // columns

        x_coord = -1 * w // 2 + brick_width // 2
        bricks = []

        y_values = []

        y_value = 260
        for i in range(8):
            y_value -= (gap_width + 15)
            y_values.append(y_value)

        for i in range(columns):
            brick = RedBrick(x=x_coord, y=y_values[0], width=brick_width, height=15)
            bricks.append(brick)
            brick = RedBrick(x=x_coord, y=y_values[1], width=brick_width, height=15)
            bricks.append(brick)

            brick = OrangeBrick(x=x_coord, y=y_values[2], width=brick_width, height=15)
            bricks.append(brick)
            brick = OrangeBrick(x=x_coord, y=y_values[3], width=brick_width, height=15)
            bricks.append(brick)

            brick = GreenBrick(x=x_coord, y=y_values[4], width=brick_width, height=15)
            bricks.append(brick)
            brick = GreenBrick(x=x_coord, y=y_values[5], width=brick_width, height=15)
            bricks.append(brick)

            brick = YellowBrick(x=x_coord, y=y_values[6], width=brick_width, height=15)
            bricks.append(brick)
            brick = YellowBrick(x=x_coord, y=y_values[7], width=brick_width, height=15)
            bricks.append(brick)

            x_coord += brick_width + gap_width
        return bricks

    def start_game_loop(self):
        self.screen.screen.mainloop()


if __name__ == "__main__":
    Game().start_game_loop()
