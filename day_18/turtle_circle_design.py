from random import randint
import turtle as t

turtle = t.Turtle()
t.colormode(255)


def generate_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


turtle.speed("fastest")


def draw_circle_design(size_of_gap):
    for _ in range(360 // size_of_gap):
        turtle.color(generate_random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_circle_design(5)
screen = t.Screen()
screen.exitonclick()
