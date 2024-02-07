from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DIRECTION = {"Right": 0, "Up": 90, "Left": 180, "Down": 270}
MOVE_DISTANCE = 20
HEAD = 0
SHAPE = "square"
COLOR = "white"


class Snake:
    def __init__(self) -> None:
        self.__segments = []
        self.__create_snake()
        self.__head = self.__segments[HEAD]

    def __create_snake(self):
        for position in STARTING_POSITIONS:
            link = Turtle()
            link.penup()
            link.shape(SHAPE)
            link.color(COLOR)
            link.goto(position)
            self.__segments.append(link)

    def get_head(self):
        return self.__head

    def snake_grow_snake(self):
        last_link = self.__segments[len(self.__segments) - 1]
        new_segment = (last_link[0], last_link[1])

    def move(self):
        for seg_num in range(len(self.__segments) - 1, 0, -1):
            new_x = self.__segments[seg_num - 1].xcor()
            new_y = self.__segments[seg_num - 1].ycor()
            self.__segments[seg_num].goto(new_x, new_y)
        self.__head.fd(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DIRECTION["Down"]:
            self.__head.setheading(DIRECTION["Up"])

    def down(self):
        if self.__head.heading() != DIRECTION["Up"]:
            self.__head.setheading(DIRECTION["Down"])

    def left(self):
        if self.__head.heading() != DIRECTION["Right"]:
            self.__head.setheading(DIRECTION["Left"])

    def right(self):
        if self.__head.heading() != DIRECTION["Left"]:
            self.__segments[HEAD].setheading(DIRECTION["Right"])
