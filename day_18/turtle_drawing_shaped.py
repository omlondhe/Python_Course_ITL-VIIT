from random import choice
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

colors = (
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
)


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.left(angle)


for side in range(3, 21):
    turtle.color(choice(colors))
    draw_shape(side)

screen.exitonclick()
