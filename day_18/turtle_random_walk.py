from random import choice, randint
import turtle as t
from turtle import Screen, Turtle

directions = (0, 90, 180, 270)
path_lengths = (30, 20, 10, 50, 40)
pen_sizes = [i for i in range(7, 11)]

turtle = Turtle()
turtle.speed("fastest")
screen = Screen()

t.colormode(255)


def generate_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


for _ in range(121):
    turtle.color(generate_random_color())
    turtle.pensize(choice(pen_sizes))
    turtle.forward(choice(path_lengths))
    turtle.setheading(choice(directions))

screen.exitonclick()
