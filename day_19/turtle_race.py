from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet",
                       prompt="Who will win? (red, green, blue, yellow, black)")

red = Turtle("turtle")
green = Turtle("turtle")
blue = Turtle("turtle")
yellow = Turtle("turtle")
black = Turtle("turtle")

for turtle in (red, green, blue, yellow, black):
    turtle.color(str(turtle))


screen.exitonclick()
