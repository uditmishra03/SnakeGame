from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
START_POINT = 0
# MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()


class Snake:

    def __init__(self):
        self.chosen_level = None
        self.move_distance = None
        # self.chosen_level = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def difficulty_level(self):
        self.chosen_level = screen.textinput(title="Difficulty level",
                                             prompt="Choose difficulty level.\nFor Easy = 0\nFor Moderate(default) = 1\nFor Difficult = 2 ")
        if self.chosen_level == "2":
            self.move_distance = 20
        elif self.chosen_level == "1":
            self.move_distance = 17
        elif self.chosen_level == "0":
            self.move_distance = 13
        elif self.chosen_level == "":
            print("Invalid input, setting to Moderate mode")
            self.move_distance = 17
        else:
            print("Invalid input, setting to Moderate mode")
            self.move_distance = 17

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

