from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(
    title="Make your bet",
    prompt="Who will win? (red, green, blue, yellow, black)"
)
colors = ("red", "green", "orange", "blue", "yellow", "purple")
y_position = (-70, -40, -10, 20, 50, 80)

turtles = []
for turtle_index in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-240, y=y_position[turtle_index])
    turtles.append(turtle)

is_race_on = False
if bet != "":
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.pendown()
        turtle.pensize(1)
        distance = randint(0, 11)
        turtle.forward(distance)
        if turtle.xcor() > 240:
            turtle_color = turtle.pencolor()
            print(f"{turtle_color.title()} Turtle won the race.")
            print(
                f"This means, {'won' if bet == turtle_color else 'lost'} the bet!")
            is_race_on = False


screen.exitonclick()
