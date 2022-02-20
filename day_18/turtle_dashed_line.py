from turtle import Screen, Turtle, forward, penup
import turtle

turtle = Turtle()
screen = Screen()

for i in range(15):
    turtle.pendown() if i % 2 == 0 else turtle.penup()
    turtle.forward(10)

screen.exitonclick()
