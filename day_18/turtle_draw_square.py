from turtle import Screen, Turtle

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()
