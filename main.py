import time
from turtle import Screen
from snake import Snake

TIME_SLEEP = 0.1
SCREEN_BACKGROUND = "black"
GAME_NAME = "Snake Game"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def setup_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND)
    screen.title(GAME_NAME)
    screen.tracer(0)
    screen.listen()
    return screen


def start_game(screen):
    snake = Snake()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(TIME_SLEEP)
        snake.move()


def load_snake_game():
    screen = setup_screen()

    start_game(screen)

    screen.exitonclick()


load_snake_game()
