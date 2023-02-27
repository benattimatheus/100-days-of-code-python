import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("darkgreen")
t.colormode(255)

### Dashed line

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


### Shapes

# colors = ["cyan", "gold, "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray",
#    "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


### Random Walk


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# directions = [0, 90, 180, 270]
#
# tim.speed("fastest")
# tim.pensize(15)
# for _ in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)


### Spirograph


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()