import turtle
from turtle import Turtle, Screen
import random as r

ran = r.choice([1, 2, 3, 4, 5])

tim = Turtle()
turtle.colormode(255)
tim.shape("arrow")
tim.color("red")

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# tim.shape("arrow")
# tim.color("black")
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7', 'red',
          '#7FFFD4']

# tim.width(7)
tim.speed(1000)


#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for a in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for i in range(3, 11):
#     tim.color(r.choice(colors))
#     draw_shape(i)

# a = [0, 90, 180, 270, 360]

def rand_color():
    n = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    return n, g, b


#
#
# for _ in range(500):
#     angle = int(r.choice(a))
#     tim.right(angle)
#     tim.forward(30)
#     tim.color(rand_color())
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(rand_color())


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
