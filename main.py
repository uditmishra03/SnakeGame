from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_point = 0
for _ in range(3):
    snake = Turtle("square")
    snake.color("white")
    snake.goto(x= start_point, y=0)
    start_point = start_point -20


screen.exitonclick()