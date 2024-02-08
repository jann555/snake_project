import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
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
    score = Scoreboard()
    snake = Snake()
    food = Food()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(TIME_SLEEP)
        snake.move()
        # Detect Collision with food
        if snake.get_head().distance(food) < 20:
            food.refresh()
            score.increase_score()
            snake.extend_snake()
        # Detect Collision with wall
        if (snake.get_head().xcor() > 288 or snake.get_head().xcor() < -288 or
                snake.get_head().ycor() > 288 or snake.get_head().ycor() < -288):
            game_is_on = False
            score.game_over()
            food.refresh()

        # Detect Collision with body
        for segment in snake.get_snake_body()[1:]:
            if snake.get_head().distance(segment) < 10:
                game_is_on = False
                score.game_over()
                food.refresh()


def load_snake_game():
    screen = setup_screen()

    start_game(screen)

    screen.exitonclick()


load_snake_game()
