from random import choice
import turtle as t
import colorgram

turtle = t.Turtle()
colors = colorgram.extract("hirst_dot_image.jpeg", 143)

rgb_colors = []
for color in colors:
    rgb_color = color.rgb
    rgb_colors.append((rgb_color.r, rgb_color.g, rgb_color.b))

t.colormode(255)

turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.left(180)
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
turtle.setheading(0)
turtle.pendown()
for _ in range(10):
    for _ in range(13):
        turtle.dot(20, choice(rgb_colors))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(650)
    turtle.setheading(0)
    turtle.pendown()


screen = t.Screen()
screen.exitonclick()
