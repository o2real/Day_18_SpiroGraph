import turtle
from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

tim = Turtle()

tim = Turtle()
turtle.colormode(255)

tim.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


def draw_spriograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spriograph(1)






screen = Screen()
screen.exitonclick()
